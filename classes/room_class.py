
#Setting up the class for Room

class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.occupancy = [ ]
        self.capacity = capacity
        self.song_list = [ ]

#Methods of the class Room:

#Adds a guest to the occupancy list of room instance. 
# (from room_test.py - self.room1.add_guest_to_room(self, guest))
    def add_guest_to_room(self, guest): 
        #check if occupancy is less than capacity before adding guest
        if len(self.occupancy) < self.capacity: 
            self.occupancy.append(guest)
            return True
        else:
            return False

#Removes a guest to the occupancy list
    def remove_guest_from_room(self, guest):
        self.occupancy.remove(guest)

    def add_song_to_song_list(self, song):
        self.song_list.append(song)

    def remove_song_from_song_list(self, song):
        self.song_list.remove(song)

#Extension work

# #Check if the room is full, return "Room full sorry"
#     def room_capacity_full(self, room):
#         if room.capacity == 20:
#             return "Room full, sorry"
#         #Further Work:
#         #Could create a new room to add the extra guests to.


    # def room_capacity_full(self, guest):
    #     if self.capacity == 0: #check if isn't full before adding guest
    #         self.room2 = Room("Room_2", 20)  #create a new instance of Room with capacity for 20 guests
    #         self.room2.add_guest_to_room(self, guest)
    #         print("Second room:", self.room2.capacity)
    #         return(self.room2.capacity)
    #     else:
    #         room.occupancy.append(guest)
    #         room.capacity -= 1
    #         print("First room:", room.capacity)
    #         return(self.room.capacity)
        