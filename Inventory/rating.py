"""Import required modules"""
from tkinter import *
import sqlite3
from tkinter import ttk, messagebox
from datetime import date
import customtkinter
from logins import LoginSystem


class Rating:
    """Rate employee"""

    def __init__(self, root, eid):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.resizable(True, True)
        self.root.config(bg="black")

        # All Varialble
        self.var_eid = StringVar()
        self.var_emp_date = StringVar()
        self.var_emp_name = StringVar()
        self.var_emp_salary = StringVar()
        self.var_emp_utype = StringVar()
        self.var_emp_rating = StringVar()
        self.value1 = IntVar()
        self.value2 = IntVar()
        self.value3 = IntVar()
        self.value4 = IntVar()

        style = ttk.Style()
        style.configure(
            "mystyle.Treeview",
            highlightthickness=0,
            bd=0,
            font=("Calibri", 11),
            background="black",
            fieldbackground="black",
            foreground="white",
        )
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
            self.root, textvariable=self.var_eid, style="mystyle1.TLabel"
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

        self.ps_label = ttk.Label(
            master=self.root, text="Problem Solving", style="mystyle1.TLabel"
        )
        self.ps_label.place(x=560, y=240)

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

        # Employee Details
        self.emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        self.emp_frame.place(x=0, y=350, relwidth=1, height=150)

        scrolly = Scrollbar(self.emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(self.emp_frame, orient=HORIZONTAL)

        self.employee_table = ttk.Treeview(
            self.emp_frame,
            columns=("eid", "name", "salary", "absent_days", "present_days", "fsalary"),
            yscrollcommand=scrolly.set,
            xscrollcommand=scrollx.set,
            style="mystyle.Treeview",
        )
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.employee_table.xview)
        scrolly.config(command=self.employee_table.yview)
        self.employee_table.heading("eid", text="EMP ID")
        self.employee_table.heading("name", text="Name")
        self.employee_table.heading("salary", text="Salary")
        self.employee_table.heading("absent_days", text="Absent Days")
        self.employee_table.heading("present_days", text="Present Days")
        self.employee_table.heading("fsalary", text="Final Salary")
        self.employee_table["show"] = "headings"

        self.employee_table.column("eid", width=90)
        self.employee_table.column("name", width=100)
        self.employee_table.column("salary", width=100)
        self.employee_table.column("absent_days", width=100)
        self.employee_table.column("present_days", width=100)
        self.employee_table.column("fsalary", width=100)

        self.employee_table.pack(fill=BOTH, expand=1)

        self.employee_table.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def tvalue(self, eid):
        """Calculate total rating"""
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        value = (
            self.value1.get()
            + self.value2.get()
            + self.value3.get()
            + self.value4.get()
        )
        fvalue = (value / 20) * 8
        dvalue = date.today().strftime("%m/%d/%y")
        try:

            cur.execute(
                "Select rdate from rating where eid=? and ratedby IS NOT NULL ORDER BY rid DESC",
                (str(self.var_eid.get())),
            )
            row = cur.fetchone()
            if row is None or (row[0] != dvalue):
                cur.execute(
                    "Insert into rating (rdate,eid,rate,ratedby) values(?,?,?,?)",
                    (dvalue, self.var_eid.get(), fvalue, eid),
                )
                con.commit()
                messagebox.showinfo(
                    "Success", "Employee Updated Sucessfully", parent=self.root
                )
            else:
                messagebox.showerror(
                    "Error", "You have already rated for today", parent=self.root
                )
            self.show()

        except (IOError, TypeError) as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        """Show values on table"""
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute(
                "Select eid,name,email,dob,contact,utype,salary from employee where utype!='Admin'"
            )
            rows = cur.fetchall()
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert("", END, values=row)

        except (IOError, TypeError) as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, _ev):
        """Get data from table"""
        _f = self.employee_table.focus()
        content = self.employee_table.item(_f)
        row = content["values"]
        today = date.today()
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()

        try:
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

            self.var_eid.set(row[0])
            self.var_emp_name.set(row[1])
            self.var_emp_date.set(today)
            self.var_emp_utype.set(row[5])
            self.var_emp_salary.set(row[6])
            self.var_emp_rating.set(value)

        except (IOError, TypeError) as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = LoginSystem(root)
    root.mainloop()
