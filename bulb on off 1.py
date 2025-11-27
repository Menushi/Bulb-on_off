import tkinter as tk

def turn_on():
    """Turn the bulb ON: change background and label text."""
    root.config(bg="yellow")
    status_label.config(text="Bulb is ON", bg="yellow")
    on_button.config(state="disabled")
    off_button.config(state="normal")

def turn_off():
    """Turn the bulb OFF: change background and label text."""
    root.config(bg="black")
    status_label.config(text="Bulb is OFF", bg="black", fg="white")
    on_button.config(state="normal")
    off_button.config(state="disabled")

root = tk.Tk()
root.title("Bulb On / Off")
root.geometry("300x200")
root.config(bg="black")     

status_label = tk.Label(
    root,
    text="Bulb is OFF",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="black"
)
status_label.pack(pady=20)


button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=10)

on_button = tk.Button(
    button_frame,
    text="ON",
    font=("Arial", 14, "bold"),
    width=7,
    command=turn_on
)
on_button.grid(row=0, column=0, padx=10)

off_button = tk.Button(
    button_frame,
    text="OFF",
    font=("Arial", 14, "bold"),
    width=7,
    command=turn_off,
    state="disabled"  
)
off_button.grid(row=0, column=1, padx=10)

root.mainloop()
