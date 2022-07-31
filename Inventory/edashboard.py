import tkinter
from tkinter import messagebox
import customtkinter
from tkinter import *
from employee import employeeclass
from mngattendance import AttendanceMng
import sqlite3
import os  
from logins import Login_system
from esalary import esalaryClass
import datetime
from attendance import calender
from erating import EmpRate
from task import taskClass

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self,eid):
        super().__init__()
        self.geometry("1350x700+0+0")
        self.title("Logged as Employee")


        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(
            master=self, width=180, corner_radius=0
        )
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(7, weight=1)  # empty row as spacing

        self.label_1 = customtkinter.CTkLabel(
            master=self.frame_left, text="Menu", text_font=("Roboto Medium", -16)
        )  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(
            master=self.frame_left, cursor="hand2",
            text="Employee", command=self.button_event
        )
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(
            master=self.frame_left, cursor="hand2",
            text="Salary", command=lambda:self.salary(eid)
        )
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(
            master=self.frame_left, cursor="hand2",
            text="Task", command=lambda:self.task(eid)
        )
        self.button_3.grid(row=4, column=0, pady=10, padx=20)

        self.button_4 = customtkinter.CTkButton(
            master=self.frame_left, cursor="hand2",
            text="Rating", command=lambda:self.Rating(eid)
        )
        self.button_4.grid(row=5, column=0, pady=10, padx=20)

        self.button_5 = customtkinter.CTkButton(
            master=self.frame_left, cursor="hand2",
            text="Attendance", command=lambda:self.Attendance(eid)
        )
        self.button_5.grid(row=6, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(
            master=self.frame_left, text="Appearance Mode:"
        )
        self.label_mode.grid(row=8, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(
            master=self.frame_left,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode,
        )
        self.optionmenu_1.grid(row=9, column=0, pady=10, padx=20, sticky="w")

        self.button_6 = customtkinter.CTkButton(
            master=self.frame_left,
            text="Logout",
            fg_color="red",
            cursor="hand2",
            height=30,
            command=self.logout,
        )
        self.button_6.grid(row=10, column=0, pady=10, padx=20)

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure(0, weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure(0, weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(
            row=0, column=0, columnspan=1, rowspan=1, pady=20, padx=20, sticky="nsew"
        )

        self.frame_list = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_list.grid(
            row=1, column=0, columnspan=3, rowspan=2, pady=20, padx=20, sticky="nsew"
        )

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.frame_list.rowconfigure((0,1), weight=1)
        self.frame_list.columnconfigure((0,1,2), weight=1)

        self.label_info_1 = customtkinter.CTkLabel(
            master=self.frame_info,
            text="Employee Management \t\t Date: DD-MM-YYYY \t\t Time: HH:MM:SS \t\t",
            corner_radius=6,  # <- custom corner radius
            fg_color=("white", "gray38"),  # <- custom tuple-color
            justify=tkinter.LEFT,
        )
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

        self.lbl_employee = customtkinter.CTkLabel(
            self.frame_list,
            height=150,
            fg_color=("white", "gray38"),
            text="Total Employee\n[ 0 ] ",
            text_font=("goudy old style", 20, "bold"),
        )
        self.lbl_employee.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

        self.lbl_supplier = customtkinter.CTkLabel(
            self.frame_list,
            height=150,
            fg_color=("white", "gray38"),
            text="Salary Info\n[ 0 ] ",
            bg="black",
            fg="white",
            text_font=("goudy old style", 20, "bold"),
        )
        self.lbl_supplier.grid(column=1, row=0, sticky="ew", padx=15, pady=15)

        self.lbl_category = customtkinter.CTkLabel(
            self.frame_list,
            height=150,
            fg_color=("white", "gray38"),
            text="Tasks \n[ 0 ] ",
            bg="black",
            fg="white",
            text_font=("goudy old style", 20, "bold"),
        )
        self.lbl_category.grid(column=2, row=0, sticky="ew", padx=15, pady=15)

        self.lbl_product = customtkinter.CTkLabel(
            self.frame_list,
            height=150,
            text="Employee present \n[ 0 ] ",
            relief=RIDGE,
            fg_color=("white", "gray38"),
            bg="black",
            fg="white",
            text_font=("goudy old style", 20, "bold"),
        )
        self.lbl_product.grid(column=0, row=1, sticky="ew",padx=15, pady=15)

        self.lbl_product = customtkinter.CTkLabel(
            self.frame_list,
            height=150,
            text="Employee absent \n[ 0 ] ",
            fg_color=("white", "gray38"),
            relief=RIDGE,
            bg="black",
            fg="white",
            text_font=("goudy old style", 20, "bold"),
        )
        self.lbl_product.grid(column=1, row=1, sticky="ew", padx=15, pady=15)

        self.lbl_sales = customtkinter.CTkLabel(
            self.frame_list,
            height=150,
            text="Attendance info \n[ 0 ] ",
            fg_color=("white", "gray38"),
            relief=RIDGE,
            bg="black",
            fg="white",
            text_font=("goudy old style", 20, "bold"),
        )
        self.lbl_sales.grid(column=2, row=1, sticky="ew", padx=15, pady=15)

        self.optionmenu_1.set("Dark")
        self.update_content()

        # ============ frame_right ============


    @staticmethod
    def button_event():
        print("Button pressed")

    @staticmethod
    def change_appearance_mode(new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()

    def employee(self):
        self.new_win=Toplevel(self)
        self.new_obj=employeeclass(self.new_win)

    def salary(self,eid):
        self.new_win=Toplevel(self)
        self.new_obj=esalaryClass(self.new_win,eid)

    def task(self,eid):
        self.new_win=Toplevel(self)
        self.new_obj=taskClass(self.new_win,eid)

    def Rating(self,eid):
        self.new_win=Toplevel(self)
        self.new_obj=EmpRate(self.new_win,eid)

    def Attendance(self,eid):
        self.new_win=Toplevel(self)
        self.new_obj=calender(self.new_win,eid)   

    def logout(self):
        self.label_info_1.after_cancel(self.update)
        self.destroy()
        root=customtkinter.CTk()
        obj=Login_system(root)
        root.mainloop()                       

    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()

        try:
           cur.execute("select * from employee")
           employee=cur.fetchall()
           self.lbl_employee.configure(text=f'Total Employee\n[{str(len(employee))}]')
           attendence=len(os.listdir('Inventory/attendence'))
           self.lbl_sales.configure(text=f'Attendance \n [{str(attendence)}]')

           now=datetime.datetime.now()

           self.label_info_1.configure(text=f'Employee Management System \t Time: {now.strftime("%I:%M:%S")}  \t Date: {now.strftime("%d-%m-%Y")}')
           self.update=self.label_info_1.after(200,self.update_content)

        except Exception as ex:
            print(ex)
            messagebox.showerror("Error",f'Error due to : {str(ex)}',parent=self)


if __name__ == "__main__":

    root=customtkinter.CTk()
    obj=Login_system(root)
    root.mainloop()
