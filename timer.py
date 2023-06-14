import tkinter as tk
from tkinter import messagebox
import pygame

def start_timer():
    remaining_time = 2 * 60 

    def update_time():
        nonlocal remaining_time

        if remaining_time > 0:
            mins = remaining_time // 60
            secs = remaining_time % 60
            time_label.config(text=f"{mins:02d}:{secs:02d}")

            remaining_time -= 1
            window.after(1000, update_time)  # Call itself after 1 second (1000 ms)
        else:
            # Play sound
            pygame.mixer.music.load("success.mp3")
            pygame.mixer.music.play()

    update_time()

# Initialize pygame mixer
pygame.mixer.init()

# Create the main window
window = tk.Tk()
window.title("Timer")
window.geometry("300x200")
window.lift()
window.attributes('-topmost', True)

# Create the time label
time_label = tk.Label(window, text="02:00", font=("Arial", 40))
time_label.pack(pady=50)

# Create the start button
start_button = tk.Button(window, text="Start Timer", command=start_timer)
start_button.pack()

# Run the GUI loop
window.mainloop()
