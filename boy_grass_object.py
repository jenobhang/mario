from pico2d import *

# Game object class here

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.image = load_image('402102.png')
        self.x, self.y = 400, 90
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 4
        self.x += dir * 10
        self.y += dir2 * 10

    def jump(self):
        if self. y < 10:
            self.y -= 100




    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)




def handle_events():
    global running
    global dir
    global dir2
    events = get_events()
    for event in events:

        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_UP:
                dir2 += 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                dir2 -= 1

        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code


open_canvas()


grass = Grass()    #잔디 생성
boy = Boy()

running = True

dir = 0 #  -1 left +1 right
dir2 = 0



# game main loop code
while running:

    handle_events()
    boy.update()
    #game logic


    #game drawing
    clear_canvas()
    grass.draw()
    boy.draw()



    update_canvas()


    delay(0.05)

close_canvas()
# finalization code