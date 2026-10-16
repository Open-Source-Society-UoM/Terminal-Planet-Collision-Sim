from PIL import Image
from time import sleep
import os
import sys
gifs = [
    "tempGif/MJ-giphy.gif",
    "tempGif/giphy.gif",
    "tempGif/tf2.gif",
]
g = 0

im = Image.open(gifs[g%3])
im_size = [im.size[0],im.size[1],im.n_frames]
print("\033[?7l", end="")  # Turn off line wrap
print("\033[?25l", end="") # Hide the blinking text cursor
try:
    k = 0
    while True:
        if k >= im.n_frames * 2:
            k = 0
            g += 1
            im = Image.open(gifs[g%3])
            im_size = [im.size[0],im.size[1],im.n_frames]
        im.seek(k%im.n_frames)
        
        k = k+1
        current_frame = im.convert("RGBA")
        pix = current_frame.load()
        screen = [os.get_terminal_size().columns,os.get_terminal_size().lines]
        x = im_size[0]/os.get_terminal_size().columns
        y = im_size[1]/os.get_terminal_size().lines
        rndr = [f"\033[H"]
        for j in range(int(screen[1])):
            rndr.append(f"\n")
            for i in range(int(screen[0])):
                rgb = pix[i * im_size[0]//screen[0],j * im_size[1]//screen[1]]
                bright = (((rgb[0] + rgb[1] + rgb[2])/(3*255))) ** 0.5
                key = " "
                
                if bright > 0.9:
                    key = "@"
                elif bright > 0.8:
                    key = "%"
                elif bright > 0.7:
                    key = "#"
                elif bright > 0.6:
                    key = "*"
                elif bright > 0.5:
                    key = "+"
                elif bright > 0.4:
                    key = "="
                elif bright > 0.3:
                    key = "-"
                elif bright > 0.2:
                    key = ":"
                elif bright > 0.1:
                    key = "."
                code = f"38;2;{rgb[0]};{rgb[1]};{rgb[2]}"
                rndr.append(f"\033[{code}m"+key+f"\033[0m")
        sys.stdout.write("".join(rndr))
        sys.stdout.flush()
        sleep(1/60)
except KeyboardInterrupt:
    # reset keyboard
    print("\033[?25h\033[?7h")
    