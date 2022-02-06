# QTile Screens Config File

from libqtile.config import Screen
from libqtile import bar
from settings.widget import widget


# Set up the Main Screen

screens = [Screen(top=bar.Bar(widget, 24, background="#00000000", margin=[5,5,5,5]))] # Insert Widgets in the Top Bar