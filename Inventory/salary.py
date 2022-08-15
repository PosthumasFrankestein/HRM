"""Import required modules"""
from tkinter import *
import sqlite3
from tkinter import ttk, messagebox
from datetime import date
from calendar import monthrange
from logins import LoginSystem
import customtkinter


class SalaryClass:
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
        )
        self.title.place(x=50, y=100, width=1000)

        # #contents
        # row 1
        self.lbl_empid = ttk.Label(self.root, text="Emp ID", style="mystyle1.TLabel")
        self.lbl_empid.place(x=50, y=150)

        self.lbl_name = ttk.Label(self.root, text="Name", style="mystyle1.TLabel")
        self.lbl_name.place(x=350, y=150)

        self.lbl_email = ttk.Label(self.root, text="Email", style="mystyle1.TLabel")
        self.lbl_email.place(x=750, y=150)

        self.txt_empid = ttk.Label(
            self.root, textvariable=self.var_emp_id, style="mystyle1.TLabel"
        )
        self.txt_empid.place(x=150, y=150, width=180)

        self.txt_name = ttk.Label(
            self.root, textvariable=self.var_emp_name, style="mystyle1.TLabel"
        )
        self.txt_name.place(x=500, y=150, width=180)

        self.txt_email = ttk.Label(
            self.root, textvariable=self.var_emp_email, style="mystyle1.TLabel"
        )
        self.txt_email.place(x=850, y=150, width=180)

        # row 2
        self.lbl_date = ttk.Label(self.root, text="Date", style="mystyle1.TLabel")
        self.lbl_date.place(x=50, y=190)

        self.lbl_salary = ttk.Label(self.root, text="Salary", style="mystyle1.TLabel")
        self.lbl_salary.place(x=350, y=190)

        self.lbl_utype = ttk.Label(self.root, text="User Type", style="mystyle1.TLabel")
        self.lbl_utype.place(x=750, y=190)

        self.txt_name = ttk.Label(
            self.root, textvariable=self.var_emp_date, style="mystyle1.TLabel"
        )
        self.txt_name.place(x=150, y=190, width=180)

        self.txt_salary = ttk.Label(
            self.root, textvariable=self.var_emp_salary, style="mystyle1.TLabel"
        )
        self.txt_salary.place(x=500, y=190, width=180)

        self.txt_utype = ttk.Label(
            self.root,
            textvariable=self.var_emp_utype,
            justify=CENTER,
            style="mystyle1.TLabel",
        )
        self.txt_utype.place(x=850, y=190, width=180)

        # row 3
        # ====row4=======
        self.lbl_present = ttk.Label(
            self.root, text="Present Days", style="mystyle1.TLabel"
        )
        self.lbl_present.place(x=50, y=230)

        self.lbl_absent = ttk.Label(
            self.root, text="Absent Days", style="mystyle1.TLabel"
        )
        self.lbl_absent.place(x=350, y=230)

        self.lbl_holiday = ttk.Label(self.root, text="Holiday", style="mystyle1.TLabel")
        self.lbl_holiday.place(x=750, y=230)

        self.txt_present = ttk.Label(
            self.root, textvariable=self.var_emp_present, style="mystyle1.TLabel"
        )
        self.txt_present.place(x=150, y=230, width=180)

        self.txt_absent = ttk.Label(
            self.root, textvariable=self.var_emp_absent, style="mystyle1.TLabel"
        )
        self.txt_absent.place(x=500, y=230, width=180)

        self.txt_holiday = Entry(
            self.root,
            textvariable=self.var_emp_holiday,
            insertbackground="white",
            font=("goudy old style", 11),
            background="#211f1f",
            foreground="white",
        )
        self.txt_holiday.place(x=850, y=230, width=180)

        # row 4
        self.lbl_rating = ttk.Label(self.root, text="Rating", style="mystyle1.TLabel")
        self.lbl_rating.place(x=50, y=270)

        self.lbl_bonus = ttk.Label(self.root, text="Bonus", style="mystyle1.TLabel")
        self.lbl_bonus.place(x=350, y=270)

        self.lbl_tsalary = ttk.Label(
            self.root, text="Total Salary", style="mystyle1.TLabel"
        )
        self.lbl_tsalary.place(x=750, y=270)

        self.txt_rating = ttk.Label(
            self.root, textvariable=self.var_emp_rating, style="mystyle1.TLabel"
        )
        self.txt_rating.place(x=150, y=270, width=180)

        self.txt_bonus = ttk.Label(
            self.root, textvariable=self.var_emp_bonus, style="mystyle1.TLabel"
        )
        self.txt_bonus.place(x=500, y=270, width=180)

        self.txt_tsalary = ttk.Label(
            self.root,
            textvariable=self.var_emp_tsalary,
            justify=CENTER,
            style="mystyle1.TLabel",
        )
        self.txt_tsalary.place(x=850, y=270, width=180)

        # row 5
        self.lbl_remark = ttk.Label(self.root, text="Remark", style="mystyle1.TLabel")
        self.lbl_remark.place(x=50, y=310)

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
        )
        self.btn_calculate.place(x=440, y=355, width=180, height=28)

        self.btn_approve = customtkinter.CTkButton(
            self.root,
            text="Approve",
            command=self.approve,
            text_font=("goudy old style", 11),
            fg_color="blue",
            cursor="hand2",
        )
        self.btn_approve.place(x=645, y=355, width=180, height=28)

        self.btn_pay = customtkinter.CTkButton(
            self.root,
            text="Pay",
            command=self.pay,
            text_font=("goudy old style", 11),
            fg_color="red",
            cursor="hand2",
        )
        self.btn_pay.place(x=850, y=355, width=180, height=28)

        # Employee Details
        self.emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        self.emp_frame.place(x=0, y=400, relwidth=1, height=150)

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

    def show(self):
        """Show data on table"""
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        today = date.today()
        dvalue = today.strftime("%m/%y")
        try:
            cur.execute(
                "Select eid,name,email,contact,utype,salary"
                " from employee where utype!='Admin' and eid!="
                "(select eid from salary where sstatus=? and sdate LIKE ?)",
                ("paid", "%" + dvalue + "%"),
            )
            rows = cur.fetchall()
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert("", END, values=row)

        except (IOError, TypeError) as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, _ev):
        """Get data from table"""
        self.clear()
        _f = self.employee_table.focus()
        content = self.employee_table.item(_f)
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

        except (IOError, TypeError):
            messagebox.showerror("Error", "Employee not rated", parent=self.root)

        self.var_emp_id.set(row[0])
        self.var_emp_name.set(row[1])
        self.var_emp_email.set(row[2])
        self.var_emp_date.set(date.today().strftime("%d/%m/%y"))
        self.var_emp_contact.set(row[3])
        self.var_emp_utype.set(row[4])
        self.var_emp_salary.set(row[5])
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
                    "Insert into salary (fsalary,sdate,sstatus,eid,holiday,bonus)"
                    " values(?,?,?,?,?,?)",
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
        except (IOError, TypeError) as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def calculate(self):
        """Calculate salary"""
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
        except (IOError, TypeError) as ex:
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

            except (IOError, TypeError) as ex:
                messagebox.showerror(
                    "Error", f"Error due to : {str(ex)}", parent=self.root
                )
        else:
            messagebox.showerror("Error", "Salary not approved", parent=self.root)

    def clear(self):
        """Clear Table"""
        self.var_emp_holiday.set("")
        self.var_emp_bonus.set("")
        self.var_emp_tsalary.set("")


if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = LoginSystem(root)
    root.mainloop()
