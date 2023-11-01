import os
import subprocess

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras.widget.decorations import RectDecoration


@hook.subscribe.startup
def autostart():
    subprocess.run("~/.config/qtile/autostart.sh")


colors = [
    ["#2e3440", "#2e3440"],  # 0 background
    ["#d8dee9", "#d8dee9"],  # 1 foreground
    ["#3b4252", "#3b4252"],  # 2 background lighter
    ["#bf616a", "#bf616a"],  # 3 red
    ["#a3be8c", "#a3be8c"],  # 4 green
    ["#ebcb8b", "#ebcb8b"],  # 5 yellow
    ["#81a1c1", "#81a1c1"],  # 6 blue
    ["#b48ead", "#b48ead"],  # 7 magenta
    ["#88c0d0", "#88c0d0"],  # 8 cyan
    ["#e5e9f0", "#e5e9f0"],  # 9 white
    ["#4c566a", "#4c566a"],  # 10 grey
    ["#d08770", "#d08770"],  # 11 orange
    ["#8fbcbb", "#8fbcbb"],  # 12 super cyan
    ["#5e81ac", "#5e81ac"],  # 13 super blue
    ["#242831", "#242831"],  # 14 super dark background
]
# fmt: off
fonts = {
    "primary": "JetBrainsMono Nerd Font"
    }

fontSize = {
    "IconLarge": "30",
    "h1": 25,
    "h2": 15,
    "h3": 12,
    "h4": 7,
    "frame": 20,
    }
# fmt: on
super = "mod4"
alt = "mod1"
control = "control"
terminal = "tilix"
chrome = "google-chrome-stable"
vscode = "code"
rofi = "rofi -show run"
filemanager = "nautilus"
screenshot = "kazam"

