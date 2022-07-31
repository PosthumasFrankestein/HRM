from sqlite3.dbapi2 import connect
from tkinter import *
# from PIL import Image,ImageTk
import sqlite3
from tkinter import ttk,messagebox
from logins import Login_system
import customtkinter
customtkinter.set_appearance_mode("system")

class AttendanceMng:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1100x500+220+130")
       self.root.title("Logged as Admin")
       customtkinter.set_appearance_mode("system")


       #All Varialble
       self.var_searchby=StringVar()
       self.var_searchtxt=StringVar()

       self.var_emp_id=StringVar()
       self.var_emp_date=StringVar()
       self.var_emp_contact=StringVar()
       self.var_emp_name=StringVar()
       self.var_emp_email=StringVar()
       self.var_emp_utype=StringVar()  
       self.var_emp_remark=StringVar()    

       title=Label(self.root,text="Attendance Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)

    # #contents 
    #row 1
       lbl_empid=Label(self.root,text="Emp ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
       lbl_date=Label(self.root,text="Date",font=("goudy old style",15),bg="white").place(x=350,y=150)
       lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=750,y=150)

       txt_empid=Label(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)
       txt_date=Label(self.root,textvariable=self.var_emp_date,font=("goudy old style",15),bg="lightyellow").place(x=500,y=150,width=180)       
       txt_contact=Label(self.root,textvariable=self.var_emp_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)

#row 2
       lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
       lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=350,y=190)
       lbl_doj=Label(self.root,text="User Type",font=("goudy old style",15),bg="white").place(x=750,y=190)

       txt_name=Label(self.root,textvariable=self.var_emp_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)       
       txt_email=Label(self.root,textvariable=self.var_emp_email,font=("goudy old style",15),bg="lightyellow").place(x=500,y=190,width=180)       
       cmb_utype=ttk.Combobox(self.root,textvariable=self.var_emp_utype,values=("Admin","Employee"),state='readonly',justify=CENTER,font=("goudy old style",15))
       cmb_utype.place(x=850,y=190,width=180)   
       cmb_utype.current(0)


