from tkinter import *
from employee import employeeclass
import sqlite3
import os  
from logins import Login_system
import datetime

class EMS:
    def __init__(self,root,eid):
       self.root=root
       self.root.geometry("1350x700+0+0")
       self.root.title("Logged as Admin")
       self.root.config(bg="skyblue")
       
       #clock ko lagi      Time
       self.lbl_clock=Label(self.root,text="Welcome to Desktop Application for Employee Management\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15,"bold"),bg="green",fg="white") 
       self.lbl_clock.place(x=0,y=0,relwidth=1,height=30)

       #left menu
       LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
       LeftMenu.place(x=0,y=102,width=200,height=565)

       lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
       btn_employee=Button(LeftMenu,text="Employee",command=self.employee,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
       btn_supplier=Button(LeftMenu,text="Salary",command=self.Salary,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
       btn_category=Button(LeftMenu,text="Task",command=self.Task,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
       btn_product=Button(LeftMenu,text="Bonus",command=self.Bonus,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
       btn_sales=Button(LeftMenu,text="Attendance",command=self.Attendance,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
       btn_logout=Button(self.root,text="Logout",command=self.logout,font=("times new roman",15,"bold"),bg="red",cursor="hand2").place(x=1180,y=630,height=30,width=150)
       
           #content ko lagi     
       self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ] ",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
       self.lbl_employee.place(x=300,y=120,height=150,width=300)

       self.lbl_supplier=Label(self.root,text="Salary Info\n[ 0 ] ",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
       self.lbl_supplier.place(x=650,y=120,height=150,width=300)

       self.lbl_category=Label(self.root,text="Tasks \n[ 0 ] ",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
       self.lbl_category.place(x=1000,y=120,height=150,width=300)

       self.lbl_product=Label(self.root,text="Employee present \n[ 0 ] ",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
       self.lbl_product.place(x=300,y=300,height=150,width=300)

       self.lbl_product=Label(self.root,text="Employee absent \n[ 0 ] ",bd=5,relief=RIDGE,bg="black",fg="white",font=("goudy old style",20,"bold"))
       self.lbl_product.place(x=650,y=300,height=150,width=300)       

       self.lbl_sales=Label(self.root,text="Attendance info \n[ 0 ] ",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
       self.lbl_sales.place(x=1000,y=300,height=150,width=300)    

       self.update_content()
      
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeclass(self.new_win)

    def Salary(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salaryClass(self.new_win)

    def Task(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=taskClass(self.new_win)

    def Bonus(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=bonusClass(self.new_win)

    def Attendance(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=attendance(self.new_win)   

    def logout(self):
        self.lbl_clock.after_cancel(self.root.update)
        self.root.destroy()
        root=Tk()
        obj=Login_system(root)
        root.mainloop()                       

    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()

        try:
           cur.execute("select * from employee")
           employee=cur.fetchall()
           self.lbl_employee.config(text=f'Total employee\n[{str(len(employee))}]')
           attendence=len(os.listdir('Inventory/attendence'))
           self.lbl_sales.config(text=f'Attendance info [{str(attendence)}]')

           now=datetime.datetime.now()
           
           self.lbl_clock.config(text=f'Welcome to Employee Management System\t\t Time: {now.strftime("%I:%M:%S")} \t\t  Date: {now.strftime("%d-%m-%Y")}')
           self.root.update=self.lbl_clock.after(200,self.update_content)
       
        except Exception as ex:
            print(ex)
            messagebox.showerror("Error",f'Error due to : {str(ex)}',parent=self.root)
            
 

if __name__=="__main__":      
    root=Tk()
    obj=Login_system(root)
    root.mainloop()