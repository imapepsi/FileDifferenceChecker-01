# Checker Class
import CharError
import itertools
import Line


def removeNewLines(file):
    """Take out any new lines from lines of a file ['line1\n', 'line2\n', ... ]"""

    newFile = []
    for line in file:
        newFile.append(line.rstrip())

    return newFile


class Checker:
    def __init__(self, name1, name2):
        self._file1 = removeNewLines(open(name1, 'r').readlines())
        self._file2 = removeNewLines(open(name2, 'r').readlines())
        self._lines = []  # List of lines
        self._errorCount = 0

    def errorCheck(self):
        """Check for errors in each line"""
        for (index, one, two) in itertools.zip_longest(range(len(self._file1)), self._file1, self._file2):
            if (one is None or one == "") and (two is not None or two == ""):  # File1 is shorter
                newLine = Line.Line(index, "", two)
                self._errorCount += 1
            elif (two is None or two == "") and (one is not None or one != ""):  # File2 is longer
                newLine = Line.Line(index, one, "")
                self._errorCount += 1

            else:  # Files are Same length
                newLine = Line.Line(index, one, two)

                for (charIndex, charOne, charTwo) in itertools.zip_longest(range(len(one)), one, two):
                    if charOne != charTwo:
                        self._errorCount += 1
                        newLine.addError(CharError.CharError(index, one, two, charIndex, charOne, charTwo))

            self._lines.append(newLine)

        # TODO: What should happen is a line is extra long? Test 3
        # Example Output: line vs line!!!
        #   Char[end]: 'None' -> '!'
        #   Char[end]: 'None' -> '!'
        #   Char[end]: 'None' -> '!'
        # Example Output: line!!! vs line
        #   Char[4]: '!' -> 'None'
        #   Char[5]: '!' -> 'None'
        #   Char[6]: '!' -> 'None'

        # TODO: What should happen if a line is "a different line" altogether?
        # What defines a different line
        # How should the error look?

    def printErrors(self):
        if self._errorCount == 0:
            print("Files are Identical")
        else:
            print("\t" + "File Differences" + "\n")
            for line in self._lines:
                line.printErrors()
