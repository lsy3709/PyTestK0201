import turtle
import random

## 함수 선언 부분 ##
def  screenLeftClick(x, y):
    global r, g, b
    tSize = random.randrange(1, 10)
    pSize = random.randrange(1, 10)
    rAngle = random.randrange(1, 360)
    turtle.shapesize(tSize)
    turtle.resizemode("auto")
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pensize(pSize)
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.right(rAngle)
    turtle.stamp()
    turtle.goto(x, y)

def  screenRightClick(x, y):
    turtle.penup()
    turtle.goto(x, y)

def  screenMidClick(x, y):
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()

## 변수 선언 부분 ##
pSize = 10
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
screen = turtle.Screen()
image1 = "C:/Users/user1/OneDrive/문서/PyTestWork/ch02/라바1.gif"
# screen.addshape(image1)
screen.register_shape(image1)
turtle.title('거북이로 그림 그리기')
turtle.shape(image1)
# turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
