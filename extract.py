from table_parser import HTMLTableParser


def simple(list):
    results = []
    p = HTMLTableParser()
    p.feed(str(list))
    for row in p.tables[0]:
        detail = {
            'level': row[0][0],
            'bond': row[1][0],
            'url': 'http://cccbdb.nist.gov/' + row[1][1] if len(row[1]) > 1 else ''
        }
        results.append(detail)
    return results


def complex(list):
    results = []
    p = HTMLTableParser()
    p.feed(str(list))
    headers = p.tables[0][0]
    # remove first 2 blank columns from header row
    del headers[0]
    del headers[0]
    for row in p.tables[0]:
        # only lines with a level
        if len(row[0]) > 0:
            level = row[0][0]
            for index, bond in enumerate(row):
                # only bond that have content
                if len(bond) == 2:
                    detail = {
                        'level': level,
                        'basis': headers[index-1][0],
                        'bond': bond[0],
                        'url': 'http://cccbdb.nist.gov/' + bond[1]
                    }
                    results.append(detail)
    return results
