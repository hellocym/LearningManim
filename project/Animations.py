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


class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end:float, **kwargs) -> None:
        super().__init__(number, **kwargs)
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)


class CountingScene(Scene):
    def construct(self):
        number = DecimalNumber().set_color(WHITE).scale(5)
        number.add_updater(lambda number: number.move_to(ORIGIN))

        self.add(number)

        self.wait()

        self.play(Count(number, 0, 100), run_time=4, rate_func=linear)

        self.wait()

