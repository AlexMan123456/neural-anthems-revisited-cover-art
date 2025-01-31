from manim import *

# manim display-album-player.py -r 3000,3000 DisplayAlbumPlayer
class DisplayAlbumPlayer(Scene):
    def construct(self):
        filename = "play-album.js"
        code_window = Code(code_file=filename, language="Javascript", background="window").scale(0.75)

        self.add(code_window)