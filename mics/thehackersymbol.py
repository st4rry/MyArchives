#!/usr/bin/python
import turtle
from turtle import*

turtle.shape("square")
color("gray",[1]*3)
i=9
while i:
  i -= 1; turtle.goto(20-i/3*20, 20-i%3*20);stamp()
  if 302&2**i:dot(15,0,1,0)
turtle.exitonclick()
