# Error Base Class

class Error:
    def __init__(self, name = "Error Type", lineNum = 0):
        self._name = name
        self._lineNum = lineNum
