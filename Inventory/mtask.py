from tkinter import *
import sqlite3
from tkinter import ttk, messagebox
from datetime import *
from logins import Login_system
import customtkinter
from tkcalendar import *


class Mngtask:
    def __init__(self, root, eid):
        self.root = root
        self.aby = eid
        self.root.geometry("1100x500+220+130")
        self.root.resizable(True, True)
        self.root.config(bg="black")
        cal = Calendar()


        # All Varialble
        self.var_task_id = StringVar()
        self.var_emp_id = StringVar()
        self.var_emp_name = StringVar()
        self.var_adate = StringVar()
        self.var_adate.set(cal.get_date())
        self.var_cdate = StringVar()
        self.var_task = StringVar()
        self.value = []

        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        cur.execute("Select eid from employee")
        rows = cur.fetchall()
        for row in rows:
            self.value.append(str(row[0]))

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

        self.title = customtkinter.CTkLabel(
            self.root,
            text="Manage Tasks",
            text_font=("goudy old style", 11),
            fg_color="#0f4d7d",
        ).place(x=50, y=100, width=1000)

        # #contents
        # row 1
        self.lbl_tid = ttk.Label(
            self.root,
            text="Task ID",
            style="mystyle1.TLabel"
        ).place(x=50, y=150)
        self.lbl_eid = ttk.Label(
            self.root,
            text="Emp Id",
            style="mystyle1.TLabel"
        ).place(x=350, y=150)
        self.lbl_name = ttk.Label(
            self.root,
            text="Name",
            style="mystyle1.TLabel"
        ).place(x=750, y=150)

        self.txt_tid = ttk.Label(
            self.root,
            textvariable=self.var_task_id,
            style="mystyle1.TLabel"
        ).place(x=160, y=150, width=180)
        self.txt_eid = customtkinter.CTkComboBox(
            self.root,
            values=self.value,
            variable=self.var_emp_id,
            command=self.fetchName,
        ).place(x=500, y=150, width=180)
        self.txt_name = ttk.Label(
            self.root,
            textvariable=self.var_emp_name,
            style="mystyle1.TLabel"
        ).place(x=850, y=150, width=180)

        # row 2
        self.lbl_date_assigned = ttk.Label(
            self.root,
            text="Date Assigned",
            style="mystyle1.TLabel"
        ).place(x=50, y=190)
        self.lbl_date_completed = ttk.Label(
            self.root,
            text="Date completed",
            style="mystyle1.TLabel"
        ).place(x=350, y=190)
        self.lbl_task = ttk.Label(
            self.root,
            text="Task",
            style="mystyle1.TLabel"
        ).place(x=750, y=190)

        self.txt_date_assigned = ttk.Label(
            self.root,
            textvariable=self.var_adate,
            style="mystyle1.TLabel"
        ).place(x=160, y=190, width=180)
        self.txt_date_completed = ttk.Label(
            self.root,
            textvariable=self.var_cdate,
            style="mystyle1.TLabel"
        ).place(x=500, y=190, width=180)
        self.txt_task = Entry(
            self.root,
            textvariable=self.var_task,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
            insertbackground="white"
        ).place(x=850, y=190, width=180)

        # row 3
        # ====row4=======
        self.lbl_task_remark = Label(
            self.root,
            text="Task Remark",
            font=("goudy old style", 11),
            fg="white",
            bg="black",
        ).place(x=50, y=230)

        self.var_tremark = Text(
            self.root,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
            insertbackground="white",
        )
        self.var_tremark.place(x=160, y=230, width=280, height=100)

        # button
        self.btn_add = customtkinter.CTkButton(
            self.root,
            text="Save",
            command=self.add,
            text_font=("goudy old style", 15),
            fg_color="#2196f3",
            cursor="hand2",
        ).place(x=500, y=305, width=110, height=28)
        self.btn_approve = customtkinter.CTkButton(
            self.root,
            text="Approve",
            command=self.approve,
            text_font=("goudy old style", 15),
            fg_color="#4caf50",
            cursor="hand2",
        ).place(x=620, y=305, width=110, height=28)
        self.btn_update = customtkinter.CTkButton(
            self.root,
            text="Reassign",
            command=self.reassign,
            text_font=("goudy old style", 15),
            fg_color="#f44336",
            cursor="hand2",
        ).place(x=740, y=305, width=110, height=28)
        self.btn_clear = customtkinter.CTkButton(
            self.root,
            text="Clear",
            command=self.clear,
            text_font=("goudy old style", 15),
            fg_color="#607d8b",
            cursor="hand2",
        ).place(x=860, y=305, width=110, height=28)

        # Employee Details
        self.emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        self.emp_frame.place(x=0, y=350, relwidth=1, height=150)

        scrolly = Scrollbar(self.emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(self.emp_frame, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(
            self.emp_frame,
            columns=(
                "tid",
                "task",
                "eid",
                "name",
                "adate",
                "cdate",
                "tstatus",
                "tremark",
            ),
            yscrollcommand=scrolly.set,
            xscrollcommand=scrollx.set,
            style="mystyle.Treeview",
        )
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("tid", text="Task ID")
        self.EmployeeTable.heading("task", text="Task")
        self.EmployeeTable.heading("eid", text="Emp Id")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("adate", text="Assign")
        self.EmployeeTable.heading("cdate", text="Complete")
        self.EmployeeTable.heading("tstatus", text="Status")
        self.EmployeeTable.heading("tremark", text="Remark")
        self.EmployeeTable["show"] = "headings"

        self.EmployeeTable.column("tid", width=10)
        self.EmployeeTable.column("task", width=10)
        self.EmployeeTable.column("eid", width=10)
        self.EmployeeTable.column("name", width=10)
        self.EmployeeTable.column("adate", width=10)
        self.EmployeeTable.column("cdate", width=10)
        self.EmployeeTable.column("tstatus", width=10)
        self.EmployeeTable.column("tremark", width=10)

        self.EmployeeTable.pack(fill=BOTH, expand=1)

        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def fetchName(self, choice):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute("Select name from employee where eid=?", choice)
            rows = cur.fetchone()
            self.var_emp_name.set(rows[0])
            self.var_emp_id.set(choice)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute(
                "Select tid,task,eid,adate,cdate,tstatus,tremark from tasks where tstatus!='approved'"
            )
            rows = cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                cur.execute("Select name from employee where eid=?", str(row[2]))
                row1 = cur.fetchone()
                value = list(row[0:3]) + list(row1[0:]) + list(row[3:])
                self.EmployeeTable.insert("", END, values=value)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.EmployeeTable.focus()
        content = self.EmployeeTable.item(f)
        row = content["values"]
        if row != "":
            self.var_task_id.set(row[0])
            self.var_emp_id.set(row[2])
            self.var_emp_name.set(row[3])
            self.var_adate.set(row[4])
            self.var_cdate.set(row[5])
            self.var_task.set(row[1])
            self.var_tremark.delete("1.0", END)
            self.var_tremark.insert(END, row[7])

    def add(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_emp_name.get() == "":
                messagebox.showerror("Error", "Select Employee Id", parent=self.root)
            else:
                cur.execute(
                    "Insert into tasks (adate,tstatus,task,tremark,eid,aby) values(?,?,?,?,?,?)",
                    (
                        self.var_adate.get(),
                        "pending",
                        self.var_task.get(),
                        self.var_tremark.get("1.0", END),
                        self.var_emp_id.get(),
                        self.aby,
                    ),
                )
                con.commit()
                messagebox.showinfo(
                    "Success", "Employee added Sucessfully", parent=self.root
                )
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def approve(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_task_id.get() == "":
                messagebox.showerror(
                    "Error", "Select Task to approve", parent=self.root
                )
            else:
                op = messagebox.askyesno(
                    "Confirm", "Do you really want to Approve?", parent=self.root
                )
                if op is True:

                    cur.execute(
                        "update tasks set tstatus='approved' where tid=?",
                        (self.var_task_id.get(),),
                    )
                    con.commit()
                    messagebox.showinfo("Success", "Task Approved", parent=self.root)
                    self.show()
                    self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def reassign(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_task_id.get() == "":
                messagebox.showerror(
                    "Error", "Select Task to reassign", parent=self.root
                )
            else:
                op = messagebox.askyesno(
                    "Confirm", "Do you really want to Reassign?", parent=self.root
                )
                if op is True:
                    cal = Calendar()
                    dvalue = cal.get_date()
                    cur.execute(
                        "Select eid from tasks where tid=?", self.var_task_id.get()
                    )
                    rows = cur.fetchone()
                    cur.execute(
                        "Insert into rtasks (tid,trdate,rejectby,eid) values(?,?,?,?)",
                        (
                            self.var_task_id.get(),
                            dvalue,
                            self.aby,
                            str(rows[0]),
                        ),
                    )
                    con.commit()
                    cur.execute(
                        "Update tasks set eid=?,tremark=? where tid=?",
                        (
                            self.var_emp_id.get(),
                            self.var_tremark.get("1.0", END),
                            self.var_task_id.get(),
                        ),
                    )
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Task Reassigned Sucessfully", parent=self.root
                    )
                    self.show()
                    self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def reject(self):
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
                        "Update employee set name=? where eid=?",
                        (
                            self.var_emp_name.get(),
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

    def clear(self):
        self.var_emp_id.set(""),

        self.var_emp_name.set(""),
        self.var_task_id.set(""),
        self.var_task.set(""),
        self.var_adate.set(""),

        self.var_cdate.set(""),
        self.var_tremark.delete("1.0", END),
        self.show()


if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = Login_system(root)
    root.mainloop()
