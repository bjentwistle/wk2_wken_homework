import unittest
from classes.guest_class import *
from classes.song_class import *
from classes.room_class import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Madonna Room", 20)
        self.guest1 = Guest("Louise Ciccone", 64, "Holiday")
        self.guest2 = Guest("Miley Cyrus", 30, "Paranoid")
        self.guest3 = Guest("Ozzy Osborne", 74, "Flowers")
        self.song1 = Song("Holiday", "Madonna", "Pop", 4)
        self.song2 = Song("Paranoid", "Black Sabbath", "Heavy Metal", 7)
        self.song3 = Song("Flowers", "Miley Cyrus", "Pop", 3)

#test 3
    def test_can_create_room_instance(self):
        room1 = Room("Room_1", 20)
        #print(room1.room_name)
        self.assertEqual("Room_1", room1.name)
#test 4
    def test_room_has_capacity(self):
        room1 = Room("Room_1", 20)
        #print(room1.capacity)
        self.assertEqual(20, room1.capacity)

#I want to test that I can add a guest to a room
    def test_add_guest_to_room(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_guest_to_room(self.guest2)
        self.assertEqual(2, len(self.room1.occupancy))

#Now I want to remove a guest from a room
    def test_remove_guest_from_room(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_guest_to_room(self.guest2)
        self.room1.remove_guest_from_room(self.guest1)
        self.assertEqual("Miley Cyrus", self.room1.occupancy[0].name)

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
