from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

r, cx, cy = 210, 800 // 2, 600 // 2


def draw_boy(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    boy.draw_now(x, y)
    delay(0.1)
    pass


def run_circle():
    print("CIRCLE")

    for degree in range(0, 360, 3):
        theta = math.radians(degree)
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy
        draw_boy(x, y)

    pass


def run_top():
    print("TOP")
    for x in range(0, 800, 10):
        draw_boy(x, 550)
    pass


def run_right():
    for y in range(550, 90, -10):
        draw_boy(790, y)
    print("RIGHT")
    pass


def run_bottom():
    print("BOTTOM")
    for x in range(800, 0, -10):
        draw_boy(x, 90)
    pass


def run_left():
    print("LEFT")
    for y in range(90, 550, 10):
        draw_boy(0, y)
    pass


def run_rectangle():
    print("RECTANGLE")
    run_top()
    run_right()
    run_bottom()
    run_left()
    pass


def run_left_line():
    print("left_line")
    for x, y in zip(range(cx, cx - 300, -10), range(cy + 100, cy - 200, -10)):
        draw_boy(x, y)
    pass


def run_right_line():
    print("right_line")
    for x, y in zip(range(cx + 300, cx, -10), range(cy - 200, cy + 100, 10)):
        draw_boy(x, y)
    pass


def run_bottom_line():
    print("bottom_line")
    for x in range(cx - 300, cx + 300, 10):
        draw_boy(x, cy - 200)
    pass


def run_triangle():
    print("TRIANGLE")
    run_left_line()
    run_bottom_line()
    run_right_line()
    pass


# fill here
while True:
    run_circle()
    run_rectangle()
    run_triangle()

close_canvas()
