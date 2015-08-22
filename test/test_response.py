from response import response
__author__ = 'johnson'

import unittest


class MyTestCase(unittest.TestCase):
    def test_response(self):
        print response(result='test')


if __name__ == '__main__':
    unittest.main()
