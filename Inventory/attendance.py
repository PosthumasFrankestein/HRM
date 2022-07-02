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
        now = cal.datetime.today()
        cal.calevent_create(now + cal.timedelta(days=-2), 'Reminder 1', 'absent')
        cal.calevent_create(now + cal.timedelta(days=3), 'Message', 'half')
        cal.tag_config('absent', background='red', foreground='yellow')
        cal.tag_config('half', background='yellow', foreground='red')

        cal.pack(pady = 20,fill="both",expand=True)

        #data
        self.var_date=StringVar()
        self.var_astatus="present"
        self.var_status="unapproved"
        self.var_remark=""
        self.var_eid=eid

        def present():
            dvalue=cal.get_date()
            date.config(text = "Attendence recorded for " + dvalue)
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                print("1")
                cur.execute("Select date from attendance where eid=?",(str(eid)))
                print("2")
                row=cur.fetchone()
                print(row[-1])
                if row[-1]==dvalue:
                        messagebox.showerror("Error","Today's attendance registered",parent=self.root)
                else:
                        dvalue=cal.get_date()
                        cur.execute("Insert into attendance (date,astatus,status,remark,eid) values(?,'present','unapproved','',?)",(dvalue,eid))       
                        con.commit()
                        messagebox.showinfo('Success',"Employee added Sucessfully",parent=self.root)
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