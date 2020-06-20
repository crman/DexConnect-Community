from tkinter import *
import tkinter
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql

con = pymysql.connect(host="localhost", user="root",password="", database="dexcommunity")
cursor = con.cursor()

sql = "select * from resources"

cursor.execute(sql)

rows = cursor.fetchall()
total = cursor.rowcount

print("Total Entry",total)

class AvailResources:
    def __init__(self,root):
        self.root = root
        self.root.title("Add Resource")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg='white')

        #for adding background image
        self.bg = ImageTk.PhotoImage(file="Images/TechBackground.jpg")
        bg = Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)

        # for adding left image
        self.left = ImageTk.PhotoImage(file="Images/LeftImage.png")
        left = Label(self.root, image=self.left).place(x=0, y=80, width=630, height=700)


        #frame for adding the data
        frame1 = Frame(self.root,bg="#ffffff")
        frame1.place(x=630, y=80, width=1450, height=700)

        title = Label(frame1, text="EXISTING RESOURCES", font=("times new roman", 20, "bold"), bg="#ffffff", fg="#203864").place(x=50, y=30)

        btn_add_resources = Button(self.root, text="Add Resources",font=("times new roman", 15, "bold"), bg="#ffffff", fg="#203864", cursor="hand2", command=self.add_window).place(x=240, y=715)


        tv = ttk.Treeview(frame1)
        tv['columns'] = ("Column 1", "Column 2", "Column 3", "Column 4", "Column 5", "Column 6", "Column 7", "Column 8", "Column 9", "Column 10")
        tv.column("#0", width=0, minwidth=0)
        tv.column("Column 1", width=50, minwidth=10)
        tv.column("Column 2", width=100, minwidth=10)
        tv.column("Column 3", width=150, minwidth=10)
        tv.column("Column 4", width=0, minwidth=0)
        tv.column("Column 5", width=0, minwidth=0)
        tv.column("Column 6", width=100, minwidth=10)
        tv.column("Column 7", width=90, minwidth=10)
        tv.column("Column 8", width=150, minwidth=10)
        tv.column("Column 9", width=90, minwidth=10)
        tv.column("Column 10", width=150, minwidth=10)

        #defining column headings
        tv.heading("#0", text="")
        tv.heading("Column 1", text="ID")
        tv.heading(1, text="Shared by")
        tv.heading(2, text="Competition")
        tv.heading(3, text="Required Skills")
        tv.heading(4, text="Suggested Course")
        tv.heading(5, text="Time Duration")
        tv.heading(6, text="Designation")
        tv.heading(7, text="Comp./University Name")
        tv.heading(8, text="Experience")
        tv.heading(9, text="Linkedin URL")


        tv.pack(side=tkinter.LEFT, padx=10)      

        
        for i in rows:
            if i == 0:
                pass
            else:
                tv.insert("", 'end', values=i)
        

    def add_window(self):
        self.root.destroy()
        import AddResources

root = Tk()
MainFrame = AvailResources(root)
root.mainloop()