# fmt: off
keys = [
    # General day to day keybindings:
    Key([super], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([alt], "q", lazy.window.kill(), desc="Close the focused window"),
    Key([super], "b", lazy.spawn(chrome)),
    Key([super], "v", lazy.spawn(vscode)),
    Key([super], "e", lazy.spawn(filemanager)),
    Key([super], "r", lazy.spawn("killall -s SIGUSR1 qtile")),
    Key([super], "k", lazy.spawn(screenshot)),
    Key([super], "Space", lazy.spawn(rofi), desc="Launch Rofi"),
    Key([super], "left", lazy.layout.next(), desc="Move focus to the window to the left"),
    Key([super], "right", lazy.layout.previous(), desc="Move focus to the window to the right"),

    Key([alt, control], "Page_Up", lazy.layout.grow(), desc="Grow window to the left"),
    Key([alt, control], "Page_Down", lazy.layout.shrink(), desc="Grow window to the right"),
    Key([alt, control], "Left", lazy.layout.swap_left(), desc=""),
    Key([alt, control], "Right", lazy.layout.swap_right(), desc=""),

]
# fmt: on

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [super],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [super, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.MonadThreeCol(border_width=1, border_focus="#0a0047", margin=10),
]


widget_defaults = dict(
    font=fonts["primary"],
    fontsize=fontSize["h2"],
    padding=0,
    background=colors[0],
    decorations=[
        BorderDecoration(
            colour=colors[0],
            border_width=[11, 0, 10, 0],
        )
    ],
)
extension_defaults = widget_defaults.copy()


def dunst():
    return subprocess.check_output(["./.config/qtile/dunst.sh"]).decode("utf-8").strip()


def toggle_dunst():
    qtile.cmd_spawn("./.config/qtile/dunst.sh --toggle")


def toggle_notif_center():
    qtile.cmd_spawn("./.config/qtile/dunst.sh --notif-center")


# Mouse_callback functions
def open_launcher():
    lazy.spawn(rofi)


def kill_window():
    qtile.cmd_spawn("xdotool getwindowfocus windowkill")


def open_pavu():
    qtile.cmd_spawn("pavucontrol")


def open_powermenu():
    qtile.cmd_spawn("power")


group_box_settings = {
    "padding": 5,
    "borderwidth": 4,
    "active": colors[9],
    "inactive": colors[10],
    "disable_drag": True,
    "rounded": True,
    "highlight_color": colors[2],
    "block_highlight_text_color": colors[6],
    "highlight_method": "block",
    "this_current_screen_border": colors[14],
    "this_screen_border": colors[7],
    "other_current_screen_border": colors[14],
    "other_screen_border": colors[14],
    "foreground": colors[1],
    "background": colors[14],
    "urgent_border": colors[3],
}

screens = [
    Screen(
        wallpaper="~/Pictures/Wallpapers/6GMqcVqw.png",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.TextBox(
                    text="",
                    foreground=colors[1],
                    background=colors[0],
                    font=fonts["primary"],
                    fontsize=fontSize["IconLarge"],
                    padding=20,
                    mouse_callbacks={"Button1": lazy.spawn(rofi)},
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    padding=10,
                    size_percent=50,
                ),
                widget.Notify(
                    font=fonts["primary"],
                    fontsize=fontSize["h2"],
                    foreground=colors[1],
                    background=colors[0],
                    action=True,
                    default_timeout=5,
                    scroll=True,
                    scroll_clear=True,
                    scroll_delay=0,
                    scroll_hide=True,
                    scroll_interval=0.01,
                    scroll_step=1.5,
                    scroll_repeat=True,
                    width=500,
                ),
                widget.Spacer(),
                widget.TextBox(
                    text="",
                    font=fonts["primary"],
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=fontSize["frame"],
                    padding=0,
                ),
                widget.Clock(
                    format="%A, %b %d %Y | %H:%M:%S",
                    background=colors[14],
                    foreground=colors[1],
                    fontsize=fontSize["h3"],
                    padding=0,
                ),
                widget.TextBox(
                    text="",
                    font=fonts["primary"],
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=fontSize["frame"],
                    padding=0,
                ),
                widget.Spacer(),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    font=fonts["primary"],
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=fontSize["frame"],
                    padding=0,
                ),
                widget.TextBox(
                    text="CPU ",
                    font=fonts["primary"],
                    foreground=colors[1],
                    background=colors[14],
                    fontsize=fontSize["h4"],
                    padding=0,
                ),
                widget.CPU(
                    font=fonts["primary"],
                    foreground=colors[1],
                    background=colors[14],
                    fontsize=fontSize["h3"],
                    markup=True,
                    format="{freq_current}GHz {load_percent}%",
                ),
                widget.TextBox(
                    text=" GPU ",
                    font=fonts["primary"],
                    foreground=colors[1],
                    background=colors[14],
                    fontsize=fontSize["h4"],
                    padding=0,
                ),
                widget.NvidiaSensors(
                    font=fonts["primary"],
                    foreground=colors[1],
                    background=colors[14],
                    fontsize=fontSize["h3"],
                ),
                widget.TextBox(
                    text="",
                    font=fonts["primary"],
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=fontSize["frame"],
                    padding=0,
                ),
                widget.TextBox(
                    text="",
                    font=fonts["primary"],
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=fontSize["frame"],
                    padding=0,
                ),
                widget.NetGraph(
                    interface="enp5s0",
                    format="{down} ↓↑ {up}",
                    font=fonts["primary"],
                    foreground=colors[7],
                    background=colors[14],
                    fill_color=colors[0],
                    graph_color=colors[4],
                    line_width=1,
                    margin_y=2,
                    type="line",
                    samples=1000,
                    frequency=0.1,
                ),
                widget.TextBox(
                    text="",
                    font=fonts["primary"],
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=fontSize["frame"],
                    padding=0,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    font=fonts["primary"],
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=fontSize["frame"],
                    padding=0,
                ),
                widget.Systray(
                    icon_size=26,
                    background=colors[14],
                    padding=7,
                ),
                widget.TextBox(
                    text="",
                    font=fonts["primary"],
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=fontSize["frame"],
                    padding=0,
                ),
            ],
            28,
            margin=[3, 12, 0, 12],
            border_width=[5, 5, 5, 5],
            border_color="#2e3440",
        ),
        bottom=bar.Gap(0),
        left=bar.Gap(0),
        right=bar.Gap(0),
    )
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


import subprocess
import os
from libqtile import hook


@hook.subscribe.startup
def dbus_register():
    id = os.environ.get("DESKTOP_AUTOSTART_ID")
    if not id:
        return
    subprocess.Popen(
        [
            "dbus-send",
            "--session",
            "--print-reply",
            "--dest=org.gnome.SessionManager",
            "/org/gnome/SessionManager",
            "org.gnome.SessionManager.RegisterClient",
            "string:qtile",
            "string:" + id,
        ]
    )
