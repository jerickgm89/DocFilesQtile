import asyncio
import os
import subprocess

from libqtile import hook

from core.screens import screens

bars = [screen.top for screen in screens]
margins = [sum(bar.margin) if bar else -1 for bar in bars]

# This hook is used to set the WM_NAME property of the bar window to "QTILE_BAR"
@hook.subscribe.startup
def startup():
    for bar, margin in zip(bars, margins):
        if not margin:
            bar.window.window.set_property(
                name="WM_NAME",
                value="QTILE_BAR",
                type="STRING",
                format=8,
            )

# This hook is used to move the Spotify client to the "0" group
@hook.subscribe.client_new
async def client_new(client):
    await asyncio.sleep(0.5)
    if client.name == "Spotify":
        client.togroup("0")

# This hook is used to run the autostart script
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])