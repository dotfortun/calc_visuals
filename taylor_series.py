from manim import *
from manim.constants import *
import numpy as np


class TaylorSeries(Scene):
    def construct(self):
        f = MathTex(
            r'f(x) = \sqrt[{3}]{x}'
        )
        f.to_corner(UL)
        self.add(f)

        plane = NumberPlane((-1, 10), (-1,3))
        plane.set_z_index(-1000)
        plane.add_coordinates()

        f_plot = plane.plot(
            lambda x: x**(1/3),
            x_range=[0, 10]
        )

        p_2 = MathTex(
            r'P_2(x) = 2+\frac{\left(x-8\right)}{12}\,-\frac{\left(x-8\right)^{2}}{288}',
            color=BLUE
        )
        p_2.to_corner(UR)
        self.add(p_2)

        p_2_plot = plane.plot(
            lambda x: 2+(x-8)/12-((x-8)**2)/288,
            x_range=[0, 10],
            color=BLUE

        )

        self.add(plane)
        self.add(f_plot)
        self.add(p_2_plot)

        self.wait()

        for degree in range(10):
            pass
