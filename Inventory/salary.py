from curses.textpad import Textbox
from tkinter import *
import sqlite3
from tkinter import ttk, messagebox
from datetime import *
from calendar import monthrange

from numpy import ScalarType
from logins import Login_system
import customtkinter


class salaryClass:
    """Manage salary of employees"""

    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x550+220+80")
        self.root.resizable(True, True)
        self.root.title("Employee Management System")
        self.root.config(bg="black")
        # All Varialble

        self.var_emp_id = StringVar()
        self.var_emp_date = StringVar()
        self.var_emp_contact = StringVar()
        self.var_emp_name = StringVar()
        self.var_emp_email = StringVar()
        self.var_emp_salary = StringVar()
        self.var_emp_utype = StringVar()
        self.var_emp_remark = StringVar()
        self.var_emp_present = StringVar()
        self.var_emp_absent = StringVar()
        self.var_emp_holiday = StringVar()
        self.var_emp_bonus = StringVar()
        self.var_emp_rating = StringVar()
        self.var_emp_tsalary = StringVar()
        self.var_sremark = StringVar()

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
            text="Salary Details",
            font=("goudy old style", 11),
            bg="#0f4d7d",
            fg="white",
        ).place(x=50, y=100, width=1000)

        # #contents
        # row 1
<<<<<<< HEAD
        self.lbl_empid = ttk.Label(
            self.root,
            text="Emp ID",
            style="mystyle1.TLabel"
        ).place(x=50, y=150)
        self.lbl_name = ttk.Label(
            self.root, text="Name",style="mystyle1.TLabel"

        ).place(x=350, y=150)
        self.lbl_email = ttk.Label(
            self.root,
            text="Email",
            style="mystyle1.TLabel"
        ).place(x=750, y=150)

        self.txt_empid = ttk.Label(
            self.root,
            textvariable=self.var_emp_id,
            style="mystyle1.TLabel"
        ).place(x=150, y=150, width=180)
        self.txt_name = ttk.Label(
            self.root,
            textvariable=self.var_emp_name,
            style="mystyle1.TLabel"
        ).place(x=500, y=150, width=180)
        self.txt_email = ttk.Label(
            self.root,
            textvariable=self.var_emp_email,
            style="mystyle1.TLabel"
        ).place(x=850, y=150, width=180)

        # row 2
        self.lbl_date = ttk.Label(
            self.root, text="Date",style="mystyle1.TLabel"

        ).place(x=50, y=190)
        self.lbl_salary = ttk.Label(
            self.root,
            text="Salary",
            style="mystyle1.TLabel"
        ).place(x=350, y=190)
        self.lbl_utype = ttk.Label(
            self.root,
            text="User Type",
            style="mystyle1.TLabel"
        ).place(x=750, y=190)

        self.txt_name = ttk.Label(
            self.root,
            textvariable=self.var_emp_date,
            style="mystyle1.TLabel"
        ).place(x=150, y=190, width=180)
        self.txt_salary = ttk.Label(
            self.root,
            textvariable=self.var_emp_salary,
            style="mystyle1.TLabel"
=======
        lbl_empid = ttk.Label(self.root, text="Emp ID", style="mystyle1.TLabel").place(
            x=50, y=150
        )
        lbl_name = ttk.Label(self.root, text="Name", style="mystyle1.TLabel").place(
            x=350, y=150
        )
        lbl_email = ttk.Label(self.root, text="Email", style="mystyle1.TLabel").place(
            x=750, y=150
        )

        txt_empid = ttk.Label(
            self.root, textvariable=self.var_emp_id, style="mystyle1.TLabel"
        ).place(x=150, y=150, width=180)
        txt_name = ttk.Label(
            self.root, textvariable=self.var_emp_name, style="mystyle1.TLabel"
        ).place(x=500, y=150, width=180)
        txt_email = ttk.Label(
            self.root, textvariable=self.var_emp_email, style="mystyle1.TLabel"
        ).place(x=850, y=150, width=180)

        # row 2
        lbl_date = ttk.Label(self.root, text="Date", style="mystyle1.TLabel").place(
            x=50, y=190
        )
        lbl_salary = ttk.Label(self.root, text="Salary", style="mystyle1.TLabel").place(
            x=350, y=190
        )
        lbl_utype = ttk.Label(
            self.root, text="User Type", style="mystyle1.TLabel"
        ).place(x=750, y=190)

        txt_name = ttk.Label(
            self.root, textvariable=self.var_emp_date, style="mystyle1.TLabel"
        ).place(x=150, y=190, width=180)
        txt_salary = ttk.Label(
            self.root, textvariable=self.var_emp_salary, style="mystyle1.TLabel"
>>>>>>> b707e97b366ec3f49e8d6e0efd90c3e9f87e28b9
        ).place(x=500, y=190, width=180)
        self.txt_utype = ttk.Label(
            self.root,
            textvariable=self.var_emp_utype,
            justify=CENTER,
            style="mystyle1.TLabel",
        ).place(x=850, y=190, width=180)

        # row 3
        # ====row4=======
<<<<<<< HEAD
        self.lbl_present = ttk.Label(
            self.root,
            text="Present Days",
            style="mystyle1.TLabel"
        ).place(x=50, y=230)
        self.lbl_absent = ttk.Label(
            self.root,
            text="Absent Days",
            style="mystyle1.TLabel"
        ).place(x=350, y=230)
        self.lbl_holiday = ttk.Label(
            self.root,
            text="Holiday",
            style="mystyle1.TLabel"
        ).place(x=750, y=230)

        self.txt_present = ttk.Label(
            self.root,
            textvariable=self.var_emp_present,
            style="mystyle1.TLabel"
        ).place(x=150, y=230, width=180)
        self.txt_absent = ttk.Label(
            self.root,
            textvariable=self.var_emp_absent,
            style="mystyle1.TLabel"
=======
        lbl_present = ttk.Label(
            self.root, text="Present Days", style="mystyle1.TLabel"
        ).place(x=50, y=230)
        lbl_absent = ttk.Label(
            self.root, text="Absent Days", style="mystyle1.TLabel"
        ).place(x=350, y=230)
        lbl_holiday = ttk.Label(
            self.root, text="Holiday", style="mystyle1.TLabel"
        ).place(x=750, y=230)

        txt_present = ttk.Label(
            self.root, textvariable=self.var_emp_present, style="mystyle1.TLabel"
        ).place(x=150, y=230, width=180)
        txt_absent = ttk.Label(
            self.root, textvariable=self.var_emp_absent, style="mystyle1.TLabel"
>>>>>>> b707e97b366ec3f49e8d6e0efd90c3e9f87e28b9
        ).place(x=500, y=230, width=180)
        self.txt_holiday = Entry(
            self.root,
            textvariable=self.var_emp_holiday,
            insertbackground="white",
            font=("goudy old style", 11),
            background="#211f1f",
            foreground="white",
        ).place(x=850, y=230, width=180)

        # row 4
<<<<<<< HEAD
        self.lbl_rating = ttk.Label(
            self.root,
            text="Rating",
            style="mystyle1.TLabel"
        ).place(x=50, y=270)
        self.lbl_bonus = ttk.Label(
            self.root,
            text="Bonus",
            style="mystyle1.TLabel"
        ).place(x=350, y=270)
        self.lbl_tsalary = ttk.Label(
            self.root,
            text="Total Salary",
            style="mystyle1.TLabel"
        ).place(x=750, y=270)

        self.txt_rating = ttk.Label(
            self.root,
            textvariable=self.var_emp_rating,
            style="mystyle1.TLabel"
        ).place(x=150, y=270, width=180)
        self.txt_bonus = ttk.Label(
            self.root,
            textvariable=self.var_emp_bonus,
            style="mystyle1.TLabel"
=======
        lbl_rating = ttk.Label(self.root, text="Rating", style="mystyle1.TLabel").place(
            x=50, y=270
        )
        lbl_bonus = ttk.Label(self.root, text="Bonus", style="mystyle1.TLabel").place(
            x=350, y=270
        )
        lbl_tsalary = ttk.Label(
            self.root, text="Total Salary", style="mystyle1.TLabel"
        ).place(x=750, y=270)

        txt_rating = ttk.Label(
            self.root, textvariable=self.var_emp_rating, style="mystyle1.TLabel"
        ).place(x=150, y=270, width=180)
        txt_bonus = ttk.Label(
            self.root, textvariable=self.var_emp_bonus, style="mystyle1.TLabel"
>>>>>>> b707e97b366ec3f49e8d6e0efd90c3e9f87e28b9
        ).place(x=500, y=270, width=180)
        self.txt_tsalary = ttk.Label(
            self.root,
            textvariable=self.var_emp_tsalary,
            justify=CENTER,
            style="mystyle1.TLabel",
        ).place(x=850, y=270, width=180)

        # row 5
<<<<<<< HEAD
        self.lbl_remark = ttk.Label(
            self.root,
            text="Remark",
            style="mystyle1.TLabel"
        ).place(x=50, y=310)
        
=======
        lbl_remark = ttk.Label(self.root, text="Remark", style="mystyle1.TLabel").place(
            x=50, y=310
        )

>>>>>>> b707e97b366ec3f49e8d6e0efd90c3e9f87e28b9
        self.var_sremark = Text(
            self.root,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
            insertbackground="white",
        )
        self.var_sremark.place(x=150, y=310, width=180, height=70)

        # button
        self.btn_calculate = customtkinter.CTkButton(
            self.root,
            text="Calculate",
            command=self.calculate,
            text_font=("goudy old style", 11),
            fg_color="#4caf50",
            cursor="hand2",
        ).place(x=440, y=355, width=180, height=28)

        self.btn_approve = customtkinter.CTkButton(
            self.root,
            text="Approve",
            command=self.approve,
            text_font=("goudy old style", 11),
            fg_color="blue",
            cursor="hand2",
        ).place(x=645, y=355, width=180, height=28)

        self.btn_pay = customtkinter.CTkButton(
            self.root,
            text="Pay",
            command=self.pay,
            text_font=("goudy old style", 11),
            fg_color="red",
            cursor="hand2",
        ).place(x=850, y=355, width=180, height=28)

        # Employee Details
        self.emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        self.emp_frame.place(x=0, y=400, relwidth=1, height=150)

        scrolly = Scrollbar(self.emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(self.emp_frame, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(
            self.emp_frame,
            columns=("eid", "name", "salary", "absent_days", "present_days", "fsalary"),
            yscrollcommand=scrolly.set,
            xscrollcommand=scrollx.set,
            style="mystyle.Treeview",
        )
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("eid", text="EMP ID")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("salary", text="Salary")
        self.EmployeeTable.heading("absent_days", text="Absent Days")
        self.EmployeeTable.heading("present_days", text="Present Days")
        self.EmployeeTable.heading("fsalary", text="Final Salary")
        self.EmployeeTable["show"] = "headings"

        self.EmployeeTable.column("eid", width=90)
        self.EmployeeTable.column("name", width=100)
        self.EmployeeTable.column("salary", width=100)
        self.EmployeeTable.column("absent_days", width=100)
        self.EmployeeTable.column("present_days", width=100)
        self.EmployeeTable.column("fsalary", width=100)

        self.EmployeeTable.pack(fill=BOTH, expand=1)

        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def show(self):
        """Show data on table"""
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        today = date.today()
<<<<<<< HEAD
        dvalue=today.strftime("%m/%y")
=======
        dvalue = today.strftime("%m/%y")
        eid = 2
>>>>>>> b707e97b366ec3f49e8d6e0efd90c3e9f87e28b9
        try:
            cur.execute(
                "Select eid,name,email,contact,utype,salary from employee where utype!='Admin' and eid!=(select eid from salary where sstatus=? and sdate LIKE ?)",
                ("paid", "%" + dvalue + "%"),
            )
            rows = cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        """Get data from table"""
        self.clear()
        f = self.EmployeeTable.focus()
        content = self.EmployeeTable.item(f)
        row = content["values"]
        today = date.today()
        dvalue = today.strftime("%m/%y")
        num_days = monthrange(today.year, today.month)
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()

        try:
            cur.execute(
                "Select count(*) from attendance where eid=? and astatus='present' and date LIKE ?",
                (str(row[0]), "%" + dvalue + "%"),
            )
            rows = cur.fetchone()
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

        except Exception as ex:
            value = 0
            messagebox.showerror("Error", f"Employee not rated", parent=self.root)

        self.var_emp_id.set(row[0]),
        self.var_emp_name.set(row[1]),
        self.var_emp_email.set(row[2]),
        self.var_emp_date.set(date.today().strftime("%d/%m/%y")),
        self.var_emp_contact.set(row[3]),
        self.var_emp_utype.set(row[4]),
        self.var_emp_salary.set(row[5]),
        self.var_emp_absent.set(int(num_days[1]) - int(rows[0]))
        self.var_emp_present.set(rows[0])
        self.var_emp_rating.set(value)

    def approve(self):
        """Approve salary"""
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_emp_tsalary.get() == "":
                messagebox.showerror(
                    "Error", "Calculate Salary First", parent=self.root
                )
            else:
                cur.execute(
                    "Insert into salary (fsalary,sdate,sstatus,eid,holiday,bonus) values(?,?,?,?,?,?)",
                    (
                        self.var_emp_tsalary.get(),
                        self.var_emp_date.get(),
                        "pending",
                        self.var_emp_id.get(),
                        self.var_emp_holiday.get(),
                        self.var_emp_bonus.get(),
                    ),
                )
                con.commit()
                messagebox.showinfo(
                    "Success", "Employee Updated Sucessfully", parent=self.root
                )
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def calculate(self):
        """Calculate salary"""
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Select employee", parent=self.root)
            else:
                if self.var_emp_holiday.get() == "":
                    messagebox.showerror(
                        "Error", "Enter no of holiday employee", parent=self.root
                    )
                else:
                    today = date.today()
                    num_days = monthrange(today.year, today.month)
                    salary = (int(self.var_emp_salary.get()) // num_days[1]) * (
                        int(self.var_emp_present.get())
                        + int(self.var_emp_holiday.get())
                    )
                    bonus = (
                        float(self.var_emp_rating.get())
                        * int(self.var_emp_salary.get())
                        / 100
                    )
                    self.var_emp_tsalary.set(int(salary + bonus))
                    self.var_emp_bonus.set(int(bonus))
                    messagebox.showinfo(
                        "Success", "Salary Calculated", parent=self.root
                    )
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def pay(self):
        """Approve salary"""
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        today = date.today()
        dvalue = today.strftime("%m/%y")
        cur.execute(
            "Select sstatus from salary where eid=? and sdate LIKE ?",
            (self.var_emp_id.get(), "%" + dvalue + "%"),
        )
        rows = cur.fetchone()
        if rows[0] == "approved":
            try:
                cur.execute(
                    "update salary set sstatus='paid' where eid=?",
                    self.var_emp_id.get(),
                )
                con.commit()
                messagebox.showinfo("Success", "Salary Paid", parent=self.root)

            except Exception as ex:
                messagebox.showerror(
                    "Error", f"Error due to : {str(ex)}", parent=self.root
                )
        else:
            messagebox.showerror("Error", f"Salary not approved", parent=self.root)

    def clear(self):
        """Clear Table"""
        self.var_emp_holiday.set(""),
        self.var_emp_bonus.set(""),
        self.var_emp_tsalary.set(""),


if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = Login_system(root)
    root.mainloop()
