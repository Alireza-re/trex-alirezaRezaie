import tkinter as tk
import tkinter.messagebox as messagebox
import random

move_count = 0

def move_cancel_button():
    global move_count
    move_count += 1
    if move_count >= 5:
        messagebox.showinfo("پیام", "خودتو خسته نکن الکی")
        move_count = 0 
    else:
        new_x = random.randint(10, 200)
        new_y = random.randint(10, 200)
        cancel_button.place(x=new_x, y=new_y)

def show_second_message_and_exit():
    messagebox.showinfo("پیام", "كاملا موافقم")
    root.quit()  

root = tk.Tk()
root.title("Mister Programmer")

header_label = tk.Label(root, text="ستون قبول داری خیلی گنگی ؟", font=("Lalezar", 22))
header_label.pack()


ok_button = tk.Button(root, text="!نه،اصلا", bg="green", fg="#fff", command=show_second_message_and_exit)
ok_button.pack()


cancel_button = tk.Button(root, text="اره ،معلومه", bg="red", fg="#fff")
cancel_button.pack()

cancel_button.bind("<Enter>", lambda e: move_cancel_button())

root.mainloop()
