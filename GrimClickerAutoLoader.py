import tkinter as tk
from tkinter import simpledialog
from pynput.keyboard import Key, Listener
import pyautogui
import time

#Screen coordinates for clicks
click_coordinates = [(928, 625), (1564, 139), (673, 162), (679, 862), (824, 664), (1671, 103), (1278,137), (1278, 137), (322, 160), (1227, 386)]
hotkey = Key.space #Default
click_delay = 1.0

#Function that handles hotkey
def on_press(key):
    if key == hotkey:
        for coord in click_coordinates:
            pyautogui.click(coord[0], coord[1])
            time.sleep(click_delay)
    elif key == Key.esc:
        listener.stop()
        root.destroy()
            
#Function for changing hotkey
def change_hotkey():
    global hotkey
    new_hotkey = simpledialog.askstring("Change Hotkey", "Press key to set a new hotkey").lower()
    if new_hotkey:
        hotkey = getattr(Key, new_hotkey, hotkey)
        
#Starts keyboard listener
with Listener(on_press=on_press) as listener:
    root = tk.Tk()
    root.title("Auto Loader")
    label = tk.Label(root, text="Press '{}' to run the auto loader".format(hotkey, click_delay))
    label.pack(padx=20, pady=10)
    change_button =tk.Button(root, text="Change Hotkey", command=change_hotkey)
    change_button.pack(pady=5)
    root.mainloop()
    
    listener.join()