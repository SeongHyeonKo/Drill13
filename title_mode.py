from pico2d import *
import game_framework
import item_mode

title_image = None


def init():
    global title_image
    title_image = load_image('title.png')


def finish():
    global title_image
    title_image = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(item_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def update():
    pass


def render():
    clear_canvas()
    title_image.draw(400, 300)
    update_canvas()

