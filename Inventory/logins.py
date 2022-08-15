"""Import required modules"""
from tkinter import *
import sqlite3
import tkinter
import customtkinter


customtkinter.set_appearance_mode("system")


class LoginSystem:
    """Login Class"""

    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.eid = StringVar()
        self.password = StringVar()
        self.utype = StringVar()

        self.login_frame = customtkinter.CTkFrame(
            self.root, bd=2, relief=RIDGE, fg_color="white"
        )
        self.login_frame.place(x=520, y=90, width=350, height=460)

        self.title = Label(
            self.login_frame,
            text="Login System",
            font=("Elephant", 30, "bold"),
            bg="white",
        )
        self.title.place(x=0, y=30, relwidth=1)

        self.lbl_user = Label(
            self.login_frame,
            text="Employee ID",
            font=("Andalus", 15),
            bg="white",
            fg="#767171",
        )
        self.lbl_user.place(x=50, y=100)

        self.txt_username = Entry(
            self.login_frame,
            textvariable=self.eid,
            font=("times new roman", 15),
            bg="#ECECEC",
        )
        self.txt_username.place(x=50, y=140, width=250)

        self.lbl_pass = Label(
            self.login_frame,
            text="Password",
            font=("Andalus", 15),
            bg="white",
            fg="#767171",
        )
        self.lbl_pass.place(x=50, y=200)

        self.txt_pass = Entry(
            self.login_frame,
            textvariable=self.password,
            show="*",
            font=("times new roman", 15),
            bg="#ECECEC",
        )
        self.txt_pass.place(x=50, y=240, width=250)

        self.btn_login = customtkinter.CTkButton(
            self.login_frame,
            width=250,
            height=35,
            border_width=0,
            corner_radius=8,
            fg_color="blue",
            hover_color="green",
            text="Log In",
            command=self.login,
        )
        self.btn_login.place(x=50, y=300)

    def login(self):
        """Login user when condition is right"""
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()

        try:
            if self.eid.get() == "" or self.password.get() == "":
                tkinter.messagebox.showerror(
                    "Error", "All fields are required", parent=self.root
                )
            else:
                cur.execute(
                    "select utype,eid from employee where eid=? AND pass=?",
                    (self.eid.get(), self.password.get()),
                )
                user = cur.fetchone()
                if user is None:
                    tkinter.messagebox.showerror(
                        "Error", "Invalid username/password", parent=self.root
                    )
                elif user[0] == "Admin":
                    eid = user[1]
                    from dashboard import Dashboard

                    self.root.destroy()
                    app = Dashboard(eid)
                    app.mainloop()
                else:
                    eid = user[1]
                    from edashboard import EDashboard

                    self.root.destroy()
                    app = EDashboard(eid)
                    app.mainloop()

        except IOError as ex:
            tkinter.messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root
            )


if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = LoginSystem(root)
    root.mainloop()
