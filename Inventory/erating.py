from tkinter import *
import sqlite3
from tkinter import ttk, messagebox
from datetime import *
from calendar import monthrange
import customtkinter
from sqlalchemy import null
from logins import Login_system

class EmpRate():
    def __init__(self,root,eid):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.resizable(True, True)
        self.root.config(bg="black")
        # All Varialble
        eid=eid
        self.var_emp_id = StringVar()
        self.var_emp_date = StringVar()
        self.var_emp_contact = StringVar()
        self.var_emp_name = StringVar()
        self.var_emp_email = StringVar()
        self.var_emp_salary = StringVar()
        self.var_emp_utype = StringVar()
        self.var_emp_rating = StringVar()
        self.var_emp_tsalary = StringVar()        
        self.value1 = IntVar()
        self.value2 = IntVar()
        self.value3 = IntVar()
        self.value4 = IntVar()

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
            textvariable=self.var_emp_utype,
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
        self.get_data(eid)


    def tvalue(self,eid):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        value = (
            self.value1.get()
            + self.value2.get()
            + self.value3.get()
            + self.value4.get()
        )
        fvalue=(value/20)*2
        dvalue=date.today().strftime("%m/%d/%y")
        try:
            cur.execute("Select rdate from rating where eid=? and ratedby is NULL ORDER BY rid DESC",(str(eid)))
            row=cur.fetchone()
            if row is None or (row[0]!=dvalue):
                cur.execute("Insert into rating (rdate,eid,rate) values(?,?,?)",(dvalue,eid,fvalue))       
                con.commit()
                messagebox.showinfo(
                    "Success", "Employee Updated Sucessfully", parent=self.root
                )
            else:
                messagebox.showerror("Error","You have already rated for today",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, eid):
        today = date.today()
        num_days = monthrange(today.year, today.month)
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()

        try:
            cur.execute("Select eid,name,utype,doj,salary from employee where eid=?",str(eid))
            row = cur.fetchone()
            self.var_emp_id.set(row[0]),
            self.var_emp_name.set(row[1]),
            self.var_emp_utype.set(row[2]),
            self.var_emp_date.set(row[3]),
            self.var_emp_salary.set(row[4])

        except Exception as ex:
            messagebox.showerror("Error", f"Error here due to : {str(ex)}", parent=self.root)




if __name__ == "__main__":
    root=customtkinter.CTk()
    obj = Login_system(root)
    root.mainloop()
