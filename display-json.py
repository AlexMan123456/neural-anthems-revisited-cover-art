from manim import *

# manim display-json.py -r 3000,3000 DisplayJSON
class DisplayJSON(Scene):
    def construct(self):
        filename = "neural-anthems.json"
        code_window = Code(code_file=filename, language="Javascript", background="window").scale(0.5)
        window_header = Text(filename, font_size=14).next_to(code_window, UP, buff=-0.25)
        self.add_foreground_mobject(window_header)

        self.add(window_header, code_window)
