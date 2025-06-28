import cfg 
import keyboard


# Статус блокировки клавиатуры
lock_keyboard_status = True
lock_mouse_status = True

# функция блокировки и разблокировки ввода с клавиатуры
def keyboard_lock(lock_keyboard_status):
        while lock_keyboard_status:
            keyboard.block_key(cfg.const.BLOCK_HOTKEY_LIST)

# пока не реализовано

# функция блокировки мыши
def mouse_lock():
    pass
# функция разблокировки мыши
def mouse_unlock():
    pass