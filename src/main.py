import pystray
import sys
import time
from PIL import Image
from pystray import Menu, MenuItem
import TimestamptoClipboard as ts


def timestamp_action(icon):
    ts.run()

def exit_action(icon):
    icon.visible = False
    icon.stop()


def setup(icon):
    icon.visible = True


def init_icon():
    icon = pystray.Icon('mon')
    icon.menu = Menu(
        MenuItem('TimeStamp', lambda : timestamp_action(icon)),
        MenuItem('Exit', lambda : exit_action(icon)),
    )
    icon.icon = Image.open('ICON.png')
    icon.title = 'ToolsBox'

    icon.run(setup)

init_icon()
