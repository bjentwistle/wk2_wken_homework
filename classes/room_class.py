
#Setting up the class for Rooms

class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.occupancy = [ ]
        self.capacity = capacity
        self.song_list = [ ]

#Methods of the class Room:

    def add_guest_to_room(self, guest): 
        self.occupancy.append(guest)

    def remove_guest_from_room(self, guest):
        self.occupancy.remove(guest)

    def add_song_to_song_list(self, song):
        self.song_list.append(song)

    def remove_song_from_song_list(self, song):
        self.song_list.remove(song)



