# QTile Widgets Config File

from settings.colors import colors
from libqtile import widget, lazy, qtile
import os

def left_corner(cn_color, bg_color=0):
    return widget.TextBox(
        foreground = colors[cn_color],
        background = colors[bg_color],
        text = "\ue0b6",
        fontsize = 24.75,
        padding=0
    )

def right_corner(cn_color, bg_color=0):
    return widget.TextBox(
        foreground = colors[cn_color],
        background = colors[bg_color],
        text = "\ue0b4",
        fontsize = 24.75,
        padding=0
    )   

def separator():
    return widget.Sep(
        linewidth = 0,
        padding = 10
    )

def icon(icon, cn_color, bg_color=0, size=50):
    return widget.TextBox(
        foreground = colors[cn_color],
        background = colors[bg_color],
        text = icon,
        fontsize = size
    )

def window_counter(cn_color, bg_color=0):
    return widget.WindowCount(
        foreground = colors[cn_color],
        background = colors[bg_color],
        show_zero = True
    )

def current_layout(bg_color):
    return widget.CurrentLayoutIcon(
        #custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
        background = colors[bg_color],
        scale = 0.5
    )

def cpu_percent(cn_color, bg_color=0):
    return widget.CPU(
        foreground = colors[cn_color],
        background = colors[bg_color],
        format = "{load_percent}%"
    )

def memory_usage(cn_color, bg_color=0):
    return widget.Memory(
        foreground = colors[cn_color],
        background = colors[bg_color],
        format = "{MemUsed: .0f} MiB"
    ) 

def available_space(cn_color, bg_color=0):
    return widget.DF(
        foreground = colors[cn_color],
        background = colors[bg_color],
        visible_on_warn = False,
        format = "{f} GiB ({r:.0f}%)"
    )

def workspaces(cn_color, active_color, focus_color, bg_color=0, size=40):
    return widget.GroupBox(
        background = colors[bg_color],
        inactive = colors[cn_color],
        active = colors[active_color],
        this_current_screen_border = colors[focus_color],
        highlight_method = "text",
        disable_drag = True,
        center_aligned = False,
        fontsize = size,
        margin_y = -9,
        margin_x = 0,
        padding_y = 0,
        padding_x = 5,
    )

def wifi(cn_color, bg_color=0):
    return widget.Wlan(
        foreground = colors[cn_color],
        background = colors[bg_color],
        format = "{essid}",
        interface = "wlp3s0",
        max_chars = 11,
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("alacritty -e nmtui")}
    )

def volume(cn_color, bg_color=0):
    return widget.PulseVolume(
        foreground = colors[cn_color],
        background = colors[bg_color],
        mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("pavucontrol")}
    )

def backlight(cn_color, bg_color=0):
    return widget.Backlight(
        foreground = colors[cn_color],
        background = colors[bg_color],
        backlight_name = "intel_backlight"
    )

def clock(cn_color, bg_color=0):
    return widget.Clock(
        foreground = colors[cn_color],
        background = colors[bg_color],
        format = "%H:%M %D"
    )

def battery(cn_color, low_color, bg_color=0):
    return widget.Battery(
        foreground = colors[cn_color],
        background = colors[bg_color],
        format = "{percent:2.0%}",
        update_interval = 10,
        low_foreground = low_color,
        low_percentage = 0.15
    )

def icon_battery(cn_color, low_color, size, bg_color=0):
    return widget.Battery(
        foreground = colors[cn_color],
        background = colors[bg_color],
        format = "{char}",
        charge_char = "",
        discharge_char = "",
        full_char ="",
        empty_char = "",
        unknown_char = "",
        update_interval = 1,
        fontsize = size,
        low_foreground = low_color,
        low_percentage = 0.15
    )

def logo(icon, cn_color, bg_color=0, size=50):
    return widget.TextBox(
        foreground = colors[cn_color],
        background = colors[bg_color],
        text = icon,
        fontsize = size,
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("alacritty -e fun")}
    )

def unix_updates(cn_color, update_color, bg_color=0):
    return widget.CheckUpdates(
        colour_no_updates = colors[cn_color],
        colour_have_updates = colors[update_color],
        background = colors[bg_color],
        no_update_string = "0",
        display_format = "{updates}!"
    )