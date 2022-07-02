from tkinter import *
import sqlite3
from tkinter import messagebox
import os


class Login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        self.eid=StringVar()
        self.password=StringVar()
        self.utype=StringVar()

        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=520,y=90,width=350,height=460)

        
        title=Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)


        lbl_user=Label(login_frame,text="Employee ID",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        txt_username=Entry(login_frame,textvariable=self.eid,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)
        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=200)
        txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250)
        btn_login=Button(login_frame,command=self.login,text="Log In",font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)

    
    def login(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()

        try:
            if self.eid.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("select utype,eid from employee where eid=? AND pass=?",(self.eid.get(),self.password.get()))
                user=cur.fetchone()
                eid=user[1]
                if user==None:
                    messagebox.showerror("Error","Invalid username/password",parent=self.root)
                elif user[0]=='Admin':
                    from dashboard import EMS
                    self.root.destroy()
                    root=Tk()
                    obj=EMS(root)
                    root.mainloop()
                else:
                    from edashboard import EMS
                    self.root.destroy()
                    root=Tk()
                    obj=EMS(root,eid)
                    root.mainloop()  
                                            
                    
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to : {str(ex)}',parent=self.root)           

if __name__=="__main__":
    root=Tk()
    obj=Login_system(root)
    root.mainloop()