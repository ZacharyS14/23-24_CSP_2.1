#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk
#Test of button
def test_my_button():
    if(ent_username.get() == "Zach" and ent_password.get() == "isbetter"):
        frame_auth.tkraise()
    else:
        fail_label = tk.Label(frame_login, text="You suck, Try again")
        fail_label.pack()
# main window
root = tk.Tk()
root.wm_geometry("200x200")
# create empty frame
frame_login = tk.Frame(root)
frame_login.grid(row = 0, column = 0, sticky = "news")
frame_auth = tk.Frame(root)
frame_auth.grid(row = 0, column = 0, sticky = "news")

lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_password = tk.Label(frame_login, text='Password:')
lbl_password.pack()

ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack(pady=5)

btn_login = tk.Button(frame_login, text='Login', command=test_my_button)
btn_login.pack(pady=5)

tk.Label(frame_login,text="Password:",font="Courier")

frame_login.tkraise()
root.mainloop()