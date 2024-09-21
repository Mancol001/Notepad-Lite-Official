#meow meow gizmo

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
from tkinter import filedialog

import sys
import webbrowser

# let's gooo uiii

window = tk.Tk()

window.geometry('400x300')



# ï̵̝̦̟̗̽́̽̓̈͋̈͂̚̕͝͝ţ̵̩͙̯̣͔̖̗̜̫̥̑̏̈́ ̷͈͓͖̜̲̜̞̀̉̔̋̆̐̿̋̊ͅt̴̨̧̧̛͉͎̗͇̻͖͎̙͚̓͊̓͊̋̂̉̈́͛͑͛̅̒̋̂̌̈́̕a̴̛̛̝͔͕̠͇̲̗̐̈̽̌̌̔̈́͗͆̍̏̎̅͌̑̕͝ķ̵͙͓͕̹͚͕͔͚̲̓̾̔̂͑͊͂̎̉̓͑͗̒͊̿̽̿̚̕͘͝ȩ̴̡̧͔͈̫̫̩̪̗̮̜̻̺̣̲̖̘̘̰̓͛̂̊̓͊̈́̕͜s̶̡̢̨̪͎̹̦̱̳͑́̋̃͂̔̔́͂̏̀ ̶̢̢̨̬̩̖̱͚̜̳̹̻̮̰̭̦̲͔̱̉̆́̎̍̏̃̀̄͂̈́̄̊͛̚͜ṁ̷̡̫̥̰̱̬͇̞͖̳͇͌̂͊̈́̽͛̇̔́̋̓́̽͐̎͆̕̕͜ͅė̷̩͍͕̀̍̂́̓̀̃̽̈̌̈̇͌̅͠ ̸̡̱̩̳̟̘̺̦̓̀͂̃́̔̉̔͂̒̌̅̔̔͐͝͠s̴̟̾̇̉̑̓̓͌̂͗̍͘ŏ̴̜͕̙̔̒͆̽̈́̏̈́̊̇̊͘͝ǫ̶̛̲̪̱̣̮̱͕͍̰̥͎̩͆͛̀̽͌̈́͆͂̋͋͗̅͋̔͝͝ͅ ̴̧̨̛̛͕̩͖̗̪̲̮̺̗̩̜̏̾́̔́̽͗̀̈́͂̔̚̚͜͝͝l̷͎̬̜͚̼͇̗̈̓̽̒̑̚͝͝o̴̧̺̣͓͗͜ṋ̶̢̡̧̛͓̩̪̺̗̞̳͇̱͉̯͍̙̮̮̇̎̾̊̌͑̐̓̉͋̾̀͋̅͘͝ḡ̸͔͑̄̌̓͌̎̊͆̈͂͆͝͝ģ̸̦̼͙̲̳͓̮̺͎͉̪̮̩̗͙̗̟̼͒̔͌͛̽͗̄̆͛̏̕͘͜͜ǧ̵̢̺̭̙͜͜g̸̢̧̛̝͙̞̣̯̫̞̮̥̱͆̀̑̄͆̄͊͘



window.title("Notepad Lite")

window.resizable(0,0)


def about_app():
    messagebox.showinfo("Notepad Lite", "Made in 2024, App Version: 1.0, App was made just for fun (;")

textZone = tk.Text(master=window)
menu_up = Menu(window)
menuButton = Menu(menu_up, tearoff=0)
menuFileButton = Menu(menu_up, tearoff=0)

menuButton.add_command(label="Exit", command=sys.exit)
menuButton.add_command(label="About", command=about_app)
menuButton.add_command(label="Creator's Github", command=lambda: webbrowser.open("https://github.com/Mancol001"))

def save_as_func():
    text_inputed = textZone.get("1.0", tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    with open(file_path, "w") as file:
        file.write(text_inputed)
        print("File has saved")
        messagebox.showinfo("Notepad Lite", "File has been saved")

def open_file_func():
    text_inputed = textZone.get("1.0", tk.END)
    file_path = filedialog.askopenfilename(defaultextension=".txt", 
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    with open(file_path, "r") as file:
        text_cont = file.read()
        textZone.delete("1.0", tk.END)
        textZone.insert(tk.END, text_cont)



def save_open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", 
                                               filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            target_text = textZone.get("1.0", tk.END)
            file.write(target_text)
            messagebox.showinfo("Notepad Lite", "File has been saved")


menuFileButton.add_command(label="Save as", command=save_as_func)
menuFileButton.add_command(label="Save", command=save_open_file)

menuFileButton.add_command(label="Open File", command=open_file_func)



menu_up.add_cascade(label="Menu", menu=menuButton)
menu_up.add_cascade(label="File", menu=menuFileButton)

textZone.pack()

window.config(menu=menu_up)

window.mainloop()