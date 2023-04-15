import unittest
from classes.guest_class import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Louise Ciccone", 64, "Holiday", 50)
        self.guest2 = Guest("Miley Cyrus", 30, "Paranoid", 40)
        self.guest3 = Guest("Ozzy Osborne", 74, "Flowers", 10)


#3 tests here

    def test_can_create_guest(self):
        self.assertEqual(64, self.guest1.age)
        self.assertEqual(50, self.guest1.wallet)

#Extension work
    def test_reduce_wallet(self):
        self.guest2.reduce_wallet(15)
        self.assertEqual(25, self.guest2.wallet)

    def test_not_enough_money(self):
        self.assertEqual(False, self.guest3.reduce_wallet(15))
