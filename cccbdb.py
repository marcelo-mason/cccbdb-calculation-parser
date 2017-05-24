import sys
import runner


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Syntax: python cccbdb.py [method] [formula]')
        exit()

    # command line args
    method = sys.argv[1]
    formula = sys.argv[2]

    if method == 'geom':
        runner.run(method, formula, 'http://cccbdb.nist.gov/geom1x.asp', 'http://cccbdb.nist.gov/geom2x.asp', deep=True)

    if method == 'dipole':
        runner.run(method, formula, 'http://cccbdb.nist.gov/dipole1x.asp', 'http://cccbdb.nist.gov/dipole2x.asp', deep=False)
