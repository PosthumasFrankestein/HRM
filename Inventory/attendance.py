# Import Required Library
from tkinter import *
from tkinter import messagebox
from tkcalendar import *
import sqlite3
from logins import Login_system

# Create Object
class calender:
    def __init__(self,root,eid):
        # Set geometry
        self.root=root
        root.geometry('600x450+300+160')
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
            
        # Add Calendar
        cal = Calendar(root,firstweekday="sunday",
        weekenddays=[6,7], 
        showothermonthdays=False,
        showweeknumbers=False,
        weekendbackground="white",
        weekendforeground="red",
        selectmode="none",
        background="skyblue",
        selectbackground="skyblue",
        selectforeground="white"
        )
        cur.execute("Select date,astatus from attendance where eid=?",(str(eid)))
        days=cur.fetchall()
        for day in days:
            from datetime import datetime

            date = datetime.strptime(day[0], '%m/%d/%y').date()


            if day[1]=='present':
                cal.calevent_create(date, 'Reminder 1', 'present')

        now = cal.datetime.today()
        cal.calevent_create(now + cal.timedelta(days=-2), 'Reminder 1', 'absent')
        # cal.calevent_create(now + cal.timedelta(days=3), 'Message', 'half')
        cal.tag_config('absent', background='red', foreground='yellow')
        cal.tag_config('half', background='yellow', foreground='red')
        cal.tag_config('present', background='green', foreground='white')

        cal.pack(pady = 20,fill="both",expand=True)

        #data
        
        self.var_eid=eid

        def present():
            dvalue=cal.get_date()
            date.config(text = "Attendence recorded for " + dvalue)
            try:
                cur.execute("Select date from attendance where eid=?  ORDER BY aid DESC",(str(eid)))
                row=cur.fetchone()
                if row==None or row[-1]!=dvalue:
                    dvalue=cal.get_date()
                    cur.execute("Insert into attendance (date,astatus,status,remark,eid) values(?,'present','unapproved','',?)",(dvalue,eid))       
                    con.commit()
                    messagebox.showinfo('Success',"Attendance Registered",parent=self.root)
                else:
                    messagebox.showerror("Error","Today's attendance already registered",parent=self.root)
            except Exception as ex:
                print(str(ex))
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

        # Add Button and Label
        Button(root, text = "Make Present",bg="#4dfa16",
            command = present).pack(pady = 0)

        date = Label(root, text = "")
        date.pack(pady = 0)

        # Execute Tkinter
        root.mainloop()

if __name__=="__main__":      
    root=Tk()
    # obj=calender(root)
    obj=Login_system(root)
    root.mainloop()