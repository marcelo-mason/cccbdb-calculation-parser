# cccbdb.nist.gov Geometry Parser

Pulls all geometry and dipole information from cccbdb.nist.gov for the specified chemical formula

## Setup

* Install Python 3

* Clone the repo to your machine

`git clone git@github.com:marcelo-mason/cccbdb-geometry-parser.git && cd cccbdb-geometry-parser`

* Install script dependencies

`python setup.py develop`

* Run the script by supplying the following command line arguments

`Syntax: python cccbdb.py [method] [formula] [deep/shallow]`

**The method you get from the ccbdb url**  
i.e. the method for this url *http://cccbdb.nist.gov/polcalc1x.asp* is "polcalc"

*Examples:*

`python cccbdb.py geom CH4 deep`

`python cccbdb.py dipole CH4 shallow`

* The script will run through extracting the data and outputting status to the console.  It will create a text file in your current path with the output.

# Screenshots

![Console](screenshots/console.jpg)

![output](screenshots/output.jpg)
