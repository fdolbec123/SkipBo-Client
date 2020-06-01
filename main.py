import pyglet

# Fin des imports

menu = pyglet.window.Window(1280, 720, resizable=False, caption="Bienvenue dans SkipBo!")
label = pyglet.text.Label("Hello World", font_name="Times New Roman", font_size=36, x=menu.width//2,
                          y=menu.height//2, anchor_x="center", anchor_y="center")


@menu.event
def on_draw():
    menu.clear()
    label.draw()


pyglet.app.run()
