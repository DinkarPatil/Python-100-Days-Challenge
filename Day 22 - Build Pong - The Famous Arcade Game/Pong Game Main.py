# Building the Pong Game
# Step 1: Create a screen
# Step 2: Create and move a paddle
# Step 3: Create another paddle
# Step 4: Create the ball and make it move
# Step 5: Detect collision with wall and bounce
# Step 6: Detect collision with paddle
# Step 7: Detect when paddle misses
# Step 8: Keep the score


from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
scoreboard = Scoreboard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()

# Right paddle keys
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

# Left paddle keys
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect Right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_point()

    # Detect left paddle misses
    if ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.l_point()


screen.exitonclick()
