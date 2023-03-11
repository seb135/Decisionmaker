import customtkinter as tk

tk.set_appearance_mode("dark")

tk.set_default_color_theme("dark-blue")

root = tk.CTk()
root.geometry("500x350")

def login():
    print("Test")

frame = tk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = tk.CTkLabel(master=frame, text='Login System')
label.pack(pady=12, padx=10)

entry1 = tk.CTkEntry(master=frame, placeholder_text="username")
entry1.pack(pady=12,padx=10)

entry2 = tk.CTkEntry(master=frame, placeholder_text="password", show="*")
entry2.pack(pady=12,padx=10)

button = tk.CTkButton(master=frame, text='login', command=login)
button.pack(pady=12,padx=10)

checkbox = tk.CTkCheckBox(master=frame, text="Stay logged in")
checkbox.pack(pady=12,padx=10)

root.mainloop()