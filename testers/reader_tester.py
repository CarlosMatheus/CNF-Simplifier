import unittest
import reader


class TestReader(unittest.TestCase):

    def test_read(self):
        r = reader.Reader()
        file = r.read('input00.txt')
        print(file)
        # self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
