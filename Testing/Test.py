import unittest
import itertools

class MyTestCase(unittest.TestCase):
    def test_something(self):

        foo = ['a', 'b', 'c']
        bar = [1, 2]

        for f, b in itertools.zip_longest(foo, bar):
            print(f, b)


if __name__ == '__main__':
    unittest.main()
