from manim import *
from manim.opengl import *
from moderngl.program_members import Attribute


class OpenGLIntro(Scene):
    def construct(self):
        tex = Tex("Hello World!").scale(3)
        self.play(Write(tex))
        for t, p in [(10, 50), (-10, -50), (30, -75), (-30, 75)]:
            self.play(
                self.camera.animate.set_euler_angles(
                    theta=t*DEGREES,
                    phi=p*DEGREES
                ), run_time=0.3
            )

        self.play(FadeOut(tex))