import cfg 
import keyboard



lock_keyboard_status = True

# функция блокировки и разблокировки ввода с клавиатуры
def keyboard_lock():
        while lock_keyboard_status:
            keyboard.block_key(cfg.const.BLOCK_HOTKEY_LIST)

# пока не реализовано

def mouse_lock():
    pass

def mouse_unlock():
    pass