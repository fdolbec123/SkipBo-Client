#!/usr/bin/env python3

import glooey
import autoprop

# Import everything from glooey into this namespace.  We'll overwrite the 
# widgets we want to overwrite and everything else will be directly available.
from glooey import *

assets = glooey.themes.ResourceLoader('wesnoth')
assets.add_font('fonts/Lato-Regular.ttf')
assets.add_font('fonts/Lato-Bold.ttf')
assets.add_font('fonts/Lato-Italic.ttf')
assets.add_font('fonts/Lato-LightItalic.ttf')
assets.add_font('fonts/Lato-Light.ttf')

# Missing widgets:
# - Slider
# - Dropdown

@autoprop
class Gui(glooey.Gui):
    custom_cursor = 'normal'
    custom_cursor_style = 'bw'
        
    def __init__(self, window, *, batch=None, cursor=None, cursor_style=None):
        super().__init__(window, batch=batch)
        self._cursor = cursor or self.custom_cursor
        self._cursor_style = cursor_style or self.custom_cursor_style
        self._update_cursor()

    def get_cursor(self):
        return self._cursor

    def set_cursor(self, cursor):
        """
        Specify which cursor to use.

        There are a number of different cursor to choose from (not all of which 
        will be relevant to every application):

        - ``"normal"``
        - ``"wait"``
        - ``"select"``
        - ``"select_illegal"``
        - ``"select_location"``
        - ``"move"``
        - ``"move_drag"``
        - ``"attack"``
        - ``"attack_drag"``
        - ``"no_cursor"``
        """
        self._cursor = cursor
        self._update_cursor()

    def get_cursor_style(self):
        return self._cursor_style

    def set_cursor_style(self, style):
        """
        Set the style of the cursor.

        There are two possible styles:

        - ``"bw"``: Simple black-and-white cursors.
        - ``"color"``: More elaborate color cursors.
        """
        self._cursor_style = style
        self._update_cursor()

    def _update_cursor(self):
        cursor = self._cursor
        style = self._cursor_style
        key = f'{cursor}_{style}'

        try:
            super().set_cursor(
                    assets.image(f'cursors/{key}.png'),
                    assets.yaml(f'cursors/hotspots.yml')[key],
            )
        except pyglet.resource.ResourceNotFoundException:
            raise UsageError(f"The Wesnoth theme doesn't have a cursor named '{cursor}' in the '{style}' style.")

class Label(glooey.Label):
    custom_color = '#b9ad86'
    custom_font_name = 'Lato Regular'
    custom_font_size = 10

class BaseButton(glooey.Button):
    Background = glooey.Image

    class Label(Label):
        custom_alignment = 'center'

class Button(BaseButton):
    custom_base_image = assets.image('buttons/basic/normal.png')
    custom_over_image = assets.image('buttons/basic/normal_active.png')
    custom_down_image = assets.image('buttons/basic/normal_pressed.png')

class SmallButton(BaseButton):
    custom_base_image = assets.image('buttons/basic/small.png')
    custom_over_image = assets.image('buttons/basic/small_active.png')
    custom_down_image = assets.image('buttons/basic/small_pressed.png')

class BackgroundButton(BaseButton):
    custom_base_image = assets.image('buttons/basic/background.png')
    custom_over_image = assets.image('buttons/basic/background_active.png')
    custom_down_image = assets.image('buttons/basic/background_pressed.png')

class SquareButton(BaseButton):
    custom_base_image = assets.image('buttons/basic/square_25.png')
    custom_over_image = assets.image('buttons/basic/square_25_active.png')
    custom_down_image = assets.image('buttons/basic/square_25_pressed.png')

class BigSquareButton(BaseButton):
    custom_base_image = assets.image('buttons/basic/square_30.png')
    custom_over_image = assets.image('buttons/basic/square_30_active.png')
    custom_down_image = assets.image('buttons/basic/square_30_pressed.png')

class BiggerSquareButton(BaseButton):
    custom_base_image = assets.image('buttons/basic/square_60.png')
    custom_over_image = assets.image('buttons/basic/square_60_active.png')
    custom_down_image = assets.image('buttons/basic/square_60_pressed.png')

class MenuButton(BaseButton):
    custom_base_image = assets.image('buttons/menu/normal.png')
    custom_over_image = assets.image('buttons/menu/normal_active.png')
    custom_down_image = assets.image('buttons/menu/normal_pressed.png')

class SmallMenuButton(BaseButton):
    custom_base_image = assets.image('buttons/menu/small.png')
    custom_over_image = assets.image('buttons/menu/small_active.png')
    custom_down_image = assets.image('buttons/menu/small_pressed.png')

