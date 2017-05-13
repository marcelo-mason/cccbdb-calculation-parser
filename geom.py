import sys
import os
import requests
import extract
from bs4 import BeautifulSoup


#####################################

URLS = {
    'form': 'http://cccbdb.nist.gov/getformx.asp',
    'geom2': 'http://cccbdb.nist.gov/geom2x.asp',
    'dump': 'http://cccbdb.nist.gov/carttabdumpx.asp'
}

HEADERS = {
    'Host': 'cccbdb.nist.gov',
    'Connection': 'keep-alive',
    'Content-Length': 26,
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Origin': 'http://cccbdb.nist.gov',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://cccbdb.nist.gov/geom1x.asp',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-CA,en-GB;q=0.8,en-US;q=0.6,en;q=0.4',
}

#####################################


def run(formula):
    data = {
        'formula': formula,
        'submit1': 'Submit'
    }

    # request initial url
    session = requests.Session()
    res = session.post(URLS['form'], data=data, headers=HEADERS, allow_redirects=False)

    # follow the redirect using same session cookie
    if res.status_code == 302:
        res2 = session.get(URLS['geom2'])

    # find tables
    soup = BeautifulSoup(res2.content, 'html.parser')
    predefined = soup.find('table', attrs={'id': 'table1'})
    standard = soup.find('table', attrs={'id': 'table2'})
    effective = soup.find('table', attrs={'id': 'table3'})

    # extract data (including links to codes)
    p_results = extract.simple(predefined)
    s_results = extract.complex(standard)
    e_results = extract.complex(effective)

    # create file
    file = open(os.getcwd() + formula + '.txt', 'w')

    # for each link in data
    for result in (p_results + s_results + e_results):
        try:
            # pull codes
            session.get(result['url'])
            res4 = session.post(URLS['dump'])
            soup = BeautifulSoup(res4.content, 'html.parser')
            codes = soup.find('textarea').text

            # remove blank lines
            clean_codes = os.linesep.join([s for s in codes.splitlines() if s.strip()])

            # write to file
            file.write(result['level'] + '\n')
            if 'basis' in result:
                file.write(result['basis'] + '\n')
            file.write(result['bond'] + '\n')
            file.write(clean_codes + '\n')
            file.write('-------------------------------------------\n')
            result.pop('url', None)
            print(str(result))
        except Exception as e:
            result.pop('url', None)
            print('failed: ' + str(result))

    file.close()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Syntax: python geom.py [formula]')
        exit()

    run(sys.argv[1])
