import keyboard
from time import sleep
from win32gui import GetWindowText, GetForegroundWindow
sleep(0.3)

# Keybinds
print(r"""

 .-.
(o o) boo!
| O \
 \   \
  `~~~'

""")


def window():
    focus = GetWindowText(GetForegroundWindow())
    return focus


def keybind(args, kwargs):
    keyboard.remap_key(args, '0')
    keyboard.remap_key(kwargs, '9')


while True:
    window()
    sleep(0.6)
    if window() == 'Roblox':
        keybind('z', 'x')
        sleep(0.1)
    else:
        keyboard.unhook_all()
