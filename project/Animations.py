from manim import *


class SomeAnimations(Scene):
    def construct(self):
        square = Square()

        self.play(FadeIn(square))

        self.play(Rotate(square, PI/4))

        self.play(FadeOut(square))

        self.wait(1)


class AnimateExample(Scene):
    def construct(self):
        square = Square().set_fill(RED, opacity=1.0)
        self.add(square)

        self.play(square.animate.set_fill(WHITE))
        self.wait(1)

        self.play(square.animate.shift(UP).rotate(PI / 3))
        self.wait(1)


class Runtime(Scene):
    def construct(self):
        square = Square()
        self.add(square)
        self.play(square.animate.shift(UP), run_time=3)
        self.wait(1)