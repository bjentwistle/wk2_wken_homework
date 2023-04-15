import unittest
from classes.guest_class import *
from classes.song_class import *
from classes.room_class import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Madonna Room", 20)
        self.room2 = Room("Take That Room", 0) #for testing add_guest_to_room when it's full
        self.guest1 = Guest("Louise Ciccone", 64, "Holiday", 50)
        self.guest2 = Guest("Miley Cyrus", 30, "Paranoid", 40)
        self.guest3 = Guest("Ozzy Osborne", 74, "Flowers", 100)
        self.song1 = Song("Holiday", "Madonna", "Pop", 4)
        self.song2 = Song("Paranoid", "Black Sabbath", "Heavy Metal", 7)
        self.song3 = Song("Flowers", "Miley Cyrus", "Pop", 3)

# 7 Tests here

    def test_can_create_room_instance(self):
        self.assertEqual("Madonna Room", self.room1.name)

    def test_room_instance_has_capacity(self):
        self.assertEqual(20, self.room1.capacity)

#I want to test that I can add a guest to a room
    def test_add_guest_to_room(self):
        result1 = self.room1.add_guest_to_room(self.guest1)
        result2 = self.room1.add_guest_to_room(self.guest2)
        self.assertEqual(2, len(self.room1.occupancy))
        self.assertEqual(True, result1)
        self.assertEqual(True, result2)

#checking if room capacity is full before adding guest - part of extesnion work
    def test_add_guest_to_full_room(self):
        response = self.room2.add_guest_to_room(self.guest1)
        self.assertEqual(False, response) 

#Now I want to remove a guest from a room
    def test_remove_guest_from_room(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_guest_to_room(self.guest2)
        self.room1.remove_guest_from_room(self.guest1)
        self.assertEqual("Miley Cyrus", self.room1.occupancy[0].name)
        self.assertEqual(1, len(self.room1.occupancy)) #occupancy changes as the guests leave.

#To add and remove songs from the list
    def test_add_song_to_song_list(self):
        self.room1.add_song_to_song_list(self.song1)
        self.assertEqual("Holiday", self.room1.song_list[0].name)

    def test_remove_song_from_song_list(self):
        self.room1.add_song_to_song_list(self.song1)
        self.room1.add_song_to_song_list(self.song2)
        self.assertEqual(2, len(self.room1.song_list))
        self.room1.remove_song_from_song_list(self.song1)
        self.assertEqual("Paranoid", self.room1.song_list[0].name)



