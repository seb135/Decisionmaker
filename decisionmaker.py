import customtkinter as tk
from random import choice

tk.set_appearance_mode("dark")

tk.set_default_color_theme("dark-blue")

options = ['Go for a walk', 'Play a video game', 'Do something productive', 'Netflix & Chill', 'Go shopping']

option = choice(options)

def show_response():
        response = option
        textbox.insert(tk.END, response)

root = tk.CTk()
root.geometry("500x350")

frame = tk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = tk.CTkLabel(master=frame, text='DecisionMaker 3000')
label.pack(pady=12, padx=10)

entry1 = tk.CTkEntry(master=frame, placeholder_text="How do you feel?")
entry1.pack(pady=12,padx=10)

button = tk.CTkButton(master=frame, text='Give me something to do', command=show_response)
button.pack(pady=12,padx=10)

textbox = tk.CTkTextbox(master=frame, height=12, width=300 )
textbox.pack(pady=12,padx=10)

root.mainloop()



