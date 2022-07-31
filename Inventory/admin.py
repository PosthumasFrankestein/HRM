from sqlite3.dbapi2 import connect
from tkinter import *
import sqlite3
from tkinter import ttk,messagebox


class adminclass:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1100x500+220+130")
       self.root.title("Employee Management System")
       self.root.config(bg="black")
       #All Varialble
       self.var_searchby=StringVar()
       self.var_searchtxt=StringVar()

       self.var_emp_id=StringVar()
       self.var_emp_gender=StringVar()
       self.var_emp_contact=StringVar()
       self.var_emp_name=StringVar()
       self.var_emp_dob=StringVar()
       self.var_emp_doj=StringVar()
       self.var_emp_email=StringVar()
       self.var_emp_pass=StringVar()
       self.var_login=StringVar()
       self.var_emp_salary=StringVar()   
       self.var_emp_address=StringVar()    


       title=Label(self.root,text="Admin Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)

    # #contents 
    #row 1
       lbl_empid=Label(self.root,text="Emp ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
       lbl_login=Label(self.root,text="Login",font=("goudy old style",15),bg="white").place(x=350,y=150)
       lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=750,y=150)

       txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)       
       txt_login=Entry(self.root,textvariable=self.var_emp_pass,font=("goudy old style",15),bg="lightyellow").place(x=500,y=150,width=180)
       txt_contact=Entry(self.root,textvariable=self.var_emp_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)

#row 2
       lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
       lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15),bg="white").place(x=350,y=190)
       lbl_doj=Label(self.root,text="D.O.J",font=("goudy old style",15),bg="white").place(x=750,y=190)

       txt_name=Entry(self.root,textvariable=self.var_emp_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)       
       txt_dob=Entry(self.root,textvariable=self.var_emp_dob,font=("goudy old style",15),bg="lightyellow").place(x=500,y=190,width=180)       
       txt_doj=Entry(self.root,textvariable=self.var_emp_doj,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)       

#row 3
       lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=50,y=230)
       lbl_pass=Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x=350,y=230)
       lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=750,y=230)

       txt_email=Entry(self.root,textvariable=self.var_emp_email,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)       
       txt_pass=Entry(self.root,textvariable=self.var_emp_pass,font=("goudy old style",15),bg="lightyellow").place(x=500,y=230,width=180)
       cmb_gender=ttk.Combobox(self.root,textvariable=self.var_emp_gender,values=("Select","Male","Female","Other"),state='readonly',justify=CENTER,font=("goudy old style",15))
       cmb_gender.place(x=850,y=230,width=180)
       cmb_gender.current(0)

      #====row4=======
       lbl_address=Label(self.root,text="Address",font=("goudy old style",15),bg="white").place(x=50,y=270)
       lbl_salary=Label(self.root,text="Salary",font=("goudy old style",15),bg="white").place(x=500,y=270)

       self.txt_address=Text(self.root,font=("goudy old style",15),bg="lightyellow")
       self.txt_address.place(x=150,y=270,width=300,height=60)       
       txt_salary=Entry(self.root,textvariable=self.var_emp_salary,font=("goudy old style",15),bg="lightyellow").place(x=600,y=270,width=180)       

      #button
       btn_add=Button(self.root,text="Add",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
       btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
       btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)
       btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)

       #Admin Details
       emp_frame=Frame(self.root,bd=3,relief=RIDGE)
       emp_frame.place(x=0,y=350,relwidth=1,height=150)

       scrolly=Scrollbar(emp_frame,orient=VERTICAL)
       scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

       self.AdminTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
       scrollx.pack(side=BOTTOM,fill=X)
       scrolly.pack(side=RIGHT,fill=Y)
       scrollx.config(command=self.AdminTable.xview)
       scrolly.config(command=self.AdminTable.yview)
       self.AdminTable.heading("eid",text="EMP ID")
       self.AdminTable.heading("name",text="Name")
       self.AdminTable.heading("email",text="Email")
       self.AdminTable.heading("gender",text="Gender")
       self.AdminTable.heading("contact",text="Contact")
       self.AdminTable.heading("dob",text="D.O.B")
       self.AdminTable.heading("doj",text="D.O.J")
       self.AdminTable.heading("pass",text="Password")
       self.AdminTable.heading("address",text="Adress")
       self.AdminTable.heading("salary",text="Salary")
       self.AdminTable["show"]="headings"

       self.AdminTable.column("eid",width=90)
       self.AdminTable.column("name",width=100)
       self.AdminTable.column("email",width=100)
       self.AdminTable.column("gender",width=100)
       self.AdminTable.column("contact",width=100)
       self.AdminTable.column("dob",width=100)
       self.AdminTable.column("doj",width=100)
       self.AdminTable.column("pass",width=100)
       self.AdminTable.column("utype",width=100)
       self.AdminTable.column("address",width=100)
       self.AdminTable.column("salary",width=200)


       self.AdminTable.pack(fill=BOTH,expand=1)


       self.AdminTable.bind("<ButtonRelease-1>",self.get_data)
       self.show()

