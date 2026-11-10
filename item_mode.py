from pico2d import load_image

item_select_image = None


def init():
    global item_select_image
    item_select_image = load_image('item_select.png')


def finish():
    global item_select_image
    item_select_image = None


def handle_events():
    pass


def update():
    pass


def render():
    from pico2d import clear_canvas, update_canvas
    clear_canvas()
    item_select_image.draw(400, 300)
    update_canvas()
