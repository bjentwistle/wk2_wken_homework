
#Setting up the class for Room

class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.occupancy = [ ]
        self.capacity = capacity
        self.song_list = [ ]
        self.fee = 15           #extension work

#Methods of the class Room:

#Adds a guest to the occupancy list of room instance. 
# (from room_test.py - self.room1.add_guest_to_room(self, guest))
    def add_guest_to_room(self, guest): 
        #extension work - check if occupancy is less than capacity before adding guest
        if len(self.occupancy) < self.capacity: 
            self.occupancy.append(guest)
            return True
        else:
            return False

#Removes a guest to the occupancy list of room instance
#(from room_test.py - self.room1.remove_guest_from_room(self.guest1) )
    def remove_guest_from_room(self, guest):
        self.occupancy.remove(guest)

#Adds a song to the song list in room instance
    def add_song_to_song_list(self, song):
        self.song_list.append(song)

#Removes a song to the song list in room instance
    def remove_song_from_song_list(self, song):
        self.song_list.remove(song)

#Checks if guest's fav song is in the song list.
    def is_fav_song_in_list(self, guest):
        for i in range(len(self.song_list)):
            if self.song_list[i].name == guest.fav_song:
                print("Woohoo!")
                return True
            else:
                print("Boo!")
                return False