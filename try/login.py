import tkinter
import tkinter.messagebox
import customtkinter
from complex_example import App
import sqlite3


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class Login(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520
    def __init__(self):
        super().__init__()
        
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute(
                "Select eid from employee")
            rows= cur.fetchall()
            value=[]
            for row in rows:
                value.append(str(row[0]))
    
            print(value)
        except Exception as ex:
            print("Error", f"Error due to : {str(ex)}", parent=self.root)


        def combobox_callback(choice):
            print("combobox dropdown clicked:", choice)

        combobox = customtkinter.CTkComboBox(master=self,
                                            values=value,
                                            command=combobox_callback)
        combobox.pack(padx=20, pady=10)
        
    

if __name__ == "__main__":
    app = Login()
    app.mainloop()
