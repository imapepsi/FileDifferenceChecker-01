"""
File Difference Checker

Mia Seppi
7/16/2022
"""

import Checker
import sys

if __name__ == '__main__':
    # Get Input files to read in
    fileName1 = str(sys.argv[1])
    fileName2 = str(sys.argv[2])

    try:
        myCheck = Checker.Checker(fileName1, fileName2)

        myCheck.errorCheck()

        myCheck.printErrors()

    except Exception as e:
        print(e)
