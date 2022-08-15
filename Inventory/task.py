"""Import required modules"""
from tkinter import *
import sqlite3
from tkinter import ttk, messagebox
from logins import LoginSystem
import customtkinter
from tkcalendar import Calendar


class TaskClass:
    """Show assigned employee tasks"""

    def __init__(self, root, eid):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.resizable(True, True)
        self.root.config(bg="black")
        # All Varialble

        self.var_task_id = StringVar()
        self.var_emp_id = StringVar()
        self.var_emp_name = StringVar()
        self.var_cdate = StringVar()
        self.var_adate = StringVar()
        self.var_task = StringVar()

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

        self.title = customtkinter.CTkLabel(
            self.root,
            text="Manage Tasks",
            text_font=("goudy old style", 11),
            fg_color="#0f4d7d",
        )
        self.title.place(x=50, y=100, width=1000)

        # #contents
        # row 1
        self.lbl_tid = ttk.Label(self.root, text="Task ID", style="mystyle1.TLabel")
        self.lbl_tid.place(x=50, y=150)

        self.lbl_eid = ttk.Label(self.root, text="Emp Id", style="mystyle1.TLabel")
        self.lbl_eid.place(x=350, y=150)

        self.lbl_name = ttk.Label(self.root, text="Name", style="mystyle1.TLabel")
        self.lbl_name.place(x=750, y=150)

        self.txt_tid = ttk.Label(
            self.root, textvariable=self.var_task_id, style="mystyle1.TLabel"
        )
        self.txt_tid.place(x=160, y=150, width=180)

        self.txt_eid = ttk.Label(
            self.root, textvariable=self.var_emp_id, style="mystyle1.TLabel"
        )
        self.txt_eid.place(x=500, y=150, width=180)

        self.txt_name = ttk.Label(
            self.root, textvariable=self.var_emp_name, style="mystyle1.TLabel"
        )
        self.txt_name.place(x=850, y=150, width=180)

        # row 2
        self.lbl_date_assigned = ttk.Label(
            self.root, text="Date Assigned", style="mystyle1.TLabel"
        )
        self.lbl_date_assigned.place(x=50, y=190)

        self.lbl_date_completed = ttk.Label(
            self.root, text="Date completed", style="mystyle1.TLabel"
        )
        self.lbl_date_completed.place(x=350, y=190)

        self.lbl_task = ttk.Label(self.root, text="Task", style="mystyle1.TLabel")
        self.lbl_task.place(x=750, y=190)

        self.txt_date_assigned = ttk.Label(
            self.root, textvariable=self.var_adate, style="mystyle1.TLabel"
        )
        self.txt_date_assigned.place(x=160, y=190, width=180)

        self.txt_date_completed = ttk.Label(
            self.root, textvariable=self.var_cdate, style="mystyle1.TLabel"
        )
        self.txt_date_completed.place(x=500, y=190, width=180)

        self.txt_task = Entry(
            self.root,
            textvariable=self.var_task,
            font=("goudy old style", 11),
            insertbackground="white",
            bg="#211f1f",
            fg="white",
        )
        self.txt_task.place(x=850, y=190, width=180)

        # row 3
        # ====row4=======
        self.lbl_task_remark = Label(
            self.root,
            text="Task Remark",
            font=("goudy old style", 11),
            fg="white",
            bg="black",
        )
        self.lbl_task_remark.place(x=50, y=230)

        self.var_tremark = Text(
            self.root,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
            insertbackground="white",
        )
        self.var_tremark.place(x=160, y=230, width=280, height=100)

        # button
        self.btn_complete = customtkinter.CTkButton(
            self.root,
            text="Complete",
            command=lambda: self.complete(eid),
            text_font=("goudy old style", 15),
            fg_color="#4caf50",
            cursor="hand2",
        )
        self.btn_complete.place(x=620, y=305, width=110, height=28)

        self.btn_forfeit = customtkinter.CTkButton(
            self.root,
            text="Forfeit",
            command=lambda: self.forfeit(eid),
            text_font=("goudy old style", 15),
            fg_color="#f44336",
            cursor="hand2",
        )
        self.btn_forfeit.place(x=740, y=305, width=110, height=28)

        self.btn_clear = customtkinter.CTkButton(
            self.root,
            text="Clear",
            command=lambda: self.clear(eid),
            text_font=("goudy old style", 15),
            fg_color="#607d8b",
            cursor="hand2",
        )
        self.btn_clear.place(x=860, y=305, width=110, height=28)

        # Employee Details
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=150)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.employee_table = ttk.Treeview(
            emp_frame,
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
        scrollx.config(command=self.employee_table.xview)
        scrolly.config(command=self.employee_table.yview)
        self.employee_table.heading("tid", text="Task ID")
        self.employee_table.heading("task", text="Task")
        self.employee_table.heading("eid", text="Emp Id")
        self.employee_table.heading("name", text="Name")
        self.employee_table.heading("adate", text="Assign")
        self.employee_table.heading("cdate", text="Complete")
        self.employee_table.heading("tstatus", text="Status")
        self.employee_table.heading("tremark", text="Remark")
        self.employee_table["show"] = "headings"

        self.employee_table.column("tid", width=10)
        self.employee_table.column("task", width=10)
        self.employee_table.column("eid", width=10)
        self.employee_table.column("name", width=10)
        self.employee_table.column("adate", width=10)
        self.employee_table.column("cdate", width=10)
        self.employee_table.column("tstatus", width=10)
        self.employee_table.column("tremark", width=10)

        self.employee_table.pack(fill=BOTH, expand=1)

        self.employee_table.bind("<ButtonRelease-1>", self.get_data)
        self.show(eid)

    def show(self, eid):
        """Show data on table"""
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute(
                "Select tid,task,eid,adate,cdate,tstatus,tremark"
                " from tasks where eid=? and tstatus!='approved' and tstatus!='forfeit'",
                str(eid),
            )
            rows = cur.fetchall()
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                cur.execute("Select name from employee where eid=?", str(row[2]))
                row1 = cur.fetchone()
                value = list(row[0:3]) + list(row1[0:]) + list(row[3:])
                self.employee_table.insert("", END, values=value)

        except (IOError, TypeError) as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, _ev):
        """Get table from table"""
        _f = self.employee_table.focus()
        content = self.employee_table.item(_f)
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

    def complete(self, eid):
        """Mark task as Complete"""
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()

        cal = Calendar()
        cdate = cal.get_date()
        try:
            if self.var_emp_name.get() == "":
                messagebox.showerror("Error", "Select Employee ID", parent=self.root)
            else:
                _op = messagebox.askyesno(
                    "Confirm", "Do you really want mark as complete?", parent=self.root
                )
                if _op is True:

                    cur.execute(
                        "update tasks set tstatus='complete',cdate=? where tid=?",
                        (
                            cdate,
                            self.var_task_id.get(),
                        ),
                    )
                    con.commit()
                    messagebox.showinfo("Success", "Task Completed", parent=self.root)
                    self.show(eid)
                    self.clear(eid)

        except (IOError, TypeError) as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def forfeit(self, eid):
        """Mark task as forfeit"""
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_emp_name.get() == "":
                messagebox.showerror("Error", "Select Employee ID", parent=self.root)
            else:
                _op = messagebox.askyesno(
                    "Confirm", "Do you really want to Forfeit?", parent=self.root
                )
                if _op is True:
                    cur.execute(
                        "update tasks set tstatus='forfeit' where tid=?",
                        (self.var_task_id.get(),),
                    )
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Task Forfeited Sucessfully", parent=self.root
                    )
                    self.show(eid)
                    self.clear(eid)

        except (IOError, TypeError) as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self, eid):
        """Clear values"""
        self.var_emp_id.set("")
        self.var_emp_name.set("")
        self.var_task_id.set("")
        self.var_task.set("")
        self.var_adate.set("")
        self.var_cdate.set("")
        self.var_tremark.delete("1.0", END)
        self.show(eid)


if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = LoginSystem(root)
    root.mainloop()
