from manim import *

# manim display-json.py -r 3000,3000 DisplayJSON
class DisplayJSON(Scene):
    def construct(self):
        filename = "neural-anthems.json"
        code_window = VGroup(Code(code_file=filename, language="Javascript", background="window", formatter_style="github-dark").scale(0.5))
        code_window.add(Text(filename, font_size=14, font="Arial").next_to(code_window, UP, buff=-0.25))

        code_window.scale(1.15).shift(0.5*RIGHT+0.2*DOWN)

        self.add(code_window)
