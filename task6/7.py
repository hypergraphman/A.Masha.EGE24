from turtle import *


def move(x, y):
    global cur_x, cur_y, cell
    cur_x += x
    cur_y += y
    goto(cur_x * cell, cur_y * cell)


speed(0)
cell = 30
cur_x, cur_y = 0, 0

move(10, 10)
move(3, -6)
move(-9, 3)

penup()
for x in range(0, 15 * cell, cell):
    for y in range(0, 15 * cell, cell):
        goto(x, y)
        dot(3)

done()