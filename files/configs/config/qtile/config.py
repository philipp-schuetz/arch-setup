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
app_launcher = "dmenu_run"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod], "r",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "shift"], "Return", lazy.spawn(app_launcher), desc="Spawn app launcher"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # custom hotkeys
    # brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 10"), desc="increase screen brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 10"), desc="decrease screen brightness"),

    # sound 
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle"), desc="mute audio"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute"), desc="lower volume"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute"), desc="raise volume"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
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
    layout.Columns(
        border_focus=["#6d97d3"],
        border_normal="161e2a",
        border_width=1,
        margin=8,
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
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
font = "MesloLGS NF"

screens = [
    Screen(
        wallpaper="~/.config/qtile/wallpaper.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.GroupBox(
                    fontsize=10,
                    font=font,
                    padding=5,
                    margin_x=0,
                    rounded=False,
                    background=widget_colors["bg"],
                    active=widget_colors["font_group"],
                    inactive=widget_colors["font_group"],
                    highlight_method="block",
                    disable_drag=True,
                    ),
                widget.Sep(
                    linewidth = 0,
                    padding = 5,
                    background = widget_colors["bg"],
                    ),
                widget.CurrentLayoutIcon(
                    padding = 0,
                    background = widget_colors["bg"],
                    scale=0.6,
                    ),
                #widget.CurrentLayout(
                #    font=font,
                #    padding = 0,
                #    background = widget_colors["bg"],
                #    ),
                widget.Sep(
                    linewidth = 0,
                    padding = 5,
                    background = widget_colors["bg"],
                    ),
                widget.WindowName(
                    font=font,
                    background=widget_colors["bg"],
                    foreground=widget_colors["font_window_name"],
                    ),
                widget.Systray(
                    background=widget_colors["bg"],
                    ),
                widget.Sep(
                    linewidth = 0,
                    padding = 5,
                    background = widget_colors["bg"],
                    ),
                widget.TextBox(
                    font=font,
                    fontsize=15,
                    fmt="",
                    background=widget_colors["bg"],
                    padding=5,
                    ),
                widget.CheckUpdates(
                    font=font,
                    background=widget_colors["bg"],
                    colour_have_updates=widget_colors["font_updates"],
                    colour_no_updates=widget_colors["font_updates"],
                    display_format="{updates} Updates",
                    distro="Arch_yay",
                    padding=5,
                    no_update_string="Updated",
                    update_interval=600,
                    ),
                widget.Sep(
                    linewidth = 1,
                    padding = 5,
                    background = widget_colors["bg"],
                    ),
                widget.TextBox(
                    font=font,
                    fontsize=16,
                    fmt="墳",
                    background=widget_colors["bg"],
                    padding=5,
                    ),
                widget.Volume(
                    font=font,
                    background=widget_colors["bg"],
                    fmt="{}",
                    padding = 5,
                    ),
                widget.Sep(
                    linewidth = 1,
                    padding = 5,
                    background = widget_colors["bg"],
                    ),
                widget.Battery(
                    font=font,
                    fontsize=25,
                    background=widget_colors["bg"],
                    format="{char}",
                    padding=5,
                    full_char="",
                    charge_char="",
                    discharge_char="",
                    update_interval=5,
                    ),
                 widget.Battery(
                    font=font,
                    background=widget_colors["bg"],
                    format="{char}{percent:2.0%}",
                    charge_char="Charging... ",
                    discharge_char="",
                    padding=5,
                    ),
                widget.Sep(
                    linewidth = 1,
                    padding = 5,
                    background = widget_colors["bg"],
                    ),
                widget.Clock(
                    font=font,
                    background=widget_colors["bg"],
                    format="%a %d.%b %H:%M",
                    padding=5,
                    ),
                widget.Sep(
                    linewidth = 1,
                    padding = 5,
                    background = widget_colors["bg"],
                    ),
                widget.QuickExit(
                    font=font,
                    fontsize=16,
                    background=widget_colors["bg"],
                    default_text="",
                    countdown_format="{}",
                    padding=5,
                    ),
                widget.Sep(
                    linewidth = 0,
                    padding = 5,
                    background = widget_colors["bg"],
                    ),
            ],
            24, # size
            opacity=1,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

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
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
