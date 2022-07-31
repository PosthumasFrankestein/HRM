from sqlite3.dbapi2 import connect
from tkinter import *
import sqlite3
from tkinter import ttk, messagebox
from datetime import *
from calendar import monthrange
from logins import Login_system
import customtkinter



class esalaryClass:
    def __init__(self, root,eid):
        self.root = root
        self.root.geometry("1100x400+220+130")
        self.root.resizable(True, True)
        self.root.title("Employee Management System")
        self.root.config(bg="black")
        eid=eid
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
        lbl_name= Label(
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
            bg="#211f1f",fg="white",
        ).place(x=150, y=150, width=180)
        txt_name = Label(
            self.root,
            textvariable=self.var_emp_name,
            font=("goudy old style", 11),
            bg="#211f1f",fg="white",
        ).place(x=500, y=150, width=180)
        txt_email = Label(
            self.root,
            textvariable=self.var_emp_email,
            font=("goudy old style", 11),
            bg="#211f1f",fg="white",
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
            bg="#211f1f",fg="white",
        ).place(x=150, y=190, width=180)
        txt_salary = Label(
            self.root,
            textvariable=self.var_emp_salary,
            font=("goudy old style", 11),
            bg="#211f1f",fg="white",
        ).place(x=500, y=190, width=180)
        txt_utype = Label(
            self.root,
            textvariable=self.var_emp_utype,
            justify=CENTER,
            font=("goudy old style", 11),
            bg="#211f1f",fg="white"
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
            bg="#211f1f",fg="white",
        ).place(x=150, y=230, width=180)
        txt_absent = Label(
            self.root,
            textvariable=self.var_emp_absent,
            font=("goudy old style", 11),
            bg="#211f1f",fg="white",
        ).place(x=500, y=230, width=180)
        txt_holiday = Entry(
            self.root,
            textvariable=self.var_emp_holiday,
            insertbackground="white",
            font=("goudy old style", 11),
            bg="#211f1f",fg="white"
        ).place(x=850, y=230, width=180)
        
        #row 4
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
            bg="#211f1f",fg="white",
        ).place(x=150, y=270, width=180)
        txt_bonus = Entry(
            self.root,
            textvariable=self.var_emp_bonus,
            font=("goudy old style", 11),
            bg="#211f1f",fg="white",
            insertbackground="white",
        ).place(x=500, y=270, width=180)
        txt_tsalary = Label(
            self.root,
            textvariable=self.var_emp_tsalary,
            justify=CENTER,
            font=("goudy old style", 11),
            bg="#211f1f",fg="white"
        ).place(x=850, y=270, width=180)

        # button
        btn_receipt = customtkinter.CTkButton(
            self.root,
            text="Get Data",
            command=lambda:self.get_data(eid),
            text_font=("goudy old style", 11),
            fg_color="#4caf50",
            cursor="hand2",
        ).place(x=850, y=305, width=180, height=28)


    def get_data(self, eid):
        today = date.today()
        num_days = monthrange(today.year,today.month)
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        cur.execute("Select eid,name,email,dob,contact,utype,salary from employee where eid=?",str(eid))
        row = cur.fetchone()
        
        try:
            cur.execute("Select count(*) from attendance where eid=? and astatus='present'",(str(row[0])))
            rows = cur.fetchone()

            

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

        self.var_emp_id.set(row[0]),
        self.var_emp_name.set(row[1]),
        self.var_emp_email.set(row[2]),
        self.var_emp_date.set(row[3]),
        self.var_emp_contact.set(row[4]),
        self.var_emp_utype.set(row[5]),
        self.var_emp_salary.set(row[6]),
        self.var_emp_absent.set(int(num_days[1])-int(rows[0]))
        self.var_emp_present.set(rows[0])


if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = esalaryClass(root)
    root.mainloop()
