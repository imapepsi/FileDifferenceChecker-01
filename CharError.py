# Character Error Class

import Error


class CharError(Error.Error):  # Error with character types
    def __init__(self, lineNum, version1, version2, charNum, char1, char2):
        self._lineNum = lineNum
        self._version1 = version1
        self._version2 = version2
        self._charNum = charNum
        self._char1 = char1
        self._char2 = char2

    def printError(self):
        if self._charNum is None:
            print(f"  Char[end]: '{self._char1}' -> '{self._char2}'")
        else:
            print(f"  Char[{self._charNum}]: '{self._char1}' -> '{self._char2}'")
