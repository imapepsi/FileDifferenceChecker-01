# Line Class

class Line:
    def __init__(self, num, versionOne, versionTwo):
        self._num = num
        self._versionOne = versionOne
        self._versionTwo = versionTwo
        self._charErrors = []  # List of Character Errors in the line

    def addError(self, newError):
        self._charErrors.append(newError)

    def printErrors(self):
        # Lines are printed here because one line may have multiple errors
        if self._num is None:
            print(f"Line[missing]: '{self._versionOne}' | '{self._versionTwo}'")
        elif (self._versionOne == "" or self._versionTwo == "") and (self._versionOne != self._versionTwo):
            # If only one of the lines is "" then a line was skipped
            print(f"Line[{self._num}]: '{self._versionOne}' | '{self._versionTwo}'")
            print("  Skipped")
        else:
            print(f"Line[{self._num}]: '{self._versionOne}' | '{self._versionTwo}'")

        for e in self._charErrors:
            e.printError()
