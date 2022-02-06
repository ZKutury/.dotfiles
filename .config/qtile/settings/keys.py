# QTile Keys ShortCuts Config

from libqtile.config import Key
from libqtile.command import lazy

mod = "mod4" # Main Modifier Key

# Setting the keys

keys = [
    # ------ Window Managment ShortCuts ------

    Key([mod, "shift"], "r", lazy.restart()), # Restart QTile
    Key([mod, "shift"], "q", lazy.shutdown()), # ShutDown QTile to LightDM
    Key([mod], "Tab", lazy.next_layout()), # Go to the next WorkSpace Mode
    Key([mod, "shift"], "Tab", lazy.prev_layout()), # Go to the previous WorkSpace Mode

    Key([mod], "w", lazy.window.kill()), # Close target window
    Key([mod], "f", lazy.window.toggle_floating()), # Toggle non-tiling mode

    Key([mod], "h", lazy.layout.left()), # Move focus to left
    Key([mod], "l", lazy.layout.right()), # Move focus to right
    Key([mod], "j", lazy.layout.down()), # Move focus down
    Key([mod], "k", lazy.layout.up()), # Move focus up

    Key([mod, "shift"], "h", lazy.layout.shuffle_left()), # Move window left
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()), # Move window right

    Key([mod, "shift"], "j", lazy.layout.shrink()), # Increases window size
    Key([mod, "shift"], "k", lazy.layout.grow()), # Decreases window size


    # ------ Apps ShortCuts ------

    Key([mod], "Return", lazy.spawn("alacritty")), # Open terminal

    Key([mod], "m", lazy.spawn("rofi -show drun")), # Run app
    Key([mod], "n", lazy.spawn("rofi -show")), # Search in running apps

    Key([mod], "s", lazy.spawn("scrot -q 100 -e 'mv $f ~/Pictures/ScreenShots/'")), # Make a ScreenShot
    Key([mod, "shift"], "s", lazy.spawn("scrot -s -q 100 -e 'mv $f ~/Pictures/ScreenShots/'")), # Selected Area ScreenShot

    Key([mod], "t", lazy.spawn("redshift -O 4000")), # Increase blue filter
    Key([mod, "shift"], "t", lazy.spawn("redshift -x")), # Reset blue filter

    Key([mod], "a", lazy.spawn("code")), # Run VS Code
    Key([mod], "s", lazy.spawn("spotify")), # Run Spotify
    Key([mod], "d", lazy.spawn("discord")), # Run Discord
    Key([mod], "f", lazy.spawn("firefox")), # Run Firefox

    Key([mod], "p", lazy.spawn("killall dunst")),


    # ------ Miscellaneous ShortCuts ------

    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+")), # Turn up volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%-")), # Turn down volume
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")), # Mute volume

    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")), # Turn up bright
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")), # Turn down bright

]
