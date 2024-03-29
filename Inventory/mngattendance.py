"""Import required modules"""
from tkinter import *
import sqlite3
from tkinter import ttk, messagebox
from logins import LoginSystem
import customtkinter


class AttendanceMng:
    """Manage Attendance class"""

    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Logged as Admin")
        self.root.config(bg="black")

        # All Varialble
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_emp_id = StringVar()
        self.var_emp_date = StringVar()
        self.var_emp_contact = StringVar()
        self.var_emp_name = StringVar()
        self.var_emp_email = StringVar()
        self.var_emp_utype = StringVar()
        self.var_emp_remark = StringVar()
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

        title = Label(
            self.root,
            text="Attendance Details",
            font=("goudy old style", 15),
            bg="#0f4d7d",
            fg="white",
        )
        title.place(x=50, y=100, width=1000)

        # #contents
        # row 1
        lbl_empid = ttk.Label(self.root, text="Emp ID", style="mystyle1.TLabel")
        lbl_empid.place(x=50, y=150)

        lbl_date = ttk.Label(self.root, text="Date", style="mystyle1.TLabel")
        lbl_date.place(x=350, y=150)

        lbl_contact = ttk.Label(self.root, text="Contact", style="mystyle1.TLabel")
        lbl_contact.place(x=750, y=150)

        txt_empid = ttk.Label(
            self.root, textvariable=self.var_emp_id, style="mystyle1.TLabel"
        )
        txt_empid.place(x=150, y=150, width=180)

        txt_date = ttk.Label(
            self.root, textvariable=self.var_emp_date, style="mystyle1.TLabel"
        )
        txt_date.place(x=500, y=150, width=180)

        txt_contact = ttk.Label(
            self.root, textvariable=self.var_emp_contact, style="mystyle1.TLabel"
        )
        txt_contact.place(x=850, y=150, width=180)

        # row 2
        lbl_name = ttk.Label(self.root, text="Name", style="mystyle1.TLabel")
        lbl_name.place(x=50, y=190)

        lbl_email = ttk.Label(self.root, text="Email", style="mystyle1.TLabel")
        lbl_email.place(x=350, y=190)

        lbl_doj = ttk.Label(self.root, text="User Type", style="mystyle1.TLabel")
        lbl_doj.place(x=750, y=190)

        txt_name = ttk.Label(
            self.root, textvariable=self.var_emp_name, style="mystyle1.TLabel"
        )
        txt_name.place(x=150, y=190, width=180)

        txt_email = ttk.Label(
            self.root, textvariable=self.var_emp_email, style="mystyle1.TLabel"
        )
        txt_email.place(x=500, y=190, width=180)

        cmb_utype = ttk.Label(
            self.root, textvariable=self.var_emp_utype, style="mystyle1.TLabel"
        )
        cmb_utype.place(x=850, y=190, width=180)

        # row 3
        # ====row4=======
        lbl_remark = Label(
            self.root,
            text="Remark",
            font=("goudy old style", 11),
            bg="black",
            fg="white",
        )
        lbl_remark.place(x=50, y=270)

        self.txt_remark = Text(
            self.root,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
        )
        self.txt_remark.place(x=150, y=230, width=300, height=60)

        # button
        btn_approve = customtkinter.CTkButton(
            self.root,
            text="Approve",
            command=self.approve,
            text_font=("goudy old style", 11),
            fg_color="blue",
            cursor="hand2",
        )
        btn_approve.place(x=50, y=305, width=110, height=28)

        btn_reject = customtkinter.CTkButton(
            self.root,
            text="Reject",
            command=self.reject,
            text_font=("goudy old style", 11),
            fg_color="red",
            cursor="hand2",
        )
        btn_reject.place(x=170, y=305, width=110, height=28)

        # Employee Details
        self.emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        self.emp_frame.place(x=0, y=350, relwidth=1, height=150)

        scrolly = Scrollbar(self.emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(self.emp_frame, orient=HORIZONTAL)

        self.employee_table = ttk.Treeview(
            self.emp_frame,
            columns=("eid", "name", "email", "contact", "utype", "date", "remark"),
            yscrollcommand=scrolly.set,
            xscrollcommand=scrollx.set,
            style="mystyle.Treeview",
        )
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.configure(command=self.employee_table.xview)
        scrolly.configure(command=self.employee_table.yview)
        self.employee_table.heading("eid", text="EMP ID")
        self.employee_table.heading("name", text="Name")
        self.employee_table.heading("email", text="Email")
        self.employee_table.heading("contact", text="Contact")
        self.employee_table.heading("utype", text="User Type")
        self.employee_table.heading("date", text="Date")
        self.employee_table.heading("remark", text="Remark")
        self.employee_table["show"] = "headings"

        self.employee_table.column("eid", width=90)
        self.employee_table.column("name", width=100)
        self.employee_table.column("email", width=100)
        self.employee_table.column("contact", width=100)
        self.employee_table.column("utype", width=100)
        self.employee_table.column("date", width=100)
        self.employee_table.column("remark", width=100)

        self.employee_table.pack(fill=BOTH, expand=1)

        self.employee_table.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def show(self):
        """Get value from database"""
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute(
                "Select date,remark,eid from attendance where status!='approve'"
            )
            rows = cur.fetchall()
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                cur.execute(
                    "Select eid,name,email,contact,utype from employee where eid=?",
                    row[2],
                )
                rows1 = cur.fetchall()
                value = rows1[0] + row
                self.employee_table.insert("", END, values=value)

        except IOError as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, _ev):
        """Get data from table"""
        _f = self.employee_table.focus()
        content = self.employee_table.item(_f)
        row = content["values"]
        if len(row) != 0:
            self.var_emp_id.set(row[0])
            self.var_emp_name.set(row[1])
            self.var_emp_email.set(row[2])
            self.var_emp_date.set(row[5])
            self.var_emp_contact.set(row[3])
            self.var_emp_utype.set(row[4])
            self.txt_remark.delete("1.0", END)
            self.txt_remark.insert(END, row[6])

    def approve(self):
        """Approve Attendance"""
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror(
                    "Error", "Employee ID must be required", parent=self.root
                )
            else:
                cur.execute(
                    "Select * from employee where eid=?", (self.var_emp_id.get(),)
                )
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror(
                        "Error", "Invalid employee id", parent=self.root
                    )
                else:
                    cur.execute(
                        "Update attendance set status=?,astatus=?,remark=? where eid=? and date=?",
                        (
                            "approve",
                            "present",
                            self.txt_remark.get("1.0", END),
                            self.var_emp_id.get(),
                            self.var_emp_date.get(),
                        ),
                    )
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Employee Updated Sucessfully", parent=self.root
                    )
                    self.show()
        except IOError as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def reject(self):
        """Reject Attendance"""
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror(
                    "Error", "Employee ID must be required", parent=self.root
                )
            else:
                cur.execute(
                    "Select * from employee where eid=?", (self.var_emp_id.get(),)
                )
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror(
                        "Error", "Invalid employee id", parent=self.root
                    )
                else:
                    cur.execute(
                        "Update attendance set status=?,astatus=?,remark=? where eid=? and date=?",
                        (
                            "reject",
                            "absent",
                            self.txt_remark.get("1.0", END),
                            self.var_emp_id.get(),
                            self.var_emp_date.get(),
                        ),
                    )
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Employee Updated Sucessfully", parent=self.root
                    )
                    self.show()
        except IOError as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = LoginSystem(root)
    root.mainloop()
