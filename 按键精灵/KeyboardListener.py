from pynput import keyboard


def on_press(key):
    try:
        print(str(key.char) + '')
    except AttributeError:
        print(str(key) + '')


def on_release(key):
    pass


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()