#Setting up the class for Guest

class Guest:
    def __init__(self, name, age, fav_song, wallet):
        self.name = name
        self.age = age
        self.fav_song = fav_song
        self.wallet = wallet        #extension work

#Extension work

#Add a method to reduce wallet
    def reduce_wallet(self, room_fee):
        if self.wallet >= room_fee:
            self.wallet -= room_fee
            return True
        else:
            return False