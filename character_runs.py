from pico2d import *

open_canvas()

grass = load_image('grass.png')
boy = load_image('run_animation.png')

def run_circle():
    print("CIRCLE")
    clear_canvas_now()
    boy.draw_now(400,300)
    delay(0.1)
    pass

def run_rectangle():
    print("RECTANGLE")
    pass

# fill here
while True:
    run_rectangle()
    run_circle()

close_canvas()

