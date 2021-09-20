import turtle
from turtle import Screen
from player import Player
from block import Block
from ball import Ball
from score import Score
import time

#init screen
screen = Screen()
#screen setup
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0, 0)

#create player
player = Player((0, -265))
#create blocks
block = Block()
#create ball
ball = Ball()
#create score
score = Score()


#listen to screen clicks
screen.listen()
screen.onkey(player.go_left, 'a')
screen.onkey(player.go_right, 'd')

game_is_on = True
while game_is_on:
    time.sleep(0.02)
    screen.update()
    ball.move()

    #Detect the side border
    if ball.xcor() <= -380 or ball.xcor() >= 380:
        ball.bounce_x()
    #Detect top border
    if ball.ycor() >= 280:
        ball.bounce_y()
    #Reset Ball if paddle misses
    if ball.ycor() < -300:
        ball.reset_position()

    #Paddle detection
    if player.ycor() - 20 <= ball.ycor() <= player.ycor() + 20 and (player.xcor() - 20 < ball.xcor() < player.xcor() + 20):
        ball.bounce_y()


    #Detect Block Colision
    for blk in block.blocks:
        if blk.ycor() - 20 <= ball.ycor() <= blk.ycor() + 20 and (blk.xcor() - 20 < ball.xcor() < blk.xcor() + 20):
            blk.goto(500, 500)
            score.add_point()
            ball.bounce_y()
            block.blocks.remove(blk)

    if len(block.blocks) == 0:
        turtle.done()
        score.game_over()
        game_is_on = False



#exit app
screen.exitonclick()

