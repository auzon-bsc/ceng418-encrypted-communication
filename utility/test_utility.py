import unittest
import utility

class TestUtility(unittest.TestCase):
    
    def test_is_prime(self):
        self.assertEqual(utility.is_prime(3), True)
        self.assertEqual(utility.is_prime(19), True)
        self.assertEqual(utility.is_prime(1319), True)
        self.assertEqual(utility.is_prime(6700417), True)
        self.assertEqual(utility.is_prime(4), False)
        self.assertEqual(utility.is_prime(1729), False)

    def test_is_generator(self):
        self.assertEqual(utility.is_generator(2, 11), True)
        self.assertEqual(utility.is_generator(3, 11), False)

        with self.assertRaises(ValueError):
            (utility.is_generator(3, 20), False)


if __name__ == "__main__":
    unittest.main()