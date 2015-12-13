## was ex40.py

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self): 
		for line in self.lyrics:#indent works up to 1 
			print line #only need one indent

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

she_bop = Song(["She bop he bop and we bop",
				"I bop you bop and they bop"])


print "\n"
happy_bday.sing_me_a_song()
print "\n"

bulls_on_parade.sing_me_a_song()
print "\n"
she_bop.sing_me_a_song()
print "\n"