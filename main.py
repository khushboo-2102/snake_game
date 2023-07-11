from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)                                     # using tracer method, animation gets off/stopped.

# create a Snake
snake = Snake()
food = Food()
# create a scoreboard
scoreboard = Scoreboard()


# Control the Snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Move a Snake
is_game_on = True
while is_game_on:
    screen.update()                                    # animation gets on.
    time.sleep(0.1)                                    # sleeps/delay for one second
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:      # food is 10 * 10 pixels and distance(both) is less than 15 pixels.
        food.refresh()
        snake.extend()
        scoreboard.increase_score()         # this method keeps record of score.

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    # Detect collision with tail  (if head is collide with any segment in the tail, trigger game over.)
    for segment in snake.segments[1:]:              # slicing (excluding 1st position from segments) (alternate method)
        # if segment == snake.head:
        #   pass
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()


screen.exitonclick()
