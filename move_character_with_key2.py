from pico2d import *
import random





def handle_events():
    global running
    global dir
    global dir2

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            #elif event.key == SDLK_SPACE:
            elif event.key == SDLK_UP:
                dir2 += 1

            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1


open_canvas()
grass = load_image('grass.png')
character = load_image('402102.png')
left = load_image('left.png')
stop = load_image('stopright.png')
fire = load_image('fire.png')
background = load_image('background.png')
mushroom = load_image('mush10.png')

running = True
x = 800 // 2
y = 90
frame = 0
dir = 0 #  -1 left +1 right
dir2 = 0
dir3 = 0


#gitcommit

while running:
    clear_canvas()
    #grass.draw(400, 30)
    background.draw(400, 300 )

    #direction
    if dir == 1:
        mushroom.clip_draw(frame * 100, 0, 100, 100, x+200, 140)

    if dir == -1:
        mushroom.clip_draw(frame * 100, 0, 100, 100, x + 200, 140)

    if dir == 0:
        mushroom.clip_draw(0, 0, 100, 100, x+200, 140)


    if dir == 1:
        character.clip_draw(frame * 100, 0, 100, 100, x, 140)
    elif dir == -1:
        left.clip_draw(300 - frame * 100, 0, 100, 100, x, 140)

    elif dir == 0:
        character.clip_draw(0, 0, 100, 100, x, 140)

    elif dir2 == 1:
        character.clip_draw(frame * 100, 0, 100, 100, 400, y)
    elif dir3 == 1:
        fire

    update_canvas()

    handle_events()

    frame = (frame + 1) % 4
    x += dir * 5
    y += dir2 * 5
    delay(0.05)




close_canvas()

