URLS = {
    'form': 'http://cccbdb.nist.gov/getformx.asp',
    'dump': 'http://cccbdb.nist.gov/carttabdumpx.asp',
    'dump2': 'http://cccbdb.nist.gov/tabdumpx.asp',
}


def headers(referer):
    return {
        'Host': 'cccbdb.nist.gov',
        'Connection': 'keep-alive',
        'Content-Length': '26',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Origin': 'http://cccbdb.nist.gov',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': referer,
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-CA,en-GB;q=0.8,en-US;q=0.6,en;q=0.4',
    }
