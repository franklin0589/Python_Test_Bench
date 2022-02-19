import pyglet

window = pyglet.window.Window()
# label = pyglet.text.Label('Hello, world',
#                           font_name='Times New Roman',
#                           font_size=36,
#                           x=window.width//2, y=window.height//2,
#                           anchor_x='center', anchor_y='center')
# @window.event
# def on_draw():
#     window.clear()
#     label.draw()
# pyglet.app.run()

# @window.event
# def on_key_press(symbol, modifiers):
#     print('A key was pressed')

from pyglet.window import key
from pyglet import shapes
music = pyglet.resource.media('50 Cent - In Da Club (Clean).ogg')
circle = shapes.Circle(x=100, y=150, radius=100, color=(50, 225, 30))
circle.anchor_position = 50, 25
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
        music.play()
        print('The enter key was pressed.')

@window.event
def on_draw():
    window.clear()
    circle.draw()
   

pyglet.app.run()
