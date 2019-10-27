import turtle
import time
from random import randint
import shapes
t = turtle

print("Welcome to Spirograph. Please keep both windows open")
choice = input("Choose a type of spirograph: circle, star, square, triangle or randomstar/circle/square/triangle ")

if choice == "star":
    forward = input("Give a number ")
    rt = input("Give another number ")
    colour = input("Give a colour ")
 
    while True:
        t.hideturtle()
        t.speed(100)
        t.color(str(colour))
        t.forward(int(forward))
        t.left(int(rt))

if choice == "circle":
        circle = input("Give a number ")
        rt = input("Give another number ")
        colour = input("Give a colour ")

        while True:
            t.hideturtle()
            t.speed(100)
            t.color(str(colour))
            t.circle(int(circle))
            t.left(int(rt))

if choice == "randomcircle":
    circle = randint(50, 200)
    rt = randint(1, 100)
    print(circle, rt)

    while True:
        for colours in ["red", "orange", "yellow", "green", "blue", "purple", "pink"]:
            t.bgcolor("black")
            t.hideturtle()
            t.speed(100)
            t.color(str(colours))
            t.circle(int(circle))
            t.left(int(rt))

if choice == "randomstar":   
    forward = randint(50, 200)
    rt = randint(10, 100)
    print(forward, rt)

    while True:
        for colours in ["red", "orange", "yellow", "green", "blue", "purple", "pink"]:
            t.bgcolor("black")
            t.hideturtle()
            t.speed(100)
            t.color(colours)
            t.forward(int(forward))
            t.left(int(rt))  

if choice == "square":
    size = input("Give me a number ")
    rotate = input("Give another number ")
    colour = input("Give a colour ")

    while True:
        t.speed(100)
        t.hideturtle()
        t.color(str(colour))
        shapes.square(int(size))
        t.left(int(rotate))

if choice == "randomsquare":
    size = randint(50, 200)
    rotate = randint(10, 100)
    print(size, rotate)

    while True:
        for colours in ["red", "orange", "yellow", "green", "blue", "purple", "pink"]:
            t.bgcolor("black")
            t.hideturtle()
            t.speed(100)
            t.color(colours)
            shapes.square(int(size))
            t.left(int(rotate))

if choice == "triangle":
    size = input("Give me a number ")
    rotate = input("Give another number ")
    colour = input("Give a colour ")

    while True:
        t.speed(100)
        t.hideturtle()
        t.color(str(colour))
        shapes.triangle(int(size))
        t.left(int(rotate))

if choice == "randomtriangle":
    size = randint(50, 200)
    rotate = randint(10, 100)
    print(size, rotate)

    while True:
        for colours in ["red", "orange", "yellow", "green", "blue", "purple", "pink"]:
            t.bgcolor("black")
            t.hideturtle()
            t.speed(100)
            t.color(colours)
            shapes.triangle(int(size))
            t.left(int(rotate))




    

