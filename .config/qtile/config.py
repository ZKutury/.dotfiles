# QTile Main Config File

from settings.keys import keys
from settings.groups import groups
from settings.layouts import layouts
from settings.mouse import mouse
from settings.screens import screens
from libqtile import hook
import subprocess, os


# Initial Script

@hook.subscribe.startup_once
def autostart():
    subprocess.run([os.path.expanduser("~/.config/qtile/settings/systray.sh")])


# Miscellaneous Configuration Variables

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"