import cfg 
import keyboard

# функция блокировки и разблокировки ввода с клавиатуры

def keyboard_lock():
        while True:
            keyboard.block_key(cfg.const.BLOCK_HOTKEY_LIST)



# пока не реализовано

def mouse_lock():
    pass

def mouse_unlock():
    pass