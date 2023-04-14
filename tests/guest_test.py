import unittest
from classes.guest_class import *

class TestGuest(unittest.TestCase):
    
#Test 1
    def test_can_create_guest(self):
        guest1 = Guest("Louise Ciccone", 64, "Holiday")
        #print(guest1.age)
        self.assertEqual(64, guest1.age)
