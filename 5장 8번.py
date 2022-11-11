Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Turtle()
>>> t.shape("turtle")
>>> 
>>> x1 = int(input("큰 원의 중심좌표 x1: "))
큰 원의 중심좌표 x1: 0
>>> >>> 
>>> y1 = int(input("큰 원의 중심좌표 y1: "))
SyntaxError: invalid syntax
>>> y1 = int(input("큰 원의 중심좌표 y1: "))
큰 원의 중심좌표 y1: 0
>>> 
KeyboardInterrupt
>>> r1 = int(input("큰 원의 반지름: "))
큰 원의 반지름: 100
>>> x2 = int(input("작은 원의 중심좌표 x2: "))
작은 원의 중심좌표 x2: 10
>>> y2 = int(input("작은 원의 중심좌표 y2: "))
작은 원의 중심좌표 y2: 10
>>> r2 = int(input("작은 원의 반지름: "))
작은 원의 반지름: 50
>>> 
>>> t.penup()
>>> t.goto(x1,y1)
>>> t.pendown()
>>> t,circle(r1)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    t,circle(r1)
NameError: name 'circle' is not defined
>>> t.circle(r1)
>>> 
>>> t.penup()
>>> t.goto(x2,y2)
>>> t.pendown()
>>> t.circle(r2)
>>> 
>>> dist = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
>>> if dist <= r1-r2:
	turtle.write("두번째 원이 첫번째 원의 내부에 있습니다.")
elif dist <= r1+r2:
	turtle.write("두번째 원이 첫번째 원과 겹칩니다. ")
else:
	turtle.write("두번쨰 원이 첫번쨰 원과 겹치지 않습니다.")
t._screen.exitonclick()
