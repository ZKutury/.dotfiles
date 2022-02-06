# QTile WorkSpaces Config

from libqtile.config import Group, Match, Key
from libqtile.command import lazy
from settings.keys import keys, mod


# Setting the groups

groups = [
    Group("", layout="max"), # Navegator Group
    Group("", spawn="alacritty", layout="monadtall"), # Terminals Group
    Group("", layout="max"), # Development Group
    Group("", spawn="spotify", layout="max"), # Music Player Group
    Group("", layout="max"), # Text Chat App Group
    Group("", layout="monadtall"), # File Explorer Group
    Group("", spawn="alacritty --config-file /home/kutu/.config/alacritty/transparent.yml -e cava", layout="max"), # Cava and fun stuff
    Group("", layout="monadtall"), # Miscellaneous Group
]


for i, group in enumerate(groups):
    keys.extend([
        Key([mod], str(i+1), lazy.group[group.name].toscreen()),
        Key([mod, "shift"], str(i+1), lazy.window.togroup(group.name))
    ])