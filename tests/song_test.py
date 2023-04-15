import unittest

from classes.song_class import *

class TestSong(unittest.TestCase):
#Test 5
    def test_can_create_song2(self):
        self.song2 = Song("Paranoid", "Black Sabbath", "Heavy Metal", 7)
        self.assertEqual("Heavy Metal", self.song2.genre)
        #print(self.song2.genre)

    def test_can_create_song1(self):
        self.song1 = Song("Holiday", "Madonna", "Pop", 4)
        self.assertEqual("Madonna", self.song1.artist)
        #print(self.song1.artist)
