from tkinter import *
import sqlite3
from tkinter import messagebox
from datetime import *
from calendar import monthrange
import customtkinter
from logins import Login_system


class esalaryClass:
    """Check salary"""

    def __init__(self, root, eid):
        self.root = root
        self.root.geometry("1100x450+220+80")
        self.root.resizable(True, True)
        self.root.title("Employee Management System")
        self.root.config(bg="black")

        self.var_emp_id = StringVar()
        self.var_emp_date = StringVar()
        self.var_emp_contact = StringVar()
        self.var_emp_name = StringVar()
        self.var_emp_email = StringVar()
        self.var_emp_salary = StringVar()
        self.var_emp_utype = StringVar()
        self.var_emp_present = StringVar()
        self.var_emp_absent = StringVar()
        self.var_emp_holiday = StringVar()
        self.var_emp_bonus = StringVar()
        self.var_emp_rating = StringVar()
        self.var_emp_tsalary = StringVar()

        title = Label(
            self.root,
            text="Salary Details",
            font=("goudy old style", 11),
            bg="#0f4d7d",
            fg="white",
        ).place(x=50, y=100, width=1000)

        # #contents
        # row 1
        lbl_empid = Label(
            self.root,
            text="Emp ID",
            font=("goudy old style", 11),
            bg="black",
            fg="white",
        ).place(x=50, y=150)
        lbl_name = Label(
            self.root, text="Name", font=("goudy old style", 11), bg="black", fg="white"
        ).place(x=350, y=150)
        lbl_email = Label(
            self.root,
            text="Email",
            font=("goudy old style", 11),
            bg="black",
            fg="white",
        ).place(x=750, y=150)

        txt_empid = Label(
            self.root,
            textvariable=self.var_emp_id,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
        ).place(x=150, y=150, width=180)
        txt_name = Label(
            self.root,
            textvariable=self.var_emp_name,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
        ).place(x=500, y=150, width=180)
        txt_email = Label(
            self.root,
            textvariable=self.var_emp_email,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
        ).place(x=850, y=150, width=180)

        # row 2
        lbl_date = Label(
            self.root, text="Date", font=("goudy old style", 11), bg="black", fg="white"
        ).place(x=50, y=190)
        lbl_salary = Label(
            self.root,
            text="Salary",
            font=("goudy old style", 11),
            bg="black",
            fg="white",
        ).place(x=350, y=190)
        lbl_utype = Label(
            self.root,
            text="User Type",
            font=("goudy old style", 11),
            bg="black",
            fg="white",
        ).place(x=750, y=190)

        txt_name = Label(
            self.root,
            textvariable=self.var_emp_date,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
        ).place(x=150, y=190, width=180)
        txt_salary = Label(
            self.root,
            textvariable=self.var_emp_salary,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
        ).place(x=500, y=190, width=180)
        txt_utype = Label(
            self.root,
            textvariable=self.var_emp_utype,
            justify=CENTER,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
        ).place(x=850, y=190, width=180)

        # row 3
        # ====row4=======
        lbl_present = Label(
            self.root,
            text="Present Days",
            font=("goudy old style", 11),
            bg="black",
            fg="white",
        ).place(x=50, y=230)
        lbl_absent = Label(
            self.root,
            text="Absent Days",
            font=("goudy old style", 11),
            bg="black",
            fg="white",
        ).place(x=350, y=230)
        lbl_holiday = Label(
            self.root,
            text="Holiday",
            font=("goudy old style", 11),
            bg="black",
            fg="white",
        ).place(x=750, y=230)

        txt_present = Label(
            self.root,
            textvariable=self.var_emp_present,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
        ).place(x=150, y=230, width=180)
        txt_absent = Label(
            self.root,
            textvariable=self.var_emp_absent,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
        ).place(x=500, y=230, width=180)
        txt_holiday = Label(
            self.root,
            textvariable=self.var_emp_holiday,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
        ).place(x=850, y=230, width=180)

        # row 4
        lbl_rating = Label(
            self.root,
            text="Rating",
            font=("goudy old style", 11),
            bg="black",
            fg="white",
        ).place(x=50, y=270)
        lbl_bonus = Label(
            self.root,
            text="Bonus",
            font=("goudy old style", 11),
            bg="black",
            fg="white",
        ).place(x=350, y=270)
        lbl_tsalary = Label(
            self.root,
            text="Total Salary",
            font=("goudy old style", 11),
            bg="black",
            fg="white",
        ).place(x=750, y=270)

        txt_rating = Label(
            self.root,
            textvariable=self.var_emp_rating,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
        ).place(x=150, y=270, width=180)
        txt_bonus = Label(
            self.root,
            textvariable=self.var_emp_bonus,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
        ).place(x=500, y=270, width=180)
        txt_tsalary = Label(
            self.root,
            textvariable=self.var_emp_tsalary,
            justify=CENTER,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
        ).place(x=850, y=270, width=180)

        # row 5
        lbl_remark = Label(
            self.root,
            text="Remark",
            font=("goudy old style", 11),
            bg="black",
            fg="white",
        ).place(x=50, y=310)

        self.var_sremark = Text(
            self.root,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
            insertbackground="white",
        )
        self.var_sremark.place(x=150, y=310, width=180, height=80)

        # button
        btn_approve = customtkinter.CTkButton(
            self.root,
            text="Approve",
            command=lambda: self.approve(eid),
            text_font=("goudy old style", 11),
            fg_color="#4caf50",
            cursor="hand2",
        ).place(x=645, y=395, width=180, height=28)

        btn_reappeal = customtkinter.CTkButton(
            self.root,
            text="Re-appeal",
            command=lambda: self.reappeal(eid),
            text_font=("goudy old style", 11),
            fg_color="blue",
            cursor="hand2",
        ).place(x=850, y=395, width=180, height=28)

        self.get_data(eid)

    def get_data(self, eid):
        """Get data"""
        today = date.today()
        dvalue = today.strftime("%m/%y")
        num_days = monthrange(today.year, today.month)
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        cur.execute(
            "Select eid,name,email,dob,contact,utype,salary from employee where eid=?",
            str(eid),
        )
        row = cur.fetchone()

        cur.execute(
            "Select holiday,bonus,fsalary,sremark,sstatus from salary where eid=? and sdate like ?",
            (str(eid), "%" + dvalue + "%"),
        )
        row1 = cur.fetchone()
        if row1 is None:
            messagebox.showerror(
                "Error", f"Salary for this month not released", parent=self.root
            )
        elif row1[4] == "approved":
            messagebox.showerror(
                "Error", f"Salary for this month already approved", parent=self.root
            )
        else:
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

                self.var_emp_id.set(row[0]),
                self.var_emp_name.set(row[1]),
                self.var_emp_email.set(row[2]),
                self.var_emp_date.set(row[3]),
                self.var_emp_contact.set(row[4]),
                self.var_emp_utype.set(row[5]),
                self.var_emp_salary.set(row[6]),
                self.var_emp_absent.set(int(num_days[1]) - int(rows[0]))
                self.var_emp_present.set(rows[0]),
                self.var_emp_rating.set(value),
                self.var_emp_holiday.set(row1[0]),
                self.var_emp_bonus.set(row1[1]),
                self.var_emp_tsalary.set(row1[2]),
                if row1[3] is not None:
                    self.var_sremark.insert(END, row1[3]),

            except Exception as ex:
                messagebox.showerror(
                    "Error", f"Error due to : {str(ex)}", parent=self.root
                )

    def approve(self, eid):
        """Approve salary"""
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute("update salary set sstatus='approved' where eid=?", str(eid))
            con.commit()
            messagebox.showinfo("Success", "Salary Approved", parent=self.root)
            self.get_data(self, eid)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def reappeal(self, eid):
        """Reappeal for the salary"""
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute(
                "update salary set sstatus='pending',sremark=? where eid=?",
                (self.var_sremark.get("1.0", END), str(eid)),
            )
            con.commit()
            messagebox.showinfo("Success", "Salary Reappealed", parent=self.root)
            self.get_data(self, eid)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = Login_system(root)
    root.mainloop()
