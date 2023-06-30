import unittest
from shop import purchased, retry_purchase, ThreeFailedAttempts


class TestingPurchased(unittest.TestCase):
    # VALID CASES
    def test_purchased_with_enough_money(self):
        self.assertEqual(True, purchased(item="Phone", balance=100))

    # INVALID/ERRONEOUS CASES
    def test_purchased_with_not_enough_money(self):
        self.assertFalse(purchased(item="TV", balance=100))
    def test_purchased_with_negative_money(self):
        self.assertEqual(False, purchased(item="Phone", balance=-100))

    # BOUNDARY CASE
    def test_purchased_with_just_enough_money(self):
        self.assertTrue(purchased(item="TV", balance=1000))

class TestingRetryPurchase(unittest.TestCase):
    # TESTING RAISED CUSTOM ERROR
    def test_retrypurchased_too_many_attempts(self):
        with self.assertRaises(ThreeFailedAttempts):
            retry_purchase(item="TV", balance=100, attempts=3),

if __name__ == '__main__':
    unittest.main()