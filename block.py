from turtle import Turtle
import random

COLORS = ["red", "orange", "grey", "green", "blue", "purple"]
Xs = [240, 200, 160, 120, 80, 40, 00, -40, -80, -120, -160, -200, -240]
Ys = [250, 230, 210, 190, 170, 150]

class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.blocks = []
        for x in Xs:
            for y in Ys:
                self.create_block(x, y)



    def create_block(self, xpos, ypos):
        new_block = Turtle('square')
        new_block.color(random.choice(COLORS))
        new_block.up()
        new_block.shapesize(stretch_wid=0.8, stretch_len=1.7)
        new_block.goto(xpos, ypos)
        self.blocks.append(new_block)

