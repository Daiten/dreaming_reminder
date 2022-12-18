import random
import time
import tkinter as tk

def show_dream_message():
    # Generate a random time interval between 1 and 12 hours
    sleep_interval = random.randint(3600, 43200)
    print("Sleeping for {} seconds".format(sleep_interval))
    time.sleep(sleep_interval)

    # Display the dream message in a GUI window
    dream_window = tk.Tk()
    dream_window.title("Dream Message")
    dream_label = tk.Label(dream_window, text="You are dreaming")
    dream_label.pack()
    dream_window.mainloop()

while True:
    show_dream_message()
