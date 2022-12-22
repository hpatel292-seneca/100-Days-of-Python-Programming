# from turtle import Screen
# from food import Food
# import time
# from snake import Snake
# from scoreboard import ScoreBoard
# screen = Screen()
# screen.title("The Snake Game")
# screen.bgcolor("black")
# screen.tracer(0)
# screen.listen()
#
# snake = Snake()
# food = Food()
# scoreboard = ScoreBoard()
#
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")
# screen.update()
# game_is_on = True
# sleep_time = 0.1
# while game_is_on:
#     screen.update()
#     time.sleep(sleep_time)
#
#     snake.move()
#     if snake.head.distance(food) <= 25:
#         food.refresh()
#         scoreboard.point()
#         snake.add()
#         sleep_time -= 0.005
#
#     if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 320 or snake.head.ycor() < -320:
#         game_is_on = False
#
#         print(screen.canvheight)
#
#     if not snake.check():
#         game_is_on = False
#         scoreboard.game_over()
#
#
#
#
# screen.exitonclick()
a = [1, 2, 3]

if type(a) == list:
    print("hello")