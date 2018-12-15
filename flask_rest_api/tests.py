from unittest import TestCase
from mymodules.fibonacci import get_fib_sequence

class FibonacciSequenceTestCase(TestCase):

    def test_fibonacci_sequence_returns_list(self):
        self.assertEqual(get_fib_sequence(3, 5), [2,3,5])

    def test_fibonacci_sequence_raises_overflow_error(self):
        self.assertRaises(OverflowError, get_fib_sequence, 0, 100)

    def test_fibonacci_sequence_raises_value_error(self):
        self.assertRaises(ValueError, get_fib_sequence, -20, -10)
        self.assertRaises(ValueError, get_fib_sequence, 30, 10)

    def test_fibonacci_sequence_error_message(self):
        self.assertRaises(ValueError, get_fib_sequence, -20, 30)

        try:
            get_fib_sequence(-20, 30)
        except ValueError as err:
            self.assertEqual(str(err), "Start index should be less than end index and both should be positive integers")