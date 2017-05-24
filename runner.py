import os
import requests
import extract
import writer
import constant
from bs4 import BeautifulSoup


def run(calculation, formula, depth='shallow'):
    data = {
        'formula': formula,
        'submit1': 'Submit'
    }

    url1 = 'http://cccbdb.nist.gov/%s1x.asp' % calculation
    url2 = 'http://cccbdb.nist.gov/%s2x.asp' % calculation

    while True:
        try:
            # request initial url
            session = requests.Session()
            res = session.post(constant.URLS['form'], data=data, headers=constant.headers(url1), allow_redirects=False)

            # follow the redirect
            if res.status_code == 302:
                res2 = session.get(url2)

            # find tables
            soup = BeautifulSoup(res2.content, 'html.parser')
            predefined = soup.find('table', attrs={'id': 'table1'})
            standard = soup.find('table', attrs={'id': 'table2'})
            effective = soup.find('table', attrs={'id': 'table3'})

            # extract data (including links to codes)
            p_results = extract.simple(predefined)
            s_results = extract.complex(standard)
            e_results = extract.complex(effective)
        except:
            continue
        break

    # create file
    file = open(os.path.join(os.getcwd(), formula + '.' + calculation + '.' + depth + '.txt'), 'w')

    # for each link in data
    if depth == 'deep':
        for result in (p_results + s_results + e_results):
            while True:
                try:
                    # pull codes
                    session.get(result['url'])
                    res4 = session.post(constant.URLS['dump'])
                    soup = BeautifulSoup(res4.content, 'html.parser')
                    codes = soup.find('textarea').text

                    writer.file(file, result, codes)
                    writer.console(result)
                except:
                    continue
                break
    else:
        for result in (p_results + s_results + e_results):
            writer.file_shallow(file, result)
            writer.console(result)
    file.close()
