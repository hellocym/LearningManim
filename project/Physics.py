from manim import *
from manim_physics import *


class RayExampleScene(Scene):
    def construct(self):
        lens_style = {"fill_opacity": 0.5, "color": BLUE}
        a = Lens(-5, 1, **lens_style).shift(LEFT*2)
        a2 = Lens(5, 1, **lens_style).shift(RIGHT)
        b = [
            Ray(LEFT * 5 + UP * i, RIGHT, 8, [a, a2], color=RED)
            for i in np.linspace(-2, 2, 10)
        ]
        self.add(a, a2, *b)
