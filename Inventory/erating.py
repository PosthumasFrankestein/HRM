"""Import required module"""
from tkinter import *
import sqlite3
from tkinter import messagebox, ttk
from datetime import date
import customtkinter
from logins import LoginSystem


class EmpRate:
    """Rate yourself"""

    def __init__(self, root, eid):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.resizable(True, True)
        self.root.config(bg="black")
        self.var_emp_id = StringVar()
        self.var_emp_date = StringVar()
        self.var_emp_contact = StringVar()
        self.var_emp_name = StringVar()
        self.var_emp_email = StringVar()
        self.var_emp_salary = StringVar()
        self.var_emp_utype = StringVar()
        self.var_emp_rating = StringVar()
        self.var_emp_tsalary = StringVar()
        self.value1 = IntVar()
        self.value2 = IntVar()
        self.value3 = IntVar()
        self.value4 = IntVar()
        style = ttk.Style()
        style.configure(
            "mystyle1.TLabel",
            font=("goudy old style", 11),
            background="#211f1f",
            foreground="white",
            anchor=CENTER,
        )

        self.title = Label(
            self.root,
            text="Rating System",
            font=("goudy old style", 11),
            bg="#0f4d7d",
            fg="white",
        )
        self.title.place(x=50, y=100, width=1000)

        # #contents
        # row 1
        self.lbl_empid = ttk.Label(self.root, text="Emp ID", style="mystyle1.TLabel")
        self.lbl_empid.place(x=50, y=150)

        self.lbl_name = ttk.Label(self.root, text="Name", style="mystyle1.TLabel")
        self.lbl_name.place(x=350, y=150)

        self.lbl_utype = ttk.Label(self.root, text="User Type", style="mystyle1.TLabel")
        self.lbl_utype.place(x=750, y=150)

        self.txt_empid = ttk.Label(
            self.root, textvariable=self.var_emp_id, style="mystyle1.TLabel"
        )
        self.txt_empid.place(x=150, y=150, width=180)

        self.txt_name = ttk.Label(
            self.root, textvariable=self.var_emp_name, style="mystyle1.TLabel"
        )
        self.txt_name.place(x=500, y=150, width=180)

        self.txt_utype = ttk.Label(
            self.root, textvariable=self.var_emp_utype, style="mystyle1.TLabel"
        )
        self.txt_utype.place(x=850, y=150, width=180)

        # row 2
        self.lbl_date = ttk.Label(self.root, text="Date", style="mystyle1.TLabel")
        self.lbl_date.place(x=50, y=190)

        self.lbl_salary = ttk.Label(self.root, text="Salary", style="mystyle1.TLabel")
        self.lbl_salary.place(x=350, y=190)

        self.lbl_rating = ttk.Label(
            self.root, text="Avg Rating", style="mystyle1.TLabel"
        )
        self.lbl_rating.place(x=750, y=190)

        self.txt_name = ttk.Label(
            self.root, textvariable=self.var_emp_date, style="mystyle1.TLabel"
        )
        self.txt_name.place(x=150, y=190, width=180)

        self.txt_salary = ttk.Label(
            self.root, textvariable=self.var_emp_salary, style="mystyle1.TLabel"
        )
        self.txt_salary.place(x=500, y=190, width=180)

        self.txt_rating = ttk.Label(
            self.root, textvariable=self.var_emp_rating, style="mystyle1.TLabel"
        )
        self.txt_rating.place(x=850, y=190, width=180)

        # row 3
        # ====row4=======
        self.collab_label = ttk.Label(
            self.root, text="Collaboration", style="mystyle1.TLabel"
        )
        self.collab_label.place(x=50, y=240)

        self.slider1 = customtkinter.CTkSlider(
            master=self.root,
            width=320,
            from_=0,
            to=5,
            number_of_steps=5,
            variable=self.value1,
        )
        self.slider1.place(x=190, y=245)

        self.prob_label = ttk.Label(
            master=self.root, text="Problem Solving", style="mystyle1.TLabel"
        )
        self.prob_label.place(x=560, y=240)

        self.slider2 = customtkinter.CTkSlider(
            master=self.root,
            from_=0,
            width=320,
            to=5,
            number_of_steps=5,
            variable=self.value2,
        )
        self.slider2.place(x=720, y=245)

        self.know_label = ttk.Label(
            master=self.root, text="Knowledge/Skills", style="mystyle1.TLabel"
        )
        self.know_label.place(x=50, y=280)

        self.slider3 = customtkinter.CTkSlider(
            master=self.root,
            from_=0,
            width=320,
            to=5,
            number_of_steps=5,
            variable=self.value3,
        )
        self.slider3.place(x=190, y=285)

        self.cs_label = ttk.Label(
            master=self.root, text="Customer service", style="mystyle1.TLabel"
        )
        self.cs_label.place(x=560, y=280)

        self.slider4 = customtkinter.CTkSlider(
            master=self.root,
            from_=0,
            to=5,
            width=320,
            number_of_steps=5,
            variable=self.value4,
        )
        self.slider4.place(x=720, y=285)

        self.button = customtkinter.CTkButton(
            master=self.root,
            border_width=0,
            corner_radius=8,
            fg_color="green",
            text="Rate",
            command=lambda: self.tvalue(eid),
            text_font=("goudy old style", 11),
        )
        self.button.place(x=850, y=310, width=180, height=28)
        self.get_data(eid)

    def tvalue(self, eid):
        """Get total rating value"""
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        value = (
            self.value1.get()
            + self.value2.get()
            + self.value3.get()
            + self.value4.get()
        )
        fvalue = (value / 20) * 2
        dvalue = date.today().strftime("%m/%d/%y")
        try:
            cur.execute(
                "Select rdate from rating where eid=? and ratedby is NULL ORDER BY rid DESC",
                (str(eid)),
            )
            row = cur.fetchone()
            if row is None or (row[0] != dvalue):
                cur.execute(
                    "Insert into rating (rdate,eid,rate) values(?,?,?)",
                    (dvalue, eid, fvalue),
                )
                con.commit()
                messagebox.showinfo(
                    "Success", "Employee Updated Sucessfully", parent=self.root
                )
            else:
                messagebox.showerror(
                    "Error", "You have already rated for today", parent=self.root
                )

        except (IOError, TypeError) as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, eid):
        """Get data from database"""
        today = date.today()
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()

        try:
            cur.execute(
                "Select eid,name,utype,doj,salary from employee where eid=?", str(eid)
            )
            row = cur.fetchone()
            cur.execute(
                "Select count(*),sum(rate) from rating where eid=? and ratedby IS NOT NULL",
                (str(row[0])),
            )
            rows1 = cur.fetchone()
            cur.execute(
                "Select count(*),sum(rate) from rating where eid=? and ratedby IS NULL",
                (str(row[0])),
            )
            rows2 = cur.fetchone()
            if rows1[1] is None and rows2[1] is None:
                value = 0
            elif rows1[1] is None and rows2[1] is not None:
                value = rows1[1] / rows1[0]
            elif rows1[1] is None and rows2[1] is not None:
                value = rows2[1] / rows2[0]
            else:
                value = (rows1[1] / rows1[0]) + (rows2[1] / rows2[0])

            self.var_emp_id.set(row[0])
            self.var_emp_name.set(row[1])
            self.var_emp_utype.set(row[2])
            self.var_emp_date.set(today)
            self.var_emp_salary.set(row[4])
            self.var_emp_rating.set(value)

        except (IOError, TypeError) as ex:
            messagebox.showerror(
                "Error", f"Error here due to : {str(ex)}", parent=self.root
            )


if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = LoginSystem(root)
    root.mainloop()
