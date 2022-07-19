import Checker
import unittest

class MyTestCase(unittest.TestCase):
    # def __init__(self):
    #     self._checker = Checker.Checker(str(sys.argv[1]), str(sys.argv[2]))

    def test_sameFiles(self):
        print("Same Files")
        checker = Checker.Checker("Test00a.txt", "Test00b.txt")
        checker.errorCheck()
        checker.printErrors()

        # Expected Output
        """ 
        Same Files
        Files are Identical
        """


    def test_characterDiff(self):
        print("Mismatch Characters")
        checker = Checker.Checker("Test01a.txt", "Test01b.txt")
        checker.errorCheck()
        checker.printErrors()


    def test_extraCharacters(self):
        print("Extra Characters")

    def test_extraLines(self):
        print("Extra Lines")

    def test_skippedLines(self):
        print("Skipped Lines")

    def test_differentLines(self):
        print("Skipped Lines")


if __name__ == '__main__':
    unittest.main()
