import unittest
from shop import purchased, retry_purchase, ThreeFailedAttempts

class TestingPurchased(unittest.TestCase):
    
    # CASES THAT WERE PREVIOUSLY PROVIDES IN THE EXAMPLE BECKY ATTACHED
    def test_purchased_with_not_enough_money(self):
        self.assertFalse(purchased(item="Phone", balance=100))
    def test_purchased_with_negative_money(self):
        self.assertEqual(False, purchased(item="Watch", balance=-100))

    # NEW CASES I SUGGEST WE ADD:

    # Case when user has 0 balance

    def test_purchased_with_zero_balance(self):
        self.assertFalse(purchased(item="Phone", balance=0))

    #case when the person chooses an item that is not part of the available items:

    def test_purchased_with_invalid_item(self):
        self.assertFalse(purchased(item="Laptop", balance=100))

class TestingRetryPurchase(unittest.TestCase):
    # TESTING RAISED CUSTOM ERROR THAT BECKY PROVIDED
    def test_retrypurchased_too_many_attempts(self):
        with self.assertRaises(ThreeFailedAttempts):
            retry_purchase(item="TV", balance=100, attempts=3),

if __name__ == '__main__':
    unittest.main()