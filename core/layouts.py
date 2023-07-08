from libqtile import layout

from utils import color
from utils.match import title, wm_class

config = {
    "border_focus": color["magenta"],
    "border_normal": color["bg"],
    "border_width": 0,
    "margin": 10,
    "single_border_width": 0,
    "single_margin": 10,
}

layouts = [
    layout.MonadTall(
        **config,
        change_ratio=0.02,
        min_ratio=0.30,
        max_ratio=0.70,
    ),
    layout.Max(**config),
]

floating_layout = layout.Floating(
    border_focus=color["white"],
    border_normal=color["bg"],
    border_width=0,
    fullscreen_border_width=0,
    float_rules=[
        *layout.Floating.default_float_rules,
        *wm_class([
            "confirmreset",
            "Display",
            "floating",
            "gnome-screenshot",
            "gpicview",
            "lxappearance",
            "makebranch",
            "maketag",
            "pavucontrol",
            "psterm",
            "ssh-askpass",
            "thunar",
            "Xephyr",
            "xfce4-about",
        ]),  # fmt: skip
        *title([
            "branchdialog",
            "minecraft-launcher",
            "pinentry",
        ]),  # fmt: skip
    ],
)
