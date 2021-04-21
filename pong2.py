import turtle
#import winsound

wn=turtle.Screen()
wn.title("pong by SAKSHI")
wn.bgcolor("white")
wn.setup(width=800,height=600)
wn.tracer(0)

#Score
score_a=0
score_b=0


# paddle A
paddle_a=turtle.Turtle()  # small T is module name capital T is a class name
paddle_a.speed(0) # this is not the speed for paddle moves on the screen... it is the speed for animation maximum speed otherwise it will b very slow
paddle_a.color("black")
paddle_a.shape("square")
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b=turtle.Turtle()  # small T is module name capital T is a class name
paddle_b.speed(0) # this is not the speed for paddle moves on the screen... it is the speed for animation maximum speed otherwise it will b very slow
paddle_b.color("black")
paddle_b.shape("square")
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.penup()
paddle_b.goto(350, 0)
# ball
ball=turtle.Turtle()
ball.speed(0)
ball.color("green")
ball.shape("circle")
ball.penup()
ball.goto(0, 0)
ball.dx=1            # everytimes the ball moves it moves diagonally by 2 pixels right 2
ball.dy=-1            # everytimes the ball moves it moves diagonally by 2 pixels up 2

# Pen(turtle module)
pen = turtle.Turtle()
pen.speed(0)           #animation speed not the movement spped
pen.color("purple")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player A: 0    Player B: 0",align="center",font=("courier",24,"normal"))


#Function
def paddle_a_up():
    y=paddle_a.ycor()    # for reseting it to the y coordinate
    y+=20                # set 20 px to the y
    paddle_a.sety(y)      # calculate a y to set a new y
def paddle_a_down():
    y=paddle_a.ycor()    # for reseting it to the y coordinate
    y-=20                # set 20 px to the y
    paddle_a.sety(y)

def paddle_b_up():
        y = paddle_b.ycor()  # for reseting it to the y coordinate
        y += 20  # set 20 px to the y
        paddle_b.sety(y)  # calculate a y to set a new y

def paddle_b_down():
        y = paddle_b.ycor()  # for reseting it to the y coordinate
        y -= 20  # set 20 px to the y
        paddle_b.sety(y)
#keyboard binding
wn.listen()              # listen to the keyboard input
wn.onkeypress(paddle_a_up,"a") # this tell when the keyboard gets a key preesed w(only smaller not capital) it will go up
wn.onkeypress(paddle_a_down,"z")

wn.onkeypress(paddle_b_up,"k") # this tell when the keyboard gets a key preesed w(only smaller not capital) it will go up
wn.onkeypress(paddle_b_down,"m")
while True:
    wn.update()
    #Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # Border checking
    # comapare the y cordinate to bounce
    # this for the top n bottom border
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
        ######os.system("bounce.wav")
        #winsound.PlaySound("boom.wav",winsound.SND_ASYNC_)


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-1
        #winsound.PlaySound("boom.wav", winsound.SND_ASYNC_)

    # for right n left border
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("player A: {}    Player B: 0{}".format(score_a,score_b), align="center", font=("courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=1
        pen.clear()  #so the score may not overwrite each other
        pen.write("player A: {}    Player B: 0{}".format(score_a, score_a), align="center",
                  font=("courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor()> 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() +40 and ball.ycor() >paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        #winsound.PlaySound("boom.wav",winsound.SND_ASYNC_)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() +40 and ball.ycor() >paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        #winsound.PlaySound("boom.wav", winsound.SND_ASYNC_)

