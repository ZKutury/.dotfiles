# QTile Widgets Layout Config File

from settings.widgets import *

widget = [

    # OS Icon

    left_corner(2),
    logo("", 1, 2),
    #logo("", 1, 2, 37),
    right_corner(2),

    separator(),


    # Layouts and windows

    left_corner(2),
    window_counter(1,2),
    left_corner(3,2),
    current_layout(3),
    right_corner(3),

    separator(),


    # PC Stats

    left_corner(2),
    icon("", 1, 2, 30),
    cpu_percent(1, 2),
    left_corner(3, 2),
    icon("", 1, 3, 30),
    memory_usage(1,3),
    left_corner(4, 3),
    icon("", 1, 4, 30),
    available_space(1, 4),
    right_corner(4, 2),
    icon("", 1, 2, 30),
    unix_updates(1, 4, 2),
    right_corner(2),

    widget.Spacer(),


    # WorkSpaces
    left_corner(2),
    workspaces(5, 6, 1, 2),
    right_corner(2),

    separator(),
    widget.Spacer(),


    # Battery
    left_corner(4),
    #icon_battery(1, 3, 20, 4),
    battery(1, 1, 4),
    right_corner(4),

    separator(),


    # Wifi, Sound and Bright
    left_corner(4),
    icon("", 1, 4, 30),
    backlight(1, 4),
    right_corner(4, 3),
    icon("墳", 1, 3, 30),
    volume(1, 3),
    right_corner(3, 2),
    icon("", 1, 2, 30),
    wifi(1,2),
    right_corner(2),

    separator(),


    # Date Time

    left_corner(2),
    icon("", 1, 2, 30),
    clock(1, 2),
    right_corner(2)

]

widget_defaults = dict(
    font = "UbuntuMono Nerd Font",
    fontsize = 14,
    padding = 3
)
extension_defaults = widget_defaults.copy()
