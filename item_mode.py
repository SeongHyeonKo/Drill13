from pico2d import *
import game_framework
import play_mode
from ball import BALL_NONE, BALL_SMALL, BALL_LARGE, set_ball_size

item_select_image = None


def init():
    global item_select_image
    item_select_image = load_image('item_select.png')


def finish():
    global item_select_image
    item_select_image = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_0:
            set_ball_size(BALL_NONE)
            game_framework.change_mode(play_mode)


def update():
    pass


def render():
    clear_canvas()
    item_select_image.draw(400, 300)
    update_canvas()



