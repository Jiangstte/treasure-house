class Song(object):

    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

yuyanjia = ("happy berthday to you",
            "i don't wang to get sued",
            "so i'll stop right there")

bulls_on_parade = Song(["they rally around the family",
                        "with pockets full of shells"])


yuyanjia.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

