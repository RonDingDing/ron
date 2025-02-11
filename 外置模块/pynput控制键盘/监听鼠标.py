from pynput import mouse

def log(string):
    with open("C:/Users/Administrator/Desktop/新建文件夹 (2)/111.txt", "a") as f:
        f.write(string)
        f.write("\n")

def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))
    log('Pointer moved to {0}'.format((x, y)))
    

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    log('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))

##    if not pressed:
##        # Stop listener
##        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))
    log('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))

# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
