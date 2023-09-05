import turtle
import time

wn = turtle.Screen()
wn.title("Pong by rewhare")
wn.bgcolor("black")
wn.setup(width = 800, height=600)
wn.tracer(0)

score_1 = 0
score_2 = 0

paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")  
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Arial", 26, "normal"))

def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)

wn.listen()
wn.onkeypress(paddle_1_up, "w")
wn.onkeypress(paddle_1_down, "s")
wn.onkeypress(paddle_2_up, "Up")
wn.onkeypress(paddle_2_down, "Down")

# Main Game Loop
while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290: 
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290: 
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390: 
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Arial", 26, "normal"))

    if ball.xcor() < -390: 
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Arial", 26, "normal"))

    # Paddle and Ball Rebound
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1

    if score_1 >= 11:
        pen.clear()
        pen.write("Player 1 Wins!", align="center", font=("Arial", 28, "normal"))
        wn.update()
        time.sleep(5)
        break
    elif score_2 >= 11:
        pen.clear()
        pen.write("Player 2 Wins!", align="center", font=("Arial", 28, "normal"))
        wn.update()
        time.sleep(5)
        break    



