from tkinter import *
import sqlite3
from tkinter import ttk, messagebox
from logins import Login_system
import customtkinter


class employeeclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.config(bg="black")

        # All Varialble
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_emp_id = StringVar()
        self.var_emp_gender = StringVar()
        self.var_emp_contact = StringVar()
        self.var_emp_name = StringVar()
        self.var_emp_dob = StringVar()
        self.var_emp_doj = StringVar()
        self.var_emp_email = StringVar()
        self.var_emp_pass = StringVar()
        self.var_emp_utype = StringVar()
        self.var_emp_salary = StringVar()
        self.var_emp_address = StringVar()
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
            anchor=CENTER
        )

        # title

        self.title = Label(
            self.root,
            text="Employee Details",
            font=("goudy old style", 15),
            bg="#0f4d7d",
            fg="white",
        ).place(x=50, y=100, width=1000)

        # #contents
        # row 1
        self.lbl_empid = ttk.Label(
            self.root, text="Emp ID", style="mystyle1.TLabel"
        ).place(x=50, y=150)
        self.lbl_gender = ttk.Label(
            self.root, text="Gender", style="mystyle1.TLabel"
        ).place(x=350, y=150)
        self.lbl_contact = ttk.Label(
            self.root, text="Contact", style="mystyle1.TLabel"
        ).place(x=750, y=150)

        self.txt_empid = Entry(
            self.root,
            textvariable=self.var_emp_id,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
        ).place(x=150, y=150, width=180)
        self.txt_gender = customtkinter.CTkComboBox(
            self.root,
            values=("Male", "Female", "Other"),
            variable=self.var_emp_gender,
        ).place(x=500, y=150, width=180)
        self.txt_contact = Entry(
            self.root,
            textvariable=self.var_emp_contact,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
        ).place(x=850, y=150, width=180)

        # row 2
        self.lbl_name = ttk.Label(
            self.root, text="Name", style="mystyle1.TLabel"
        ).place(x=50, y=190)
        self.lbl_dob = ttk.Label(
            self.root, text="D.O.B", style="mystyle1.TLabel"
        ).place(x=350, y=190)
        self.lbl_doj = ttk.Label(
            self.root, text="D.O.J", style="mystyle1.TLabel"
        ).place(x=750, y=190)

        self.txt_name = Entry(
            self.root,
            textvariable=self.var_emp_name,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
        ).place(x=150, y=190, width=180)
        self.txt_dob = Entry(
            self.root,
            textvariable=self.var_emp_dob,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
        ).place(x=500, y=190, width=180)
        self.txt_doj = Entry(
            self.root,
            textvariable=self.var_emp_doj,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
        ).place(x=850, y=190, width=180)

        # row 3
        self.lbl_email = ttk.Label(
            self.root, text="Email", style="mystyle1.TLabel"
        ).place(x=50, y=230)
        self.lbl_pass = ttk.Label(
            self.root, text="Password", style="mystyle1.TLabel"
        ).place(x=350, y=230)
        self.lbl_utype = ttk.Label(
            self.root, text="User Type", style="mystyle1.TLabel"
        ).place(x=750, y=230)

        self.txt_email = Entry(
            self.root,
            textvariable=self.var_emp_email,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
        ).place(x=150, y=230, width=180)
        self.txt_pass = Entry(
            self.root,
            textvariable=self.var_emp_pass,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
        ).place(x=500, y=230, width=180)
        
        self.txt_utype = customtkinter.CTkComboBox(
            self.root,
            values=("Admin", "Employee"),
            variable=self.var_emp_utype,
        ).place(x=850, y=230, width=180)

        # ====row4=======
        self.lbl_address = ttk.Label(
            self.root, text="Address", style="mystyle1.TLabel"
        ).place(x=50, y=270)
        self.lbl_salary = ttk.Label(
            self.root, text="Salary", style="mystyle1.TLabel"
        ).place(x=500, y=270)

        self.txt_address = Text(
            self.root, font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
        )
        self.txt_address.place(x=150, y=270, width=300, height=60)
        
        self.txt_salary = Entry(
            self.root,
            textvariable=self.var_emp_salary,
            font=("goudy old style", 11),
            bg="black",
            fg="white",
        ).place(x=600, y=270, width=180)

        # button
        self.btn_add = Button(
            self.root,
            text="Save",
            command=self.add,
            font=("goudy old style", 11),
            bg="#2196f3",
            fg="white",
            cursor="hand2",
        ).place(x=500, y=305, width=110, height=28)
        self.btn_update = Button(
            self.root,
            text="Update",
            command=self.update,
            font=("goudy old style", 11),
            bg="#4caf50",
            fg="white",
            cursor="hand2",
        ).place(x=620, y=305, width=110, height=28)
        self.btn_delete = Button(
            self.root,
            text="Delete",
            command=self.delete,
            font=("goudy old style", 11),
            bg="#f44336",
            fg="white",
            cursor="hand2",
        ).place(x=740, y=305, width=110, height=28)
        self.btn_clear = Button(
            self.root,
            text="Clear",
            command=self.clear,
            font=("goudy old style", 11),
            bg="#607d8b",
            fg="white",
            cursor="hand2",
        ).place(x=860, y=305, width=110, height=28)

        # Employee Details
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=150)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(
            emp_frame,
            columns=(
                "eid",
                "name",
                "email",
                "gender",
                "contact",
                "dob",
                "doj",
                "pass",
                "utype",
                "address",
                "salary",
            ),
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
        self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.heading("gender", text="Gender")
        self.EmployeeTable.heading("contact", text="Contact")
        self.EmployeeTable.heading("dob", text="D.O.B")
        self.EmployeeTable.heading("doj", text="D.O.J")
        self.EmployeeTable.heading("pass", text="Password")
        self.EmployeeTable.heading("utype", text="User Type")
        self.EmployeeTable.heading("address", text="Adress")
        self.EmployeeTable.heading("salary", text="Salary")
        self.EmployeeTable["show"] = "headings"

        self.EmployeeTable.column("eid", width=90)
        self.EmployeeTable.column("name", width=100)
        self.EmployeeTable.column("email", width=100)
        self.EmployeeTable.column("gender", width=100)
        self.EmployeeTable.column("contact", width=100)
        self.EmployeeTable.column("dob", width=100)
        self.EmployeeTable.column("doj", width=100)
        self.EmployeeTable.column("pass", width=100)
        self.EmployeeTable.column("utype", width=100)
        self.EmployeeTable.column("address", width=100)
        self.EmployeeTable.column("salary", width=100)

        self.EmployeeTable.pack(fill=BOTH, expand=1)

        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    # ===========================================================================
    def add(self):
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
                if row is not None:
                    messagebox.showerror(
                        "Error",
                        "This Employee ID already assigned,try different",
                        parent=self.root,
                    )
                else:
                    cur.execute(
                        "Insert into employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",
                        (
                            self.var_emp_id.get(),
                            self.var_emp_name.get(),
                            self.var_emp_email.get(),
                            self.var_emp_gender.get(),
                            self.var_emp_contact.get(),
                            self.var_emp_dob.get(),
                            self.var_emp_doj.get(),
                            self.var_emp_pass.get(),
                            self.var_emp_utype.get(),
                            self.txt_address.get("1.0", END),
                            self.var_emp_salary.get(),
                        ),
                    )
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Employee added Sucessfully", parent=self.root
                    )
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute("Select *from employee")
            rows = cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.EmployeeTable.focus()
        content = self.EmployeeTable.item(f)
        row = content["values"]
        self.var_emp_id.set(row[0]),

        self.var_emp_name.set(row[1]),
        self.var_emp_email.set(row[2]),
        self.var_emp_gender.set(row[3]),
        self.var_emp_contact.set(row[4]),

        self.var_emp_dob.set(row[5]),
        self.var_emp_doj.set(row[6]),

        self.var_emp_pass.set(row[7]),
        self.var_emp_utype.set(row[8]),
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[9]),

    def update(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror(
                    "Error", "Employee ID must be required", parent=self.root
                )
            else:
                cur.execute(
                    "Select *from employee where eid=?", (self.var_emp_id.get(),)
                )
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror(
                        "Error", "Invalid employee id", parent=self.root
                    )
                else:
                    cur.execute(
                        "Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",
                        (
                            self.var_emp_name.get(),
                            self.var_emp_email.get(),
                            self.var_emp_gender.get(),
                            self.var_emp_contact.get(),
                            self.var_emp_dob.get(),
                            self.var_emp_doj.get(),
                            self.var_emp_pass.get(),
                            self.var_emp_utype.get(),
                            self.txt_address.get("1.0", END),
                            self.var_emp_salary.get(),
                            self.var_emp_id.get(),
                        ),
                    )
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Employee Updated Sucessfully", parent=self.root
                    )
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror(
                    "Error", "Employee ID must be required", parent=self.root
                )
            else:
                cur.execute(
                    "Select *from employee where eid=?", (self.var_emp_id.get(),)
                )
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror(
                        "Error", "Invalid employee id", parent=self.root
                    )
                else:
                    op = messagebox.askyesno(
                        "Confirm", "Do you really want to delete?", parent=self.root
                    )
                    if op is True:

                        cur.execute(
                            "delete from employee where eid=?", (self.var_emp_id.get(),)
                        )
                        con.commit()
                        messagebox.showerror(
                            "Delete", "Employee Deleted Sucessfully", parent=self.root
                        )
                        self.show()
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.var_emp_id.set(""),

        self.var_emp_name.set(""),
        self.var_emp_email.set(""),
        self.var_emp_gender.set("Select"),
        self.var_emp_contact.set(""),

        self.var_emp_dob.set(""),
        self.var_emp_doj.set(""),

        self.var_emp_pass.set(""),
        self.var_emp_utype.set("Admin"),
        self.txt_address.delete("1.0", END),
        self.var_emp_salary.set("")
        self.show()


if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = Login_system(root)
    root.mainloop()
