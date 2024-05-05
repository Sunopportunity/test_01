import tkinter as tk

def on_button_click():
    label.config(text=f"Привет, {entry.get()}!")

root = tk.Tk()
root.title("АНКЕТА")

label = tk.Label(root, text="Введите свое имя")
label.pack()

entry = tk.Entry()
entry.pack()

button = tk.Button(root, text="OK", command=on_button_click)
button.pack()

root.mainloop()