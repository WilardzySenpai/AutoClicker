import time
import keyboard
from pynput.mouse import Button, Controller
import tkinter as tk
from tkinter import Scale
import threading


mouse = Controller()
clicking = False  
click_count = 0 
speed = 0.5

# Create Tkinter window
root = tk.Tk()
root.title("Auto-Clicker")
root.resizable(True, True)  # Make the window resizable

# Click display label
label = tk.Label(root, text="Clicks: 0  Auto-Click: OFF")
label.grid(row=0, column=0, columnspan=2, pady=5)  

# Speed control with label and scale
speed_label = tk.Label(root, text="Speed (seconds per click):")
speed_label.grid(row=1, column=0, pady=5)
speed_scale = Scale(root, from_=0, to=10, resolution=0.05, orient='horizontal')
speed_scale.set(speed)  # Set initial speed
speed_scale.grid(row=1, column=1, pady=5)

def center_window(win):
    """ Centers a Tkinter window """
    win.update_idletasks()  # Update window information
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def update_display():
    label.config(text=f"Clicks: {click_count}  Auto-Click: {'ON' if clicking else 'OFF'}")

def click_repeatedly():
    global clicking, click_count
    while clicking:
        mouse.click(Button.left, 1)
        click_count += 1
        update_display()  # Update display after each click
        speed = speed_scale.get()  # Get the updated speed value
        time.sleep(speed)  # Use the updated speed

# Handle keyboard events
def on_press(key):
    global clicking
    if key.name == 'f6':
        clicking = True  
    elif key.name == 'f7':
        clicking = False  

# Register the event listener 
keyboard.on_press(on_press)

# After creating the window, center it:
center_window(root)  

# Main loop 
def run_autoclicker(): 
    while True:
        click_repeatedly() 
        time.sleep(0.1)  # Small delay

threading.Thread(target=run_autoclicker).start()  # Start the auto-clicker in a thread

root.update()  # Update the Tkinter window (this might not be needed)

# Start the Tkinter event loop    
root.mainloop() 
