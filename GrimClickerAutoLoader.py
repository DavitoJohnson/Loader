import tkinter as tk
from tkinter import simpledialog
from pynput.keyboard import Key, Listener, Controller
import pyautogui
import time

#Screen coordinates for clicks
click_coordinates = [(928, 625), (1564, 139), (673, 162), (679, 862), (824, 664), (1671, 103)]
dbl_click = [(1278,137)]
closing_seq = [(322, 160), (1227, 386)]
hotkey = Key.space #Default
click_delay = 0.1

#Function that handles hotkey
def on_press(key):
    global hotkey
    if key == hotkey:
        for coord in click_coordinates:
            #pyautogui.click(coord[0], coord[1])
            pyautogui.moveTo(coord[0], coord[1])
            #time.sleep(click_delay)
            pyautogui.mouseDown()
            #time.sleep(click_delay)
            pyautogui.mouseUp()
            #time.sleep(click_delay)
        for coord in dbl_click:
            #pyautogui.moveTo(coord[0], coord[1])
            #time.sleep(click_delay)
            pyautogui.doubleClick(coord[0], coord[1])
            #pyautogui.mouseDown()
            #time.sleep(click_delay)
            #pyautogui.mouseUp()
            #time.sleep(click_delay)
        for coord in closing_seq:
            pyautogui.moveTo(coord[0], coord[1])
            #time.sleep(click_delay)
            pyautogui.mouseDown()
            #time.sleep(click_delay)
            pyautogui.mouseUp()
            #time.sleep(click_delay)
    elif key == Key.esc:
        listener.stop()
        root.destroy()
            
#Function for changing hotkey
def change_hotkey():
    global hotkey, listener
    new_hotkey = simpledialog.askstring("Change Hotkey", "Press key to set a new hotkey").lower()
    if new_hotkey:
        hotkey = getattr(Key, new_hotkey, hotkey)
        #listener = Listener(on_press=on_press)
        listener.stop()
        #hotkey = getattr(Key, new_hotkey, hotkey)
        listener = Listener(on_press=on_press)
        listener.start()
        
#Starts keyboard listener
listener = Listener(on_press=on_press)
listener.start()

# with Listener(on_press=on_press) as listener:
root = tk.Tk()
root.title("Auto Loader")
label = tk.Label(root, text="Press '{}' to run the auto loader".format(hotkey, click_delay))
label.pack(padx=20, pady=10)
change_button =tk.Button(root, text="Change Hotkey", command=change_hotkey)
change_button.pack(pady=5)
root.mainloop()