#===========================================================================
    def add(self):
       con=sqlite3.connect(database=r'ims.db')
       cur=con.cursor()
       try:
           if self.var_emp_id.get()=="":
                  messagebox.showerror("Error","Admin ID must be required",parent=self.root)   
           else:
                  cur.execute("Select *from admin where eid=?",(self.var_emp_id.get(),))
                  row=cur.fetchone()
                  if row!=None:
                         messagebox.showerror("Error","This Admin ID already assigned,try different",parent=self.root)
                  else:
                         cur.execute("Insert into admin (eid,login,name,email,gender,contact,dob,doj,pass,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                   self.var_emp_id.get(),
                                   self.var_login.get(),
                                   self.var_emp_name.get(),
                                   self.var_emp_email.get(),
                                   self.var_emp_gender.get(),
                                   self.var_emp_contact.get(),

                                   self.var_emp_dob.get(),
                                   self.var_emp_doj.get(),

                                   self.var_emp_pass.get(),
                                   self.txt_address.get('1.0',END),
                                   self.var_emp_salary.get()       
                         ))       
                         con.commit()
                         messagebox.showinfo('Success',"Admin added Sucessfully",parent=self.root)
                         self.show()
       except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 

    def show(self):
       con=sqlite3.connect(database=r'ims.db')
       cur=con.cursor()
       try:
              cur.execute("Select *from admin")
              rows=cur.fetchall()
              self.AdminTable.delete(*self.AdminTable.get_children())
              for row in rows:
                     self.AdminTable.insert('',END,values=row)

       except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 

    def get_data(self,ev):
       f=self.AdminTable.focus()
       content=(self.AdminTable.item(f))
       row=content['values']
       self.var_emp_id.set(row[0]),

       self.var_emp_name.set(row[1]),
       self.var_emp_email.set(row[2]),
       self.var_emp_gender.set(row[3]),
       self.var_emp_contact.set(row[4]),

       self.var_emp_dob.set(row[5]),
       self.var_emp_doj.set(row[6]),

       self.var_emp_pass.set(row[7]),
       self.var_login.set(row[8]),
       self.txt_address.delete('1.0',END)
       self.txt_address.insert(END,row[9]),

    def update(self):
       con=sqlite3.connect(database=r'ims.db')
       cur=con.cursor()
       try:
           if self.var_emp_id.get()=="":
                  messagebox.showerror("Error","Admin ID must be required",parent=self.root)   
           else:
                  cur.execute("Select *from admin where eid=?",(self.var_emp_id.get(),))
                  row=cur.fetchone()
                  if row==None:
                         messagebox.showerror("Error","Invalid admin id",parent=self.root)
                  else:
                         cur.execute("Update admin set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",(
                                   self.var_emp_name.get(),
                                   self.var_emp_email.get(),
                                   self.var_emp_gender.get(),
                                   self.var_emp_contact.get(),

                                   self.var_emp_dob.get(),
                                   self.var_emp_doj.get(),

                                   self.var_emp_pass.get(),
                                   self.var_login.get(),
                                   self.txt_address.get('1.0',END),
                                   self.var_emp_salary.get(),
                                   self.var_emp_id.get(),

                         ))       
                         con.commit()
                         messagebox.showinfo('Success',"Admin Updated Sucessfully",parent=self.root)
                         self.show()
       except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 

    def delete(self):
       con=sqlite3.connect(database=r'ims.db')
       cur=con.cursor()
       try:
           if self.var_emp_id.get()=="":
                  messagebox.showerror("Error","Admin ID must be required",parent=self.root)   
           else:
                  cur.execute("Select *from admin where eid=?",(self.var_emp_id.get(),))
                  row=cur.fetchone()
                  if row==None:
                         messagebox.showerror("Error","Invalid admin id",parent=self.root)
                  else:
                         op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                         if op==True:

                            cur.execute("delete from admin where eid=?",(self.var_emp_id.get(),))
                            con.commit()
                            messagebox.showerror("Delete","Admin Deleted Sucessfully",parent=self.root)
                            self.show()
                            self.clear()

       except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 

    def clear(self):
       self.var_emp_id.set(""),

       self.var_emp_name.set(""),
       self.var_emp_email.set(""),
       self.var_emp_gender.set("Select"),
       self.var_emp_contact.set(""),

       self.var_emp_dob.set(""),
       self.var_emp_doj.set(""),

       self.var_emp_pass.set(""),
       self.var_login.set(""),
       self.txt_address.delete('1.0',END),
       self.var_emp_salary.set("")   
       self.show()


    def search(self):
       con=sqlite3.connect(database=r'ims.db')
       cur=con.cursor()
       try:   
              if self.var_searchby.get()=="Select":
                     messagebox.showerror("Error","Select Search By  option",parent=self.root)
              elif self.var_searchtxt.get()=="":
                     messagebox.showerror("Error","Search input should be required",parent=self.root)       
                     cur.execute("Select *from admin where "+self.var_searchby.get()+"LIKE '%"+self.var_searchtxt.get()+"%'")
                     rows=cur.fetchall()
                     if len(rows)!=0:
                            self.AdminTable.delete(*self.AdminTable.get_children())
                            for row in rows:
                                   self.AdminTable.insert('',END,values=row)
                     else:
                            messagebox.showerror("Error","No record found!!!",parent=self.root)              

       except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
if __name__=="__main__":      
    root=Tk()
    obj=adminclass(root)
    root.mainloop()      
