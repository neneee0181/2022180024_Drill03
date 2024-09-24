from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# 여기를 채우세요.

status = 0
x = 0
while(True):
    while (x < 800):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 2
        delay(0.01)

close_canvas()
