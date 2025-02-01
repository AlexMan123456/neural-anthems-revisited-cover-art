from manim import *

# manim display-album-player.py -r 3000,3000 DisplayAlbumPlayer
class DisplayAlbumPlayer(Scene):
    def construct(self):
        filename = "play-album.js"
        code_window = VGroup(Code(code_file=filename, language="Javascript", background="window").scale(0.75).shift(2*UP))
        code_window.add(Text(filename, font_size=15, font="Arial").next_to(code_window, UP, buff=-0.25))

        code_window.shift(0.4*RIGHT+1.3*UP)

        
        terminal_text = self.set_terminal_text()
        terminal = VGroup(RoundedRectangle(0.1, color=WHITE).move_to(terminal_text).scale(2.9).shift(0.05*LEFT), terminal_text)
        terminal.add(Text("Terminal", font_size=20, font="Arial").next_to(terminal, UP, buff=-0.35))

        terminal.shift(0.3*RIGHT+UP)

        self.add(code_window, terminal)

    def set_terminal_text(self):
        font="Monospace"
        songs = ["A New Era by AlexGB231 ft. SOLARIA", "Rap Battle by AlexGB231 ft. Kevin, JUN, ASTERIAN, Ninezero, Ritchy", "Mechanical Constructions by AlexGB231 ft. Mai, SOLARIA", "The Pirate Who Wanted Treasure by AlexGB231 ft. Kevin", "Highest Power by AlexGB231 ft. Ninezero, JUN", "Dreams by AlexGB231 ft. ASTERIAN", "Aquatic Cavern by AlexGB231 ft. JUN", "This Big World by AlexGB231 ft. SOLARIA", "The End Of the Album Blues by AlexGB231 ft. SOLARIA, Kevin, Mai"]
        terminal_text = VGroup(Text("neural-anthems-revisited-cover-art", color=BLUE, font=font))
        terminal_text.add(Text("git:(", color=DARK_BLUE, font=font).next_to(terminal_text[0], RIGHT, buff=0.5))
        terminal_text.add(Text("main", color=RED, font=font).next_to(terminal_text[1], RIGHT))
        terminal_text.add(Text(")", color=DARK_BLUE, font=font).next_to(terminal_text[2], RIGHT))
        terminal_text.add(Text("✗", color=YELLOW, font=font).next_to(terminal_text[3], RIGHT, buff=0.5))
        terminal_text.add(Text("node play-album.js", font=font).next_to(terminal_text[4], RIGHT, buff=0.5))
        terminal_text.add(Text("Now playing Neural Anthems++ by AlexGB231", font=font).next_to(terminal_text[0], DOWN, aligned_edge=LEFT))
        terminal_text.add(Text("Songs to play:", font=font).next_to(terminal_text[6], DOWN, aligned_edge=LEFT).shift(DOWN))
        for i in range(len(songs)):
            text_index=i+7
            terminal_text.add(Text(songs[i], font=font).next_to(terminal_text[text_index], DOWN, aligned_edge=LEFT).shift(RIGHT if i == 0 else 0))
            
        terminal_text.shift(7.1*LEFT+1.8*UP).scale(0.4)

        return terminal_text



"""neural-anthems-revisited-cover-art git:(main) ✗ node play-album.js 
Now playing Neural Anthems++ by AlexGB231

Songs to play:
   A New Era by AlexGB231 ft. SOLARIA
   Rap Battle by AlexGB231 ft. Kevin, JUN, ASTERIAN, Ninezero, Ritchy
   Mechanical Constructions by AlexGB231 ft. Mai, SOLARIA
   The Pirate Who Wanted Treasure by AlexGB231 ft. Kevin
   Highest Power by AlexGB231 ft. Ninezero, JUN
   Dreams by AlexGB231 ft. ASTERIAN
   Aquatic Cavern by AlexGB231 ft. JUN
   This Big World by AlexGB231 ft. SOLARIA
   The End Of the Album Blues by AlexGB231 ft. SOLARIA, Kevin, Mai"""