#row 3
      #====row4=======
       lbl_remark=Label(self.root,text="Remark",font=("goudy old style",15),bg="white").place(x=50,y=270)

       self.txt_remark=Text(self.root,font=("goudy old style",15),bg="lightyellow")
       self.txt_remark.place(x=150,y=230,width=300,height=60)       

      #button
       btn_approve=Button(self.root,text="Approve",command=self.approve,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=50,y=305,width=110,height=28)
       btn_reject=Button(self.root,text="Reject",command=self.reject,font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=150,y=305,width=110,height=28)

       #Employee Details
       emp_frame=Frame(self.root,bd=3,relief=RIDGE)
       emp_frame.place(x=0,y=350,relwidth=1,height=150)

       scrolly=Scrollbar(emp_frame,orient=VERTICAL)
       scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

       self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","contact","utype","date","remark"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
       scrollx.pack(side=BOTTOM,fill=X)
       scrolly.pack(side=RIGHT,fill=Y)
       scrollx.configure(command=self.EmployeeTable.xview)
       scrolly.configure(command=self.EmployeeTable.yview)
       self.EmployeeTable.heading("eid",text="EMP ID")
       self.EmployeeTable.heading("name",text="Name")
       self.EmployeeTable.heading("email",text="Email")
       self.EmployeeTable.heading("contact",text="Contact")
       self.EmployeeTable.heading("utype",text="User Type")
       self.EmployeeTable.heading("date",text="Date")
       self.EmployeeTable.heading("remark",text="Remark")
       self.EmployeeTable["show"]="headings"

       self.EmployeeTable.column("eid",width=90)
       self.EmployeeTable.column("name",width=100)
       self.EmployeeTable.column("email",width=100)
       self.EmployeeTable.column("contact",width=100)
       self.EmployeeTable.column("utype",width=100)
       self.EmployeeTable.column("date",width=100)
       self.EmployeeTable.column("remark",width=100)


       self.EmployeeTable.pack(fill=BOTH,expand=1)


       self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
       self.show()


    def show(self):
       con=sqlite3.connect(database=r'ims.db')
       cur=con.cursor()
       try:
              cur.execute("Select date,remark,eid from attendance where status!='approve'")
              # cur.execute("Select eid,name,email,dob,contact,utype from employee where eid=(Select eid from attendance where status='unapproved')")
              rows=cur.fetchall()
              self.EmployeeTable.delete(*self.EmployeeTable.get_children())
              for row in rows:
                     cur.execute("Select eid,name,email,contact,utype from employee where eid=?",row[2])
                     rows1=cur.fetchall()
                     value=rows1[0]+row
                     self.EmployeeTable.insert('',END,values=value)


       except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 

    def get_data(self,ev):
       f=self.EmployeeTable.focus()
       content=(self.EmployeeTable.item(f))
       row=content['values']
       if len(row)!=0:
              self.var_emp_id.set(row[0]),
              self.var_emp_name.set(row[1]),
              self.var_emp_email.set(row[2]),
              self.var_emp_date.set(row[5]),
              self.var_emp_contact.set(row[3]),
              self.var_emp_utype.set(row[4]),
              self.txt_remark.delete('1.0',END)
              self.txt_remark.insert(END,row[6]),

    def approve(self):
       con=sqlite3.connect(database=r'ims.db')
       cur=con.cursor()
       try:
           if self.var_emp_id.get()=="":
                  messagebox.showerror("Error","Employee ID must be required",parent=self.root)   
           else:
                  cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                  row=cur.fetchone()
                  if row is None:
                         messagebox.showerror("Error","Invalid employee id",parent=self.root)
                  else:
                         cur.execute("Update attendance set status=?,astatus=?,remark=? where eid=? and date=?",(
                                   "approve",
                                   "present",
                                   self.txt_remark.get('1.0',END),
                                   self.var_emp_id.get(),
                                   self.var_emp_date.get(),                                   
                         ))       
                         con.commit()
                         messagebox.showinfo('Success',"Employee Updated Sucessfully",parent=self.root)
                         self.show()
       except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 


    def reject(self):
       con=sqlite3.connect(database=r'ims.db')
       cur=con.cursor()
       try:
           if self.var_emp_id.get()=="":
                  messagebox.showerror("Error","Employee ID must be required",parent=self.root)   
           else:
                  cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                  row=cur.fetchone()
                  if row is None:
                         messagebox.showerror("Error","Invalid employee id",parent=self.root)
                  else:
                         cur.execute("Update attendance set status=?,astatus=?,remark=? where eid=? and date=?",(
                                   "reject",
                                   "absent",
                                   self.txt_remark.get('1.0',END),
                                   self.var_emp_id.get(),
                                   self.var_emp_date.get(),

                         ))       
                         con.commit()
                         messagebox.showinfo('Success',"Employee Updated Sucessfully",parent=self.root)
                         self.show()
       except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 


    def search(self):
       con=sqlite3.connect(database=r'ims.db')
       cur=con.cursor()
       try:   
              if self.var_searchby.get()=="Select":
                     messagebox.showerror("Error","Select Search By  option",parent=self.root)
              elif self.var_searchtxt.get()=="":
                     messagebox.showerror("Error","Search input should be required",parent=self.root)       
                     cur.execute("Select *from employee where "+self.var_searchby.get()+"LIKE '%"+self.var_searchtxt.get()+"%'")
                     rows=cur.fetchall()
                     if len(rows)!=0:
                            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                            for row in rows:
                                   self.EmployeeTable.insert('',END,values=row)
                     else:
                            messagebox.showerror("Error","No record found!!!",parent=self.root)              

       except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
if __name__=="__main__":     
#     root=Tk() 
    root=customtkinter.CTk()
    obj=Login_system(root)
    root.mainloop()      
