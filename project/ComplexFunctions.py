import numpy as np
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
        surface = OpenGLSurface(
            lambda u, v: (u, v, u*np.sin(v) + v*np.cos((u))),
            u_range=(-3, 3),
            v_range=(-3, 3)
        )
        surface_mesh = OpenGLSurfaceMesh(surface)
        self.play(Create(surface_mesh))
        self.play(FadeTransform(surface_mesh, surface))
        self.wait()
        light = self.camera.light_source
        self.play(light.animate.shift([0, 0, -20]))
        self.play(light.animate.shift([0, 0, 10]))
        self.play(self.camera.animate.set_euler_angles(theta=60*DEGREES))
        self.interactive_embed()


class 