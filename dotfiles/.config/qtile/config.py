# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os
import subprocess

mod = "mod4"
terminal = guess_terminal()
terminal = "alacritty"
app_launcher = "rofi -show drun"
screenshot = "flameshot gui"
calculator = "rofi -show calc -modi calc -no-show-match -no-sort"

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Launch apps
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "shift"], "Return", lazy.spawn(app_launcher), desc="Spawn app launcher"),
    Key([mod, "shift"], "s", lazy.spawn(screenshot), desc="Spawn screenshot utility"),
    Key([mod, "shift"], "c", lazy.spawn(calculator), desc="Spawn calculator"),


    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Monitor focus
    Key([mod], "period", lazy.next_screen(), desc='Move focus to next monitor'),
    Key([mod], "comma", lazy.prev_screen(), desc='Move focus to prev monitor'),

    # Sound
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle"), desc="mute audio"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 2 sset Master 10- unmute"), desc="lower volume"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 2 sset Master 10+ unmute"), desc="raise volume"),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/Pause player"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Skip to next"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Skip to previous"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

layouts = [
    layout.Columns(
        border_focus=["#89b4fa"],
        border_normal="161e2a",
        border_width=1,
        margin=8,
    ),
    layout.Max(
        margin=8,
    ),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# widget colors for flower bg image
widget_colors = {
        "bg": "#161e2a",
        "active_group": "#6d97d3",
        "inactive_group": "#32482a",
        "font_group": "#ffffff",
        "font_window_name": "#6d97d3",
        "font_updates": "#ffffff",
        }

colors = [
    "#fab387", #peach
    "#a6e3a1", #green
]

font = "MesloLGS NF"



def init_widgets_list():
    widgets_list = [
        widget.Sep(
                linewidth = 0,
                padding = 8,
                ),
        widget.Image(
                filename = "~/.config/qtile/arch-lavender.png",
                scale = "False",
                margin = 2,
                ),
        widget.Sep(
                linewidth = 0,
                padding = 8,
                ),
        widget.GroupBox(
            fontsize=10,
            font=font,
            padding=5,
            padding_x=3,
            margin_y=3,
            margin_x=0,
            borderwidth=3,
            active="#cdd6f4",
            inactive="#74c7ec",
            highlight_method="block",
            disable_drag=True,
            highlight_color="#1e1e2e",
            this_current_screen_border="#585b70",
            this_screen_border="#313244",
            other_current_screen_border="#585b70",
            other_screen_border="#313244",
            ),
        # widget.Sep(
        # linewidth = 0,
        #	padding = 8,
        #	),
        # widget.CurrentLayoutIcon(
        # 	padding = 0,
        # 	foreground="#89dceb",
        # 	scale=0.6,
        # 	),
        # widget.CurrentLayout(
        #	font=font,
        #	foreground="#89dceb",
        #	padding = 0,
       #	),
        widget.Sep(
            linewidth = 0,
            padding = 8,
            ),
        widget.WindowName(
            font=font,
            foreground="#a6e3a1",
            ),
        widget.Systray(
                icon_size=20,
                padding=4,
                ),
        widget.Sep(
            linewidth = 0,
            padding = 8,
            ),
        widget.TextBox(
            font=font,
            foreground="#f9e2af",
            fontsize=16,
            fmt="",
            padding=5,
            ),
        widget.Volume(
            font=font,
            foreground="#f9e2af",
            fmt="{}",
            padding = 5,
            ),
        widget.Sep(
            linewidth = 0,
            padding = 8,
            ),
        widget.TextBox(
            font=font,
            foreground="#fab387",
            fontsize=16,
            fmt="",
            padding=5,
            ),
        widget.Wlan(
            font=font,
            foreground="#fab387",
            format="{essid}",
            fmt="{}",
            padding = 5,
            ),
        widget.Sep(
            linewidth = 0,
            padding = 8,
            ),
        widget.TextBox(
            font=font,
            foreground="#f38ba8",
            fontsize=15,
            fmt="",
            padding=5,
            ),
        widget.CheckUpdates(
            font=font,
            foreground="#f38ba8",
            colour_have_updates="#f38ba8",
            colour_no_updates="#f38ba8",
            display_format="{updates} Updates",
            distro="Arch_yay",
            padding=5,
            no_update_string="Updated",
            update_interval=60,
            ),
        widget.Sep(
            linewidth = 0,
            padding = 8,
            ),
        widget.TextBox(
            font=font,
            foreground="#cba6f7",
            fontsize=16,
            fmt="",
            padding=5,
            ),
        widget.Clock(
            font=font,
            foreground="#cba6f7",
            format="%a %d.%b %H:%M",
            padding=5,
            ),
        widget.Sep(
            linewidth = 0,
            padding = 8,
            ),
        widget.QuickExit(
            font=font,
            foreground="#f5c2e7",
            fontsize=16,
            default_text="",
            countdown_format="{}",
            padding=5,
            ),
        widget.Sep(
            linewidth = 0,
            padding = 8,
            ),
    ]
    return widgets_list


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    del widgets_screen2[6:7] # remove systray widget from one screen
    return widgets_screen2

def init_screens():
    return [
        Screen(
            top=bar.Bar(widgets=init_widgets_screen1(),
                opacity=1.0,
                size=24,
                margin=[8, 8, 0, 8],
                background="#1e1e2e"
            ),
            wallpaper="~/.config/qtile/wallpaper.jpg",
            wallpaper_mode="fill",
        ),
        Screen(
            top=bar.Bar(widgets=init_widgets_screen2(),
                opacity=1.0,
                size=24,
                margin=[8, 8, 0, 8],
                background="#1e1e2e"
            ),
            wallpaper="~/.config/qtile/wallpaper.jpg",
            wallpaper_mode="fill",
        ),
    ]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
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
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

@hook.subscribe.client_new
def new_client(client):
    if client.name == "LibreWolf":
        client.togroup("2")
    elif client.name == "Discord Updater":
        client.togroup("3")
    elif client.name == " - Discord":
        client.togroup("3")

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
