import sys
import runner


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Syntax: python cccbdb.py [calculation] [formula] [deep/shallow]')
        print('Example: python cccbdb.py dipole CH4 shallow')
        print('Example: python cccbdb.py geom CH4 deep')
        exit()

    # command line args
    calculation = sys.argv[1]
    formula = sys.argv[2]
    depth = sys.argv[3]

    # run the parser
    runner.run(calculation, formula, depth)
