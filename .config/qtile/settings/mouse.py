# QTile Mouse Config File

from libqtile.config import Click, Drag
from libqtile.lazy import lazy
from settings.keys import mod


# Setting the mouse

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()), # Move floating window
    Click([mod], "Button2", lazy.window.bring_to_front()), # Bring to front the window
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()), # Resize floating window
]