import unittest

from classes.song_class import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Holiday", "Madonna", "Pop", 4)
        self.song2 = Song("Paranoid", "Black Sabbath", "Heavy Metal", 7)
        self.song3 = Song("Flowers", "Miley Cyrus", "Pop", 3)

#2 tests here

    def test_can_create_song1(self):
        self.assertEqual("Heavy Metal", self.song2.genre)

    def test_can_create_song2(self):
        self.assertEqual("Madonna", self.song1.artist)

