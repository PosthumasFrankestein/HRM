from sqlite3.dbapi2 import connect
from tkinter import *
import sqlite3
from tkinter import ttk, messagebox
from datetime import *
from calendar import monthrange
import customtkinter
import tkinter
from logins import Login_system


class Rating:
    def __init__(self, root,eid):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.resizable(True, True)
        self.root.config(bg="black")
        eid=eid
        # All Varialble
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_eid = StringVar()
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

        title = Label(
            self.root,
            text="Rating System",
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
        lbl_utype = Label(
            self.root,
            text="User Type",
            font=("goudy old style", 11),
            bg="black",
            fg="white",
        ).place(x=750, y=150)

        txt_empid = Label(
            self.root,
            textvariable=self.var_eid,
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
        txt_utype = Label(
            self.root,
            textvariable=self.var_emp_utype,
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
        lbl_rating = Label(
            self.root,
            text="Avg Rating",
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
        txt_rating = Label(
            self.root,
            textvariable=self.var_emp_rating,
            justify=CENTER,
            font=("goudy old style", 11),
            bg="#211f1f",
            fg="white",
        ).place(x=850, y=190, width=180)

        # row 3
        # ====row4=======
        label = Label(
            self.root,
            text="Collaboration",
            font=("goudy old style", 11),
            bg="black",
            fg="white",
        ).place(x=50, y=240)

        slider1 = customtkinter.CTkSlider(
            master=self.root,
            width=320,
            from_=0,
            to=5,
            number_of_steps=5,
            variable=self.value1,
        ).place(x=190, y=245)

        label = Label(
            master=self.root,
            text="Problem Solving",
            font=("goudy old style", 11),
            bg="black",
            fg="white",
        )
        label.place(x=560,y=240)

        slider2 = customtkinter.CTkSlider(
            master=self.root, 
            from_=0, 
            width=320,
            to=5, 
            number_of_steps=5, 
            variable=self.value2
        ).place(x=720,y=245)

        label = Label(
            master=self.root,
            text="Knowledge/Skills",
            font=("goudy old style", 11),
            bg="black",
            fg="white",
        )
        label.place(x=50,y=280)

        slider3 = customtkinter.CTkSlider(
            master=self.root, 
            from_=0, 
            width=320,
            to=5, 
            number_of_steps=5, 
            variable=self.value3
        ).place(x=190, y=285)

        label = Label(
            master=self.root,
            text="Customer service",
            font=("goudy old style", 11),
            bg="black",
            fg="white",
        )
        label.place(x=560,y=280)

        slider4 = customtkinter.CTkSlider(
            master=self.root, 
            from_=0, 
            to=5, 
            width=320,
            number_of_steps=5, 
            variable=self.value4
        ).place(x=720,y=285)

        button = customtkinter.CTkButton(
            master=self.root,
            border_width=0,
            corner_radius=8,
            fg_color="green",
            text="Rate",
            command=lambda:self.tvalue(eid),
            text_font=("goudy old style", 11)
        )
        button.place(x=850, y=310, width=180, height=28)

        # Employee Details
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=150)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(
            emp_frame,
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

    def tvalue(self,eid):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        value = (
            self.value1.get()
            + self.value2.get()
            + self.value3.get()
            + self.value4.get()
        )
        fvalue=(value/20)*8
        dvalue=date.today().strftime("%m/%d/%y")
        try:
            
            cur.execute("Select rdate from rating where eid=? and ratedby IS NOT NULL ORDER BY rid DESC",(str(self.var_eid.get())))
            row=cur.fetchone()
            print(dvalue,row)
            if row==None or (row[0]!=dvalue):
                cur.execute("Insert into rating (rdate,eid,rate,ratedby) values(?,?,?,?)",(dvalue,self.var_eid.get(),fvalue,eid))       
                con.commit()
                messagebox.showinfo(
                    "Success", "Employee Updated Sucessfully", parent=self.root
                )
            else:
                messagebox.showerror("Error","You have already rated for today",parent=self.root)
            self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute("Select eid,name,email,dob,contact,utype,salary from employee")
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
        today = date.today()
        num_days = monthrange(today.year, today.month)
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()

        try:
            cur.execute(
                "Select count(*) from attendance where eid=? and astatus='present'",
                (str(row[0])),
            )
            rows = cur.fetchone()
            cur.execute(
                "Select count(*),sum(rate) from rating where eid=?",
                (str(row[0])),
            )
            rows1=cur.fetchone()
            value=(rows1[1]/rows1[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

        self.var_eid.set(row[0]),
        self.var_emp_name.set(row[1]),
        self.var_emp_email.set(row[2]),
        self.var_emp_date.set(row[3]),
        self.var_emp_contact.set(row[4]),
        self.var_emp_utype.set(row[5]),
        self.var_emp_salary.set(row[6]),
        self.var_emp_absent.set(int(num_days[1]) - int(rows[0]))
        self.var_emp_present.set(rows[0]),
        self.var_emp_rating.set(value),

    def search(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror(
                    "Error", "Select Search By  option", parent=self.root
                )
            elif self.var_searchtxt.get() == "":
                messagebox.showerror(
                    "Error", "Search input should be required", parent=self.root
                )
                cur.execute(
                    "Select *from employee where "
                    + self.var_searchby.get()
                    + "LIKE '%"
                    + self.var_searchtxt.get()
                    + "%'"
                )
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert("", END, values=row)
                else:
                    messagebox.showerror(
                        "Error", "No record found!!!", parent=self.root
                    )

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = Login_system(root)
    root.mainloop()
