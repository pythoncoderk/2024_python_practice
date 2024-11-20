class Singer:
    def __init__(self, song, singer):
        self.song = song
        self.singer = singer

    def ans(self):
        return self.song + "/" + self.singer

song = input()
singer = input()
sing = Singer(song, singer)
print(sing.ans())