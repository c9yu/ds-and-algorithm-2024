# date : 20240219
# file : ds26_fractalCircle.py
# desc : 프랙탈 원 그리기

from tkinter import *
import random

# def drawCircle(x, y, r):
#     global count
#     count += 1
#     canvas.create_oval(x-r, y-r, x+r, y+r, outline='red')
#     canvas.create_text(x, y-r, text= str(count), font = ('', 30))

#     if r >= radius/2:
#         drawCircle(x-r//2, y, r//2)
#         drawCircle(x+r//2, y, r//2)

def drawCircle(x, y, r):
    canvas.create_oval(x-r, y-r, x+r, y+r, width = 2, outline = random.choice(colors))
    if r>= 5:
        drawCircle(x-r/2, y, r//2)
        drawCircle(x+r/2, y, r//2)


# 전역변수
radius = 400
wSize = 1000
colors = ['red', 'green', 'blue', 'black', 'orange', 'indigo', 'violet', 'crimson']

# 메인코드
window = Tk()
window.title('프랙탈 그리기')
canvas = Canvas(window, height = 1000, width = 1000, bg = 'white')



cx = 1000/2
cy = 1000/2
r = 400

# cx-r, cy-r : (좌측 상단에서의 x, y) / cx+r, cy+r : (우측 하단에서의 x, y)

drawCircle(wSize//2, wSize//2, radius)

canvas.pack()
window.mainloop()

from tkinter import *

## 클래스와 함수 선언 부분 ##
def drawTriangle(x, y, size) :
    if size >= 30 :
        drawTriangle(x, y, size/2) # 왼쪽 아래 작은 삼각형
        drawTriangle(x+size/2, y, size/2) # 오른쪽 아래 작은 삼각형
        drawTriangle(x+size/4, int(y-size*(3**0.5)/4), size/2) # 위쪽 작은 삼각형
    else:
        canvas.create_polygon(x, y, x+size, y, x+size/2, y-size*(3**0.5)/2, fill='red', outline="red")

##전역 변수 선언 부분 ##
wSize = 1000
radius = 400

##메인 코드 부분 ##
window = Tk()
window.title("삼각형 모양의 프랙탈")
canvas = Canvas (window, height=wSize, width=wSize, bg='white')

drawTriangle(wSize/5, wSize/5*4, wSize*2/3)

canvas.pack()
window.mainloop ()