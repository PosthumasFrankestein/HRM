# Import Required Library
from tkinter import *
from tkinter import messagebox
from tkcalendar import *
import sqlite3
from logins import Login_system
import customtkinter

# Create Object
class calender:
    def __init__(self, root, eid):
        # Set geometry
        self.root = root
        root.geometry("600x450+300+160")
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()

        # Add Calendar
        cal = Calendar(
            root,
            firstweekday="sunday",
            weekenddays=[6, 7],
            showothermonthdays=True,
            showweeknumbers=False,
            font=("Times New Roman", 12),
            weekendbackground="#f51b1b",
            weekendforeground="white",
            selectmode="none",
            background="skyblue",
            selectbackground="skyblue",
            selectforeground="red",
            normalbackground="#f51b1b",
            normalforeground="white",
            othermonthforeground="white",
            othermonthbackground="white",
            othermonthweforeground="white",
            othermonthwebackground="white",
        )
        cur.execute(
            "Select date,astatus,status from attendance where eid=?", (str(eid))
        )
        days = cur.fetchall()
        for day in days:
            from datetime import datetime

            date = datetime.strptime(day[0], "%d/%m/%y").date()

            if day[1] == "present" and day[2] == "approve":
                cal.calevent_create(date, "Reminder 1", "present")
            elif day[1] == "half" or day[2] == "unapproved":
                cal.calevent_create(date, "Reminder 1", "half")
            else:
                cal.calevent_create(date, "Reminder 1", "present")

        
        cal.tag_config('absent', background='#f7163c', foreground='yellow')
        cal.tag_config('half', background='yellow', foreground='red')
        cal.tag_config('present', background='#50f01a', foreground='white')

        cal.pack(pady=20, fill="both", expand=True)

        # data

        self.var_eid = eid

        def present():
            now = cal.date.today()
            dvalue=now.strftime("%d/%m/%y")
            date.configure(text="Attendence recorded for " + dvalue)
            try:
                cur.execute("Select date from attendance where eid=? ORDER BY aid DESC",(str(eid)))
                row=cur.fetchone()
                if row is None or row[-1]!=dvalue:
                    # dvalue=cal.get_date()
                    cur.execute("Insert into attendance (date,astatus,status,remark,eid) values(?,'present','unapproved','',?)",(dvalue,eid))       
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Attendance Registered", parent=self.root
                    )
                else:
                    messagebox.showerror(
                        "Error",
                        "Today's attendance already registered",
                        parent=self.root,
                    )
            except Exception as ex:
                print(str(ex))
                messagebox.showerror(
                    "Error", f"Error due to : {str(ex)}", parent=self.root
                )

        # Add Button and Label
        Button(root, text="Make Present", bg="#4dfa16", command=present).pack(pady=0)

        date = Label(root, text="")
        date.pack(pady=0)

        # Execute Tkinter


if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = Login_system(root)
    root.mainloop()
