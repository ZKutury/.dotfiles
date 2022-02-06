# QTile Layouts Config File

from libqtile import layout
from libqtile.config import Match
from settings.colors import colors

# Layout General Config

layout_conf = {
    "margin": 2,
    "border_focus": colors[4],
    "border_width": 2
}


# Layouts

layouts = [
    layout.Max(),
    layout.MonadTall(**layout_conf),
]


# Floating Layouts Compability

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)