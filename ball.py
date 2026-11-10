from pico2d import get_canvas_width, load_image

import game_world

BALL_NONE = 0
BALL_SMALL = 1
BALL_LARGE = 2
ball_size = BALL_SMALL


def set_ball_size(size):
    global ball_size
    if size not in (BALL_NONE, BALL_SMALL, BALL_LARGE):
        raise ValueError('지원하지 않는 공 크기입니다.')
    ball_size = size


def get_ball_size():
    return ball_size


class Ball:
    images = {}

    def __init__(self, x, y, velocity):
        self.size = ball_size
        filename = 'ball21x21.png' if self.size == BALL_SMALL else 'ball41x41.png'
        if filename not in Ball.images:
            Ball.images[filename] = load_image(filename)
        self.image = Ball.images[filename]
        self.x, self.y = x, y
        self.velocity = velocity

    def update(self):
        self.x += self.velocity
        if self.x < 0 or self.x > get_canvas_width():
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
