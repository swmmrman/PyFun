#joke file
from turtle import *
from time import sleep

speed(10)
color('red', 'green')
bgcolor('black')
begin_fill()
b = 200
while b > 0:
    left(b)
    forward(b * 3)
    b = b - 1
end_fill()
sleep(10)
