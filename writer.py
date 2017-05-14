import os


def file(file, result, codes):
    # remove blank lines from code
    clean_codes = os.linesep.join([s for s in codes.splitlines() if s.strip()])

    # write code to file
    file.write(result['level'] + '\n')
    if 'basis' in result:
        file.write(result['basis'] + '\n')
    file.write(result['bond'] + '\n')
    file.write(clean_codes + '\n')
    file.write('-------------------------------------------\n')
    file.flush()


def console(result, failed=False):
    result.pop('url', None)
    if failed:
        print('failed: ' + str(result))
    else:
        print(str(result))
