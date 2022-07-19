import unittest


class MyTestCase(unittest.TestCase):
    def test_sameFiles(self):
        print("Same Files")

    def test_characterDiff(self):
        print("Mismatch Characters")

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
