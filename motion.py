from manimlib import *

class SquareToCircle(Scene):
    def construct(self):
        
        circle = Circle()
        circle.set_fill(BLUE, opacity= 10)
        circle.set_stroke(BLUE_E, width=  2)
        
        self.embed()
        