from PIL import Image
from pynput import keyboard
import time
import os
import sys


class Terminal:
    def __init__(self):
        self.lastTime = time.time()
        self.fps = 0

        self.keyboard_listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.keyboard_listener.start()
        
        self.keys = set()

    def render(self, frameBuffer, x, y):
        while (time.time() - self.lastTime) < 1.0/30:
            pass
        
        self.fps = int(1.0/(time.time() - self.lastTime)+0.5)
        self.lastTime = time.time()
        rndr = [f"\033[H"]
        
        for j in range(y):
            for i in range(x):
                rgb = frameBuffer[i,j]
                bright = (((rgb[0] + rgb[1] + rgb[2])/(3*255))) ** 0.75
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
                try:
                    length = int(255/(rgb[0]**2 + rgb[1]**2 + rgb[2]**2)**0.5)
                except:
                    length = 0
                #code = f"38;2;{rgb[0]*length};{0};{rgb[2]*length}"
                code = f"38;2;{rgb[0]};{rgb[1]};{rgb[2]}"
                rndr.append(f"\033[{code}m"+key+f"\033[0m")
            rndr.append(f"\n")
        rndr.append(f"fps:{self.fps} size:{x},{y} keys:{self.keys}\n")
        sys.stdout.write("".join(rndr))
        sys.stdout.flush()
        
        pass

    # Define keyboard event handlers
    def on_press(self, key):
        self.keys.add(key)

    def on_release(self, key):
        self.keys.remove(key)

def main():
    ter = Terminal()
    print("\033[?7l", end="")    # Turn off line wrap
    print("\033[?25l", end="")   # Hide blinking text cursor
    print("\033[?1000h", end="") # ENABLE mouse tracking (Disables native drag-to-highlight)
    print("\033[?1003h", end="") # ENABLE all mouse motion tracking
    try:
        while keyboard.Key.esc not in ter.keys:
            screen = [os.get_terminal_size().columns,os.get_terminal_size().lines-1]# minus 1 for output line
            pix = getTempImageArray(screen[0],screen[1])
            ter.render(pix, screen[0],screen[1])
            
    except KeyboardInterrupt:
        pass
        
    print("end2")
    print("\033[?1000l", end="") # DISABLE mouse tracking (Restores text highlighting)
    print("\033[?1003l", end="") # DISABLE motion tracking
    print("\033[?25h", end="")   # Restore cursor
    print("\033[?7h", end="")    # Restore line wrap
    print("\033c", end="")              # Reset terminal attributes

def getTempImageArray(x,y):
    gifs = [
        "tempGif/MJ-giphy.gif",
        "tempGif/giphy.gif",
        "tempGif/tf2.gif",
    ]
    im = Image.open(gifs[cur_gifs[1]%3])

    if cur_gifs[0] >= im.n_frames * 2:
        cur_gifs[0] = 0
        cur_gifs[1] += 1
        im = Image.open(gifs[cur_gifs[1]%3])
    im.seek(cur_gifs[0]%im.n_frames)
    cur_gifs[0] += 1
    
    
    current_frame = im.convert("RGBA").resize((x,y), Image.Resampling.LANCZOS)
    return current_frame.load()

cur_gifs = [0,0]
main()
