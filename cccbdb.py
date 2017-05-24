import sys
import runner


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Syntax: python cccbdb.py [method] [formula] [deep/shallow]')
        print('Example: python cccbdb.py dipole CH4 shallow')
        print('Example: python cccbdb.py geom CH4 deep')
        exit()

    # command line args
    method = sys.argv[1]
    formula = sys.argv[2]
    depth = sys.argv[2]

    # run the parser
    runner.run(method, formula, depth)
