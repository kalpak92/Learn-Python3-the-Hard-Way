# ex40: Modules, CLasses, and Objects

class Song(object):
    
    def __init__(self,lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

print("Happy Birthday Song -->")
happy_bday.sing_me_a_song()

print('-' * 10 )
print("Bulls on parade -->")
bulls_on_parade.sing_me_a_song()
