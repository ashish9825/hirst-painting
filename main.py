# import colorgram
#
# colors = colorgram.extract('hirst.jpg', 30)
# print(colors)
#
# rgb_colors = []
#
# for color in colors:
#     color_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append(color_tuple)
#
# print(rgb_colors)
import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
screen = Screen()
screen.colormode(255)

color_list = [(140, 176, 207), (25, 32, 48), (26, 107, 159), (237, 225, 235), (209, 161, 111), (144, 29, 63),
              (230, 212, 93), (4, 163, 197), (218, 60, 84), (229, 79, 43), (195, 130, 169), (54, 168, 114),
              (28, 61, 116), (172, 53, 95), (108, 182, 90), (110, 99, 87), (193, 187, 46), (240, 204, 2), (1, 102, 119),
              (19, 22, 21), (50, 150, 109), (172, 212, 172), (118, 36, 34), (221, 173, 188), (227, 174, 166),
              (153, 205, 220), (184, 185, 210)]
tim.speed("fastest")

tim.penup()
y = -200
for i in range(10):
    tim.goto(-200, y)
    y += 50
    for _ in range(10):
        circle_color = random.choice(color_list)
        tim.pendown()
        tim.color(circle_color)
        tim.fillcolor(circle_color)
        tim.begin_fill()
        tim.circle(20)
        tim.end_fill()
        tim.penup()
        tim.forward(50)

screen.exitonclick()
