import unittest

from fib import fibonacci

class TestFib(unittest.TestCase):

    def test_fib_9_is_34(self):
        self.assertEqual(fibonacci(9),34)

    def test_fib_9_is_34_2(self):
        result = fibonacci(9)
        expected = 34
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()