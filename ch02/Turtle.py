import random
import turtle #파이썬에서 기본 제공되는 터틀 그래픽

#기능1. 마우스 왼쪽버튼->선을 그리며 거북이 따라가기
def screenLeftClick(x,y):
    global r,g,b
    tSize = random.randrange(1, 10)  # 1부터 9까지 임의의 정수로 거북이 크기 변경
    turtle.shapesize(tSize)
    r = random.random()  # 0~0.99999 중 임의의 실수로
    g = random.random()
    b = random.random()
    turtle.pencolor((r,g,b))
    turtle.pendown()
    turtle.goto(x,y)
#기능2. 마우스 오른쪽버튼->선없이 거북이 따라가기
def screenRightClick(x,y):
    turtle.penup()
    turtle.goto(x,y)

line= 10
r,g,b = 0.0,0.0,0.0

turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(line)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenRightClick,3)
turtle.done()