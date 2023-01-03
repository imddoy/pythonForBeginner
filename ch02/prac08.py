import random
import turtle

def screenLeftClick(x,y):
    global r,g,b
    tSize = random.randrange(1, 10)  # 1부터 9까지 임의의 정수로 거북이 크기 변경
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.color((r,g,b))
    turtle.penup()
    turtle.speed(0)
    turtle.setheading(random.randrange(0,360))
    turtle.goto(x, y)
    turtle.stamp()

r,g,b = 0.0,0.0,0.0

turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')

turtle.onscreenclick(screenLeftClick, 1)
turtle.done()