from manim import *
from manim.constants import *
import numpy as np


class ContinuousMotion(Scene):
    """
    No longer recognizable as the demo cribbed from manimce's home page.
    """
    def construct(self):
        func = lambda pos: np.sin(pos[1]) * RIGHT + np.cos(pos[0]) * UP
        vec_func = MathTex(
            r'f(x,y) = \begin{bmatrix}sin(x) + sin(y) \\sin(x) - sin(y) \end{bmatrix}'
        )
        self.add(vec_func)
        self.wait()

        self.play(FadeOut(vec_func))
        
        vector_field = ArrowVectorField(
            lambda x: (np.sin(x[0])+np.sin(x[1]), np.sin(x[0])-np.sin(x[1]))
        )
        self.play(FadeIn(vector_field))

        vector_field_2 = ArrowVectorField(
            lambda x: (np.sin(x[1])+np.sin(x[0]), np.sin(x[1])-np.sin(x[0]))
        )

        self.play(vector_field.animate.become(vector_field_2))
        self.wait()


class EstimatingAlternatingSums(Scene):
    def construct(self):
        pass
