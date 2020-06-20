from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql

class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Add Resource")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg='white')

        #for adding background image
        self.bg = ImageTk.PhotoImage(file="Images/TechBackground.jpg")
        bg = Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)

        #for adding left image
        self.left = ImageTk.PhotoImage(file="Images/LeftImage.png")
        left = Label(self.root, image=self.left).place(x=0, y=80, width=630, height=700)

        #frame for adding the data
        frame1 = Frame(self.root,bg="#ffffff")
        frame1.place(x=630, y=80, width=850, height=700)

        title = Label(frame1, text="ADD RESOURCES HERE", font=("times new roman", 20, "bold"), bg="#ffffff", fg="#203864").place(x=50, y=30)

        #row1
        f_name = Label(frame1, text="Enter Name", font=("times new roman", 15, "bold"), bg="#ffffff", fg="#203864").place(x=50, y=100)
        self.txt_fname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_fname.place(x=50, y=130, width=300)

        competition_name = Label(frame1, text="Enter Competition Name", font=("times new roman", 15, "bold"), bg="#ffffff", fg="#203864").place(x=470, y=100)
        self.txt_competition_name = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_competition_name.place(x=470, y=130, width=300)

        #row2
        required_skills = Label(frame1, text="Required Skils", font=("times new roman", 15, "bold"), bg="#ffffff", fg="#203864").place(x=50, y=190)
        self.txt_required_skills = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_required_skills.place(x=50, y=220, width=300)

        Suggested_courses = Label(frame1, text="Enter Suggested Courses", font=("times new roman", 15, "bold"), bg="#ffffff", fg="#203864").place(x=470, y=190)
        self.txt_suggested_courses = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_suggested_courses.place(x=470, y=220, width=300)

        #row3
        duration = Label(frame1, text="Approx Duration of Competition", font=("times new roman", 15, "bold"), bg="#ffffff", fg="#203864").place(x=50, y=280)
        self.txt_duration = Entry(frame1, font=("times new roman", 13), bg="lightgray")
        self.txt_duration.place(x=50, y=310, width=300)

        designation = Label(frame1, text="Select Designation", font=("times new roman", 15, "bold"), bg="#ffffff", fg="#203864").place(x=470, y=280)
        self.txt_designation = Entry(frame1, font=("times new roman", 13), bg="lightgray")
        self.txt_designation.place(x=470, y=310, width=300)

        #row4
        company_name = Label(frame1, text="Name of Company/University", font=("times new roman", 15, "bold"), bg="#ffffff", fg="#203864").place(x=50, y=370)
        self.txt_company_name = Entry(frame1, font=("times new roman", 13), bg="lightgray")
        self.txt_company_name.place(x=50, y=400, width=300)

        experience = Label(frame1, text="Experience(in years)", font=("times new roman", 15, "bold"), bg="#ffffff", fg="#203864").place(x=470, y=370)
        self.txt_experience = Entry(frame1, font=("times new roman", 13), bg="lightgray")
        self.txt_experience.place(x=470, y=400, width=300)

        #row5
        linked_in = Label(frame1, text="LinkedIn Profile Link", font=("times new roman", 15, "bold"), bg="#ffffff", fg="#203864").place(x=50, y=460)
        self.txt_linkedin = Entry(frame1, font=("times new roman", 13), bg="lightgray")
        self.txt_linkedin.place(x=50, y=490, width=300)

        #Terms and condition checkbox
        self.var_chk = IntVar()
        chk= Checkbutton(frame1,text='I Agree The Terms & Conditions',variable=self.var_chk, onvalue=1, offvalue=0, bg="#ffffff", fg="#203864", font=("times new roman", 15, "bold")).place(x=50, y=560)

        btn_register = Button(frame1, text="Submit",font=("times new roman", 13), bg="#203864", fg="#ffffff", cursor="hand2", command=self.register_data).place(x=50, y=600, width=200)

        btn_existing_resources = Button(self.root, text="Check Existing Resource",font=("times new roman", 15, "bold"), bg="#ffffff", fg="#203864", cursor="hand2", command=self.resources_window).place(x=197, y=715)

    
    def resources_window(self):
        self.root.destroy()
        import AvailableResources

    
    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_competition_name.delete(0, END)
        self.txt_required_skills.delete(0, END)
        self.txt_suggested_courses.delete(0, END)
        self.txt_duration.delete(0, END)
        self.txt_designation.delete(0, END)
        self.txt_company_name.delete(0, END)
        self.txt_experience.delete(0, END)
        self.txt_linkedin.delete(0, END)
    
    
    def register_data(self):
        #print(self.var_fname.get(), self.txt_competition_name.get())
        if self.txt_fname.get() == "" or self.txt_competition_name.get() == "" or self.txt_company_name.get() == "" or self.txt_designation.get() == "" or self.txt_experience.get() == "" or self.txt_required_skills.get() == "" or self.txt_duration.get() == "" or self.txt_suggested_courses.get() == "" or self.txt_linkedin.get() == "" :
            messagebox.showerror("Error", "All fields must required", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please agree our terms and conditions", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root",password="", database="dexcommunity")

                cur = con.cursor()

                cur.execute("insert into resources (f_name, competition_name, required_skills, Suggested_courses, duration, designation, company_name, experience, linked_in) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (self.txt_fname.get(),
                            self.txt_competition_name.get(),
                            self.txt_required_skills.get(),
                            self.txt_suggested_courses.get(),
                            self.txt_duration.get(),
                            self.txt_designation.get(),
                            self.txt_company_name.get(),
                            self.txt_experience.get(),
                            self.txt_linkedin.get()
                        ))
                con.commit()
                con.close()

                messagebox.showinfo("Success", "Resources added successfully!", parent=self.root)
                self.clear()

            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)
                




root = Tk()
MainFrame = Register(root)
root.mainloop()