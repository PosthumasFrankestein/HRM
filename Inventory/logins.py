from tkinter import *
import sqlite3
from tkinter import messagebox
import customtkinter 


customtkinter.set_appearance_mode("system")

class Login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.eid=StringVar()
        self.password=StringVar()
        self.utype=StringVar()

        login_frame=customtkinter.CTkFrame(self.root,bd=2,relief=RIDGE,fg_color="white")
        login_frame.place(x=520,y=90,width=350,height=460)


        title=Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)


        lbl_user=Label(login_frame,text="Employee ID",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        txt_username=Entry(login_frame,textvariable=self.eid,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)
        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=200)
        txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250)
        btn_login= customtkinter.CTkButton(login_frame,
                                 width=250,
                                 height=35,
                                 border_width=0,
                                 corner_radius=8,
                                 fg_color="blue",
                                 hover_color="green",
                                 text="Log In",
                                 command=self.login).place(x=50,y=300)

    def login(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()

        try:
            if self.eid.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("select utype,eid from employee where eid=? AND pass=?",(self.eid.get(),self.password.get()))
                user=cur.fetchone()
                if user is None:
                    messagebox.showerror("Error","Invalid username/password",parent=self.root)
                elif user[0]=='Admin':
                    eid=user[1]
                    from dashboard import App
                    self.root.destroy()
                    app=App(eid)
                    app.mainloop()
                else:
                    eid=user[1]
                    from edashboard import App
                    self.root.destroy()
                    app=App(eid)
                    app.mainloop()  
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to : {str(ex)}',parent=self.root)           

if __name__=="__main__":
    root=customtkinter.CTk()
    obj=Login_system(root)
    root.mainloop()
