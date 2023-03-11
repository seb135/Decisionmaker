import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text='Hello, world!')
label.pack()

button = tk.Button(root, text='Quit', command=root.quit)
button.pack()

root.mainloop()