class BlankMenuButton(BaseButton):
    custom_base_image = assets.image('buttons/menu/blank.png')
    custom_over_image = assets.image('buttons/menu/blank_active.png')
    custom_down_image = assets.image('buttons/menu/blank_pressed.png')

class Checkbox(glooey.Checkbox):
    custom_unchecked_base = assets.image('buttons/toggles/checkbox.png')
    custom_unchecked_over = assets.image('buttons/toggles/checkbox_active.png')
    custom_unchecked_down = assets.image('buttons/toggles/checkbox_touched.png')
    custom_checked_base = assets.image('buttons/toggles/checkbox_pressed.png')
    custom_checked_over = assets.image('buttons/toggles/checkbox_active_pressed.png')

class RadioButton(glooey.RadioButton):
    custom_unchecked_base = assets.image('buttons/toggles/radiobox.png')
    custom_unchecked_over = assets.image('buttons/toggles/radiobox_active.png')
    custom_unchecked_down = assets.image('buttons/toggles/radiobox_touched.png')
    custom_checked_base = assets.image('buttons/toggles/radiobox_pressed.png')
    custom_checked_over = assets.image('buttons/toggles/radiobox_active_pressed.png')

class CollapseButton(glooey.Checkbox):
    custom_unchecked_base = assets.image('buttons/toggles/fold_arrow.png')
    custom_unchecked_over = assets.image('buttons/toggles/fold_arrow_active.png')
    custom_unchecked_down = assets.image('buttons/toggles/fold_arrow_pressed.png')
    custom_checked_base = assets.image('buttons/toggles/unfold_arrow.png')
    custom_checked_over = assets.image('buttons/toggles/unfold_arrow_active.png')
    custom_checked_down = assets.image('buttons/toggles/unfold_arrow_pressed.png')



class VScrollBox(glooey.ScrollBox):

    class Frame(glooey.Frame):

        class Box(glooey.Bin):
            custom_horz_padding = 5

        class Decoration(glooey.Background):
            custom_center = assets.texture('dialogs/translucent54_background.png')

    class VBar(glooey.VScrollBar):
        custom_scale_grip = True

        class Decoration(glooey.Background):
            custom_center = assets.texture('dialogs/translucent54_background.png')

        class Grip(glooey.Button):
            custom_base_top = assets.image('buttons/scrollbar/top.png')
            custom_base_center = assets.texture('buttons/scrollbar/mid.png')
            custom_base_bottom = assets.image('buttons/scrollbar/bottom.png')

            custom_over_top = assets.image('buttons/scrollbar/top_active.png')
            custom_over_center = assets.texture('buttons/scrollbar/mid_active.png')
            custom_over_bottom = assets.image('buttons/scrollbar/bottom_active.png')

            custom_down_top = assets.image('buttons/scrollbar/top_pressed.png')
            custom_down_center = assets.texture('buttons/scrollbar/mid_pressed.png')
            custom_down_bottom = assets.image('buttons/scrollbar/bottom_pressed.png')

            custom_alignment = 'fill'

class HScrollBox(glooey.ScrollBox):

    class Frame(glooey.Frame):

        class Box(glooey.Bin):
            custom_vert_padding = 5

        class Decoration(glooey.Background):
            custom_center = assets.texture('dialogs/translucent54_background.png')

    class HBar(glooey.HScrollBar):
        custom_scale_grip = True

        class Decoration(glooey.Background):
            custom_center = assets.texture('dialogs/translucent54_background.png')

        class Grip(glooey.Button):
            custom_base_left = assets.image('buttons/scrollbar/left.png')
            custom_base_center = assets.texture('buttons/scrollbar/horizontal.png')
            custom_base_right = assets.image('buttons/scrollbar/right.png')

            custom_over_left = assets.image('buttons/scrollbar/left_active.png')
            custom_over_center = assets.texture('buttons/scrollbar/horizontal_active.png')
            custom_over_right = assets.image('buttons/scrollbar/right_active.png')

            custom_down_left = assets.image('buttons/scrollbar/left_pressed.png')
            custom_down_center = assets.texture('buttons/scrollbar/horizontal_pressed.png')
            custom_down_right = assets.image('buttons/scrollbar/right_pressed.png')

            custom_alignment = 'fill'


# I'm not sure exactly how these two are supposed to be used...
class HighlightFrame(glooey.Frame):

    class Decoration(glooey.Image):
        custom_image = assets.image('dialogs/selection.png')

class BrightHighlightFrame(glooey.Frame):

    class Decoration(glooey.Image):
        custom_image = assets.image('dialogs/selection2.png')

class SelectableButton:
    pass

class BraidedFrame:
    pass

class GildedFrame:
    pass

