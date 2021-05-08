import turtle
import time
screen = turtle.Screen()
screen.bgcolor('green')
screen.title('Pong game')
screen.setup(800,600)


paddle_a= turtle.Turtle()
paddle_a.shape('square')
paddle_a.shapesize(5,1)
paddle_a.speed(0)
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(-350,0)

paddle_b= turtle.Turtle()
paddle_b.shape('square')
paddle_b.shapesize(5,1)
paddle_b.speed(0)
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350,0)

ball = turtle.Turtle()
ball.shape('circle')
ball.speed(0)
ball.color('white')

def paddle_a_up():
    y = paddle_a.ycor()
    y=y+10
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y=y-10
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y=y+10
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y=y-10
    paddle_b.sety(y)

screen.listen()
screen.onkeypress(paddle_a_up,'q')
screen.onkeypress(paddle_a_down,'a')
screen.onkeypress(paddle_b_up,'Up')
screen.onkeypress(paddle_b_down,'Down')


score1=0
score2=0

score = turtle.Turtle()
score.speed(0)
score.color('red')
score.penup()
score.hideturtle()
score.goto(0,260)
score.write(' player1: 0        player2: 0',align = 'center', font=('aerial',30,'bold'))


ball.speedx=4
ball.speedy=4
ball.penup()

def display1():
    score3 = turtle.Turtle()
    score3.speed(0)
    score3.color('red')
    score3.penup()
    score3.hideturtle()
    score3.goto(0,0)
    score3.write(' player 1 has won', align='center', font=('aerial', 30, 'bold'))
def display2():
    score4 = turtle.Turtle()
    score4.speed(0)
    score4.color('red')
    score4.penup()
    score4.hideturtle()
    score4.goto(0,0)
    score4.write(' player 1 has won', align='center', font=('aerial', 30, 'bold'))
while True:
    screen.update()
    ball.setx(ball.xcor()+ball.speedx)
    ball.sety(ball.ycor()+ball.speedy)
    if ball.xcor()>390 :
        ball.goto(0,0)
        ball.speedx*=-1
        score1+=1
        score.clear()
        score.write('player1: {}        player2:{}'.format(score1,score2),align='center',font=('aerial',30,'bold'))
    elif ball.xcor()<-390 :
        ball.goto(0,0)
        ball.speedx*=-1
        score2+=1
        score.clear()
        score.write('player1: {}        player2: {}'.format(score1,score2),align='center',font=('aerial',30,'bold'))

    elif ball.ycor() > 290 or ball.ycor()<-290:
        ball.speedy*=-1
    if (ball.xcor()>330 and ball.xcor()<350) and ((ball.ycor()<paddle_b.ycor()+50) and (ball.ycor()>paddle_b.ycor()-50)):
        ball.speedx*=-1
    elif(ball.xcor()<-330 and ball.xcor()>-350) and ((ball.ycor()<paddle_a.ycor()+50) and (ball.ycor()>paddle_a.ycor()-50)):
        ball.speedx*=-1
    if score1==10:
        score.clear()
        display1()
        ball.hideturtle()
        time.sleep(3)
        turtle.Screen().bye()

    elif score2==10:
        score.clear()
        display2()
        ball.hideturtle()
        time.sleep(3)
        turtle.Screen().bye()



