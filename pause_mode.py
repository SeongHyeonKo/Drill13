from pico2d import *
import game_framework
import game_world

pause_font = None


def init():
    global pause_font
    pause_font = load_font('C:/Windows/Fonts/arial.ttf', 32)


def finish():
    global pause_font
    pause_font = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    pause_font.draw(320, 340, 'PAUSED', (255, 255, 255))
    pause_font.draw(250, 295, 'Press P to resume', (255, 255, 255))
    update_canvas()
