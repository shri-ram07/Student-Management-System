import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import filedialog as fd
from Function_def import *
import pyautogui
from PIL import Image, ImageTk
from database import *
import sys

class Main:
    def __init__(self):
        # Create main window
        self.pic = None
        self.fram_for_marksheet = None
        self.frame_for_detail_entry = None
        self.frame_for_mark_entry = None
        self.root = tk.Tk()
        self.root.title("Student Record App")
        self.root.geometry("1000x1000")
        self.root.minsize(width=1000, height=800)
        self.root.maxsize(width=1000, height=800)
        self.image2 = PhotoImage(file="C:\\Users\\rauna\\PycharmProjects\\Student_UI\\PNG\\icon.png")
        self.root.iconphoto(True, self.image2)
        self.root.resizable(width=False, height=False)
        self.main_menu = Menu(self.root)
        self.m1 = Menu(self.main_menu, tearoff=0)
        self.m1.add_command(label="About", command=about_command_function)
        self.m1.add_separator()
        self.m1.add_command(label="Help", command=Help_command_function)
        self.m1.add_separator()
        self.main_menu.add_cascade(label="Options", menu=self.m1)
        self.main_menu.add_command(label="Exit", command=exit)
        self.root.config(menu=self.main_menu)
        self.sql = Database()

        #data initialisation
        self.Name=None
        self.Class=None
        self.Roll_Number=None
        self.Group=None
        self.Gender=None
        self.Mobile=None
        self.Email=None
        self.Fathers_Name=None
        self.Mothers_Name=None
        self.Institute_Name=None




        # Initialize images
        self.image1 = tk.PhotoImage(file=r"C:\Users\rauna\PycharmProjects\Student_UI\PNG\background_image_main.png")
        self.image2 = tk.PhotoImage(file=r"C:\Users\rauna\PycharmProjects\Student_UI\PNG\frame1_back.png")
        self.image3 = tk.PhotoImage(file=r"C:\Users\rauna\PycharmProjects\Student_UI\PNG\soxwpkg2.png")
        self.image4 = tk.PhotoImage(file=r"C:\Users\rauna\PycharmProjects\Student_UI\PNG\frame_back.png")
        self.image5 = tk.PhotoImage(file=r"C:\Users\rauna\PycharmProjects\Student_UI\PNG\teacher back.png")
        self.image6 = tk.PhotoImage(file=r"C:\Users\rauna\PycharmProjects\Student_UI\PNG\dummy.png")
        self.image7 = PhotoImage(file=r"C:\Users\rauna\PycharmProjects\Student_UI\PNG\MarkSheet.png")

        # Call for frame 1 -----> Login
        self.login()
        self.root.mainloop()

    def login(self):
        self.frame_login_screen = Frame(self.root, width=1000, height=800, borderwidth=10, highlightbackground="black", highlightthickness=2)
        self.frame_login_screen.pack()  # This line will pack the frame into the root window

        label2 = Label(self.frame_login_screen, image=self.image3, anchor="center")
        label2.place(x=20, y=70)

        log_frame = Frame(self.frame_login_screen, width=400, height=700, borderwidth=10, highlightbackground="black", highlightthickness=2)
        log_frame.place(x=550, y=70)

        frame_back = Label(log_frame, image=self.image4, bg="black", fg="black")
        frame_back.pack()

        label1 = Label(self.frame_login_screen, text="Welcome to Student Record Interface", anchor="nw", font=("Brush Script MT", 30))
        label1.place(relx=0.19, rely=0)

        label2 = Label(log_frame, text="Sign-in", font=("Cooper Black", 22, "bold"), fg="#57a1f8", highlightbackground="black", highlightthickness=1)
        label2.place(relx=0.34, rely=0.009)

        label3 = Label(log_frame, text="Username - ", font=("Microsoft YaHei light", 11, "bold"), fg="#57a1f8", highlightbackground="black", highlightthickness=1)
        label3.place(x=5, y=150)

        label4 = Label(log_frame, text="Password - ", font=("Microsoft YaHei light", 11, "bold"), fg="#57a1f8", highlightbackground="black", highlightthickness=1)
        label4.place(x=5, y=200)

        self.entry1 = Entry(log_frame, font=("Microsoft YaHei light", 11, "bold"))
        self.entry1.place(x=150, y=150)

        self.entry2 = Entry(log_frame, font=("Microsoft YaHei light", 11, "bold"))
        self.entry2.place(x=150, y=200)

        def login_action():
            if self.sql.auth(self.entry1.get(), self.entry2.get()):
                self.m1 = messagebox.showinfo("Login Successfull",
                                              "Welcome to Student Record Teacher Interface 👍")
                self.id=self.entry1.get()
                self.password=self.entry2.get()
                # Clear login screen content
                self.frame_login_screen.pack_forget()
                # Show detail entry content
                self.detail_entry()
            else:
                self.m1 = messagebox.showinfo("Login Unsuccessfully",
                                              "Please enter correct details !!!")



        button1 = Button(log_frame, text="Sign In", font=("Microsoft YaHei light", 11, "bold"), command=login_action, bg="#57a1f8", fg="white")
        button1.place(relx=0.40, rely=0.4)

        label5 = Label(log_frame, text="* Contact us for creating User ID and Password *", font=("Brush Script MT", 10), highlightbackground="black", highlightthickness=1)
        label5.place(relx=0.13, rely=0.7)

    def detail_entry(self):
        self.frame_for_detail_entry = Frame(self.root, width=1000, height=800, borderwidth=10, highlightbackground="black", highlightthickness=2)
        self.frame_for_detail_entry.pack()  # This line will pack the frame into the root window
        teacher_Canvas = Canvas(self.frame_for_detail_entry, width=1000, height=800, highlightbackground="black",
                                highlightthickness=2)  # main canvas
        teacher_Canvas.pack()
        teacher_Canvas.create_image(0, 0, image=self.image5, anchor=NW)
        teacher_Canvas.create_text(230, 20, text="Welcome to Student Record Teacher Interface", anchor=NW,
                                   font=("Brush Script MT", 22))  # greeting text
        frame1 = Frame(teacher_Canvas, width=590, height=650, highlightbackground="Black", highlightthickness=0.5,
                       bg="#F0EBEF")  # big frame inside canvas
        teacher_Canvas.create_window(40, 100, window=frame1, anchor=NW)
        frame1.bg = Label(frame1, image=self.image2)
        frame1.bg.pack(fill=BOTH, expand=1)
        frame2 = Frame(teacher_Canvas, width=220, height=220, highlightbackground="Black",
                       highlightthickness=0.5)  # small frame inside canvas
        teacher_Canvas.create_window(740, 540, window=frame2, anchor=NW)
        frame3 = Frame(frame2, width=90, height=90, highlightbackground="black", highlightthickness=2,
                       bg="white")  # a frame inside a small frame for photo
        frame3.place(x=125, y=5)

        # frame1 Content

        # Labels
        l1 = Label(frame1, text="Student Details", font=("Microsoft YaHei light", 18, "bold"),
                   highlightbackground="black", highlightthickness=1, bg="#F0EBEF")
        l1.place(x=185, y=10)
        l2 = Label(frame1, text="Action -", font=("Microsoft YaHei light", 10, "bold"), highlightbackground="black",
                   highlightthickness=1, bg="#F0EBEF")
        l2.place(x=10, y=70)
        l3 = Label(frame1, text="Name -", font=("Microsoft YaHei light", 10, "bold"), highlightbackground="black",
                   highlightthickness=1, bg="#F0EBEF")
        l3.place(x=10, y=110)
        l4 = Label(frame1, text="Class -", font=("Microsoft YaHei light", 10, "bold"), highlightbackground="black",
                   highlightthickness=1, bg="#F0EBEF")
        l4.place(x=10, y=145)
        l5 = Label(frame1, text="Roll Number -", font=("Microsoft YaHei light", 10, "bold"),
                   highlightbackground="black", highlightthickness=1, bg="#F0EBEF")
        l5.place(x=10, y=180)
        l6 = Label(frame1, text="Group -", font=("Microsoft YaHei light", 10, "bold"), highlightbackground="black",
                   highlightthickness=1, bg="#F0EBEF")
        l6.place(x=10, y=215)
        l7 = Label(frame1, text="Gender -", font=("Microsoft YaHei light", 10, "bold"), highlightbackground="black",
                   highlightthickness=1, bg="#F0EBEF")
        l7.place(x=10, y=250)
        l8 = Label(frame1, text="Mobile -", font=("Microsoft YaHei light", 10, "bold"), highlightbackground="black",
                   highlightthickness=1, bg="#F0EBEF")
        l8.place(x=10, y=285)
        l9 = Label(frame1, text="Email -", font=("Microsoft YaHei light", 10, "bold"), highlightbackground="black",
                   highlightthickness=1, bg="#F0EBEF")
        l9.place(x=10, y=320)
        l10 = Label(frame1, text="Fathers Name -", font=("Microsoft YaHei light", 10, "bold"),
                    highlightbackground="black", highlightthickness=1, bg="#F0EBEF")
        l10.place(x=10, y=355)
        l11 = Label(frame1, text="Mothers Name -", font=("Microsoft YaHei light", 10, "bold"),
                    highlightbackground="black", highlightthickness=1, bg="#F0EBEF")
        l11.place(x=10, y=390)
        l12 = Label(frame1, text="School Name -", font=("Microsoft YaHei light", 10, "bold"),
                    highlightbackground="black", highlightthickness=1, bg="#F0EBEF")
        l12.place(x=10, y=425)

        # Buttons
        def req():
            var = c1.get()


            if var == "New Entry":
                def insert_data():
                    self.Name = E1.get()
                    self.Class = E2.get()
                    self.Roll_Number = E3.get()
                    self.Group = E4.get()
                    self.Gender = c2.get()
                    self.Mobile = E5.get()
                    self.Email = E6.get()
                    self.Fathers_Name = E7.get()
                    self.Mothers_Name = E8.get()
                    self.Institute_Name = E9.get()

                    self.frame_for_detail_entry.pack_forget()
                    self.mark_entry(
                        self.Name,
                        self.Class,
                        self.Roll_Number,
                        self.Group,
                        self.Gender,
                        self.Mobile,
                        self.Email,
                        self.Fathers_Name,
                        self.Mothers_Name,
                        self.Institute_Name,
                    )

                b2 = Button(frame1, text="Submit", font=("Bell MT", "10"), command=insert_data, bg="#57a1f8",
                            highlightbackground="black", highlightthickness=2)  # Next @2
                b2.place(x=250, y=500)
                l13 = Label(frame1, text="Photo (only png of 90x90px) -",
                            font=("Microsoft YaHei light", 10, "bold"), highlightbackground="black",
                            highlightthickness=1, bg="#F0EBEF")
                l13.place(x=10, y=460)

                def choose():
                    global img
                    f_type = [('PNG Files', "*.png")]
                    filename = fd.askopenfilename(filetypes=f_type)
                    self.f2l_img1 = PhotoImage(file=filename)
                    self.std_pic_for_sql = convert_to_binary(filename)

                bp = Button(frame1, text="Upload File", command=choose, bg="#57a1f8")
                bp.place(x=400, y=460)


            elif var == "Delete Entry":
                self.Roll_Number = E3.get()
                def delete_data():
                    self.sql.delete_std(self.Roll_Number)

                b2 = Button(frame1, text="Submit", font=("Bell MT", "10"), command=delete_data, bg="#57a1f8",
                            highlightbackground="black", highlightthickness=2)  # Next @2
                b2.place(x=250, y=500)

            elif var == "Data Visualisation":
                self.Roll_Number = E3.get()
                def show_data():

                    self.frame_for_detail_entry.pack_forget()
                    self.show_marksheet(self.Roll_Number)

                b2 = Button(frame1, text="Submit", font=("Bell MT", "10"), command=show_data, bg="#57a1f8",
                            highlightbackground="black", highlightthickness=2)  # Next @2
                b2.place(x=250, y=500)

        b1 = Button(frame1, text="NEXT", font=("Bell MT", "10"), command=req, bg="#57a1f8")
        b1.place(x=500, y=67)

        # Entries
        E1 = Entry(frame1, font=("Bell MT", "12", "bold"), width=30)
        E1.place(x=200, y=110)
        E2 = Entry(frame1, font=("Bell MT", "12", "bold"), width=30)
        E2.place(x=200, y=145)
        E3 = Entry(frame1, font=("Bell MT", "12", "bold"), width=30)
        E3.place(x=200, y=180)
        E4 = Entry(frame1, font=("Bell MT", "12", "bold"), width=30)
        E4.place(x=200, y=215)
        E5 = Entry(frame1, font=("Bell MT", "12", "bold"), width=30)
        E5.place(x=200, y=285)
        E6 = Entry(frame1, font=("Bell MT", "12", "bold"), width=30)
        E6.place(x=200, y=320)
        E7 = Entry(frame1, font=("Bell MT", "12", "bold"), width=30)
        E7.place(x=200, y=355)
        E8 = Entry(frame1, font=("Bell MT", "12", "bold"), width=30)
        E8.place(x=200, y=390)
        E9 = Entry(frame1, font=("Bell MT", "12", "bold"), width=30)
        E9.place(x=200, y=425)

        # combox
        c1 = Combobox(frame1, values=("New Entry", "Delete Entry", "Data Visualisation"),
                      font=("Bell MT", "10",), width=30)
        c1.place(x=100, y=70)
        c2 = Combobox(frame1, values=["Male", "Female", "Other"])
        c2.place(x=200, y=250)

        def clear():
            li = [E1, E2, E3, E4, E5, E6, E7, E8, E9]
            for i in li:
                i.delete(0, END)

        b3 = Button(frame1, text="Reset", command=clear, bg="#57a1f8")
        b3.place(x=259, y=600)

        # frame2 content
        data = self.sql.fetch_teach(self.id, self.password)
        userid = data[0]
        password = data[1]
        name = data[2]
        email = data[4]
        Post = data[5]
        photo = data[6]

        # Convert binary data to image file
        image_path = f"C:\\Users\\rauna\\PycharmProjects\\Student_UI\\Teacher_Pic\\{userid}.png"
        convert_to_og(photo,image_path)

        # Use Pillow to load the image
        image = Image.open(image_path)
        teacher_profile_pic = ImageTk.PhotoImage(image)
        teacher_profile = Label(frame3, image=teacher_profile_pic)
        teacher_profile.image = teacher_profile_pic
        teacher_profile.pack(fill=BOTH, expand=True)

        sl1 = Label(frame2, text=f"ID-{userid}", font=("Microsoft YaHei light", 7, "bold"))
        sl1.place(x=2, y=2)
        sl2 = Label(frame2, text=f"Pass-{password}", font=("Microsoft YaHei light", 7, "bold"))
        sl2.place(x=2, y=22)
        sl3 = Label(frame2, text=f"Name-{name}", font=("Microsoft YaHei light", 7, "bold"))
        sl3.place(x=2, y=121)
        sl4 = Label(frame2, text=f"Email-{email}", font=("Microsoft YaHei light", 7, "bold"))
        sl4.place(x=2, y=143)
        sl5 = Label(frame2, text=f"Post-{Post}", font=("Microsoft YaHei light", 7, "bold"))
        sl5.place(x=2, y=164)

        def logout():


            Logout_m = messagebox.showinfo("Logout Successfully",
                                           "Please Visit Again  ")
            self.frame_for_detail_entry.pack_forget()
            self.login()

        logout = Button(frame2, text="Logout", font=("Microsoft YaHei light", 7, "bold"), command=logout, bg="#57a1f8")
        logout.place(x=80, y=185)

    def mark_entry(self,
                   Name,
                   Class,
                   Roll_Number,
                   Group,
                   Gender,
                   Mobile,
                   Email,
                   Fathers_Name,
                   Mothers_Name,
                   Institute_Name,
                   ):
        self.frame_for_mark_entry = Frame(self.root, width=1000, height=800, borderwidth=10,
                                            highlightbackground="black", highlightthickness=2)
        self.frame_for_mark_entry.pack()  # This line will pack the frame into the root window
        Canvas1 = Canvas(self.frame_for_mark_entry, width=1000, height=800, highlightthickness=2,
                         highlightbackground="black")
        Canvas1.pack()
        Canvas1.create_text(300, 0, text="Student Marks", anchor=NW, font=("Wide Latin", 18))
        #Marksheet Background

        Canvas1.create_image(0, 0, image=self.image7, anchor=NW)

        f1 = Frame(Canvas1, width=330, height=160, highlightthickness=0.5,
                   highlightbackground="Black")
        f1.pack()
        Canvas1.create_window(50, 60, window=f1, anchor=NW)
        f2 = Frame(Canvas1, width=100, height=100, highlightthickness=0.5,
                   highlightbackground="Black")
        f2.pack()
        f2l = Label(f2, image=self.f2l_img1)
        f2l.pack()
        Canvas1.create_window(830, 60, window=f2, anchor=NW)
        f3 = Frame(Canvas1, width=900, height=320, highlightthickness=0.5,
                   highlightbackground="Black")
        f3.pack()
        Canvas1.create_window(50, 280, window=f3, anchor=NW)
        f4 = Frame(Canvas1, width=900, height=40, highlightthickness=0.5, highlightbackground="Black")
        f4.pack()
        Canvas1.create_window(50, 620, window=f4, anchor=NW)

        # frame1 content



        l1_for_marks = Label(f1, text=f"Name: {Name}", font=("Bell MT", 11, "bold"))
        l1_for_marks.place(x=10, y=10)
        l2_for_marks = Label(f1, text=f"Roll No.: {Roll_Number}", font=("Bell MT", 11, "bold"))
        l2_for_marks.place(x=10, y=30)
        l3_for_marks = Label(f1, text=f"Fathers Name: {Fathers_Name}",
                             font=("Bell MT", 11, "bold"))
        l3_for_marks.place(x=10, y=50)
        l4_for_marks = Label(f1, text=f"Mothers Name: {Mothers_Name}",
                             font=("Bell MT", 11, "bold"))
        l4_for_marks.place(x=10, y=70)
        l5_for_marks = Label(f1, text=f"Gender: {Gender}", font=("Bell MT", 11, "bold"))
        l5_for_marks.place(x=10, y=90)
        l6_for_marks = Label(f1, text=f"Institute: {Institute_Name}",
                             font=("Bell MT", 11, "bold"))
        l6_for_marks.place(x=10, y=110)
        l7_for_marks = Label(f1, text=f"Mobile No. : {Mobile}", font=("Bell MT", 11, "bold"))
        l7_for_marks.place(x=10, y=130)

        # Headings in Frame3

        result_canva = Canvas(f3, width=900, height=320)
        result_canva.pack()
        result_canva.create_rectangle(0, 0, 905, 40)  # Heading main
        result_canva.create_rectangle(0, 0, 240, 325)  # Subject column
        result_canva.create_text(115, 20, text="Subject", font=("bell mt", 15, "bold"))

        result_canva.create_rectangle(240, 0, 520, 325)  # UT 1 column
        result_canva.create_text(380, 20, text="Unit-I", font=("bell mt", 15, "bold"))
        result_canva.create_rectangle(520, 0, 800, 325)  # UT 2 column
        result_canva.create_text(660, 20, text="Unit-II", font=("bell mt", 15, "bold"))
        result_canva.create_text(850, 20, text="Total", font=("bell mt", 15, "bold"))

        # sub Headings
        result_canva.create_text(275, 55, text="I.A", font=("bell mt", 8, "bold"))
        result_canva.create_text(345, 55, text="Max Marks", font=("bell mt", 8, "bold"))
        result_canva.create_text(415, 55, text="Theory", font=("bell mt", 8, "bold"))
        result_canva.create_text(485, 55, text="Max Marks", font=("bell mt", 8, "bold"))
        result_canva.create_text(555, 55, text="I.A", font=("bell mt", 8, "bold"))
        result_canva.create_text(625, 55, text="Max Marks", font=("bell mt", 8, "bold"))
        result_canva.create_text(695, 55, text="Theory", font=("bell mt", 8, "bold"))
        result_canva.create_text(765, 55, text="Max Marks", font=("bell mt", 8, "bold"))

        result_canva.create_rectangle(240, 40, 800, 70)  # sub heading
        result_canva.create_rectangle(240, 40, 310, 325)
        result_canva.create_rectangle(310, 40, 380, 325)
        result_canva.create_rectangle(380, 40, 450, 325)
        result_canva.create_rectangle(450, 40, 520, 325)
        result_canva.create_rectangle(520, 40, 590, 325)
        result_canva.create_rectangle(590, 40, 660, 325)
        result_canva.create_rectangle(660, 40, 730, 325)
        result_canva.create_rectangle(730, 40, 800, 325)

        # Entry Widgets In frame 3
        result_canva.create_text(115, 110, text="English", font=("Microsoft JhengHei UI Light", 12))
        E_E1 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                     bg="#F0FF3E", textvariable=IntVar().set(0))
        result_canva.create_window(275, 110, window=E_E1)
        E_E1.insert(0, 0)
        E_E2 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                     bg="#F0FF3E", textvariable=IntVar().set(0))
        result_canva.create_window(345, 110, window=E_E2)
        E_E2.insert(0, 20)
        E_E3 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                     bg="#F0FF3E", textvariable=IntVar().set(0))
        result_canva.create_window(415, 110, window=E_E3)
        E_E3.insert(0, 0)
        E_E4 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                     bg="#F0FF3E", textvariable=IntVar().set(0))
        result_canva.create_window(485, 110, window=E_E4)
        E_E4.insert(0, 80)
        E_E5 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                     bg="#F0FF3E", textvariable=IntVar().set(0))
        result_canva.create_window(555, 110, window=E_E5)
        E_E5.insert(0, 0)
        E_E6 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                     bg="#F0FF3E", textvariable=IntVar().set(0))
        result_canva.create_window(625, 110, window=E_E6)
        E_E6.insert(0, 20)
        E_E7 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                     bg="#F0FF3E", textvariable=IntVar().set(0))
        result_canva.create_window(695, 110, window=E_E7)
        E_E7.insert(0, 0)
        E_E8 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                     bg="#F0FF3E", textvariable=IntVar().set(0))
        result_canva.create_window(765, 110, window=E_E8)
        E_E8.insert(0, 80)

        result_canva.create_text(115, 150, text="Maths", font=("Microsoft JhengHei UI Light", 12))
        Ma_E1 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                      bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(275, 150, window=Ma_E1)
        Ma_E1.insert(0, 0)
        Ma_E2 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                      bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(345, 150, window=Ma_E2)
        Ma_E2.insert(0, 20)
        Ma_E3 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                      bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(415, 150, window=Ma_E3)
        Ma_E3.insert(0, 0)
        Ma_E4 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                      bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(485, 150, window=Ma_E4)
        Ma_E4.insert(0, 80)
        Ma_E5 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                      bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(555, 150, window=Ma_E5)
        Ma_E5.insert(0, 0)
        Ma_E6 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                      bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(625, 150, window=Ma_E6)
        Ma_E6.insert(0, 20)
        Ma_E7 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                      bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(695, 150, window=Ma_E7)
        Ma_E7.insert(0, 0)
        Ma_E8 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                      bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(765, 150, window=Ma_E8)
        Ma_E8.insert(0, 80)

        result_canva.create_text(115, 190, text="Hindi", font=("Microsoft JhengHei UI Light", 12))
        H_E1 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                     bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(275, 190, window=H_E1)
        H_E1.insert(0, 0)
        H_E2 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                     bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(345, 190, window=H_E2)
        H_E2.insert(0, 20)
        H_E3 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                     bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(415, 190, window=H_E3)
        H_E3.insert(0, 0)
        H_E4 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                     bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(485, 190, window=H_E4)
        H_E4.insert(0, 80)
        H_E5 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                     bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(555, 190, window=H_E5)
        H_E5.insert(0, 0)
        H_E6 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                     bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(625, 190, window=H_E6)
        H_E6.insert(0, 20)
        H_E7 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                     bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(695, 190, window=H_E7)
        H_E7.insert(0, 0)
        H_E8 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                     bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(765, 190, window=H_E8)
        H_E8.insert(0, 80)

        result_canva.create_text(115, 230, text="Science", font=("Microsoft JhengHei UI Light", 12))
        Sc_E1 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                      bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(275, 230, window=Sc_E1)
        Sc_E1.insert(0, 0)
        Sc_E2 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                      bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(345, 230, window=Sc_E2)
        Sc_E2.insert(0, 20)
        Sc_E3 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                      bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(415, 230, window=Sc_E3)
        Sc_E3.insert(0, 0)
        Sc_E4 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                      bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(485, 230, window=Sc_E4)
        Sc_E4.insert(0, 80)
        Sc_E5 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                      bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(555, 230, window=Sc_E5)
        Sc_E5.insert(0, 0)
        Sc_E6 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                      bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(625, 230, window=Sc_E6)
        Sc_E6.insert(0, 20)
        Sc_E7 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                      bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(695, 230, window=Sc_E7)
        Sc_E7.insert(0, 0)
        Sc_E8 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                      bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(765, 230, window=Sc_E8)
        Sc_E8.insert(0, 80)

        result_canva.create_text(115, 270, text="Social Science", font=("Microsoft JhengHei UI Light", 12))
        Ss_E1 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                      bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(275, 270, window=Ss_E1)
        Ss_E1.insert(0, 0)
        Ss_E2 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                      bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(345, 270, window=Ss_E2)
        Ss_E2.insert(0, 20)
        Ss_E3 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                      bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(415, 270, window=Ss_E3)
        Ss_E3.insert(0, 0)
        Ss_E4 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                      bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(485, 270, window=Ss_E4)
        Ss_E4.insert(0, 80)
        Ss_E5 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                      bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(555, 270, window=Ss_E5)
        Ss_E5.insert(0, 0)
        Ss_E6 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                      bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(625, 270, window=Ss_E6)
        Ss_E6.insert(0, 20)
        Ss_E7 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                      bg="#F0FF3E", textvariable=IntVar)
        result_canva.create_window(695, 270, window=Ss_E7)
        Ss_E7.insert(0, 0)
        Ss_E8 = Entry(result_canva, highlightthickness=0.5, highlightbackground="black", width=8,
                      bg="#F0FF3E")
        result_canva.create_window(765, 270, window=Ss_E8)
        Ss_E8.insert(0, 80)

        def get():
            def calc_total(a, s, d, f, g, h, j, k):
                return round(((a + d + g + j) / 200) * 100, 2)

            t1e = calc_total(int((E_E1.get())), int((E_E2.get())), int((E_E3.get())),
                             int((E_E4.get())), int((E_E5.get())), int((E_E6.get())),
                             int((E_E7.get())), int((E_E8.get())))
            T_Re = Label(result_canva,
                         text=t1e,
                         font=('Microsoft JhengHei UI Light', 10, "bold"), highlightthickness=0.5,
                         highlightbackground="red")
            result_canva.create_window(850, 110, window=T_Re)

            t1m = calc_total(int((Ma_E1.get())), int((Ma_E2.get())), int((Ma_E3.get())),
                             int((Ma_E4.get())), int((Ma_E5.get())), int((Ma_E6.get())),
                             int((Ma_E7.get())), int((Ma_E8.get())))
            T_Rm = Label(result_canva,
                         text=t1m,
                         font=("Microsoft JhengHei UI Light", 10, "bold"), highlightthickness=0.5,
                         highlightbackground="red")
            result_canva.create_window(850, 150, window=T_Rm)

            t1h = calc_total(int((H_E1.get())), int((H_E2.get())), int((H_E3.get())),
                             int((H_E4.get())), int((H_E5.get())), int((H_E6.get())),
                             int((H_E7.get())), int((H_E8.get())))
            T_Rh = Label(result_canva,
                         text=t1h,
                         font=("Microsoft JhengHei UI Light", 10, "bold"), highlightthickness=0.5,
                         highlightbackground="red")
            result_canva.create_window(850, 190, window=T_Rh)

            t1sc = calc_total(int((Sc_E1.get())), int((Sc_E2.get())), int((Sc_E3.get())),
                              int((Sc_E4.get())), int((Sc_E5.get())), int((Sc_E6.get())),
                              int((Sc_E7.get())), int((Sc_E8.get())))
            T_Rsc = Label(result_canva,
                          text=t1sc,
                          font=("Microsoft JhengHei UI Light", 10, "bold"), highlightthickness=0.5,
                          highlightbackground="red")
            result_canva.create_window(850, 230, window=T_Rsc)

            t1ss = calc_total(int((Ss_E1.get())), int((Ss_E2.get())), int((Ss_E3.get())),
                              int((Ss_E4.get())), int((Ss_E5.get())), int((Ss_E6.get())),
                              int((Ss_E7.get())), int((Ss_E8.get())))
            T_Rss = Label(result_canva,
                          text=t1ss,
                          font=("Microsoft JhengHei UI Light", 10, "bold"), highlightthickness=0.5,
                          highlightbackground="red")
            result_canva.create_window(850, 270, window=T_Rss)

            # frame 4 content
            self.Total_obtained_marks = t1e + t1ss + t1sc + t1h + t1m
            self.percentage = (self.Total_obtained_marks / 500) * 100
            label_in_f4 = Label(f4,
                                text=f"Maximum Marks = 500  ,  Obtained Marks = {self.Total_obtained_marks} , Percentage = {self.percentage} %",
                                font=("bell mt", 15, "bold"))
            label_in_f4.place(x=0, y=0)

        tt_button = Button(result_canva, text="Get", highlightthickness=0.5,
                           highlightbackground="black",
                           command=get, bg="red", width=10)
        result_canva.create_window(850, 305, window=tt_button)

        #Back Button
        def back():
            self.frame_for_mark_entry.pack_forget()
            # Show detail entry content
            self.detail_entry()

        back_button = Button(Canvas1, text="Back", width=10, font=("bell mt", 8, "bold"),
                               bg="yellow",
                               fg='Black', command=back)
        Canvas1.create_window(400, 750, window=back_button)

        def sub():
            values = (
                self.Roll_Number,
                self.Name,
                self.Fathers_Name,
                self.Mothers_Name,
                self.Gender,
                self.Mobile,
                self.Email,
                self.Class + self.Group,
                self.Institute_Name,
                self.std_pic_for_sql,
                E_E1.get(),
                E_E5.get(),
                E_E3.get(),
                E_E7.get(),
                Ma_E1.get(),
                Ma_E5.get(),
                Ma_E3.get(),
                Ma_E7.get(),
                H_E1.get(),
                H_E5.get(),
                H_E3.get(),
                H_E7.get(),
                Sc_E1.get(),
                Sc_E5.get(),
                Sc_E3.get(),
                Sc_E7.get(),
                Ss_E1.get(),
                Ss_E5.get(),
                Ss_E3.get(),
                Ss_E7.get(),
                "500",
                self.Total_obtained_marks,
                self.percentage
            )
            self.sql.entry_std(values,self.Roll_Number)

            self.frame_for_mark_entry.pack_forget()
            # Show detail entry content
            self.detail_entry()



        submit_button = Button(Canvas1, text="Submit", width=10, font=("bell mt", 8, "bold"),
                               bg="blue",
                               fg='Black', command=sub)
        Canvas1.create_window(600, 750, window=submit_button)
    def show_marksheet(self,roll):
        data=self.sql.fetch_std(roll)
        if len(data)>0:
            self.frame_for_marksheet = Frame(self.root,width=1000, height=800, borderwidth=10, highlightbackground="black", highlightthickness=2)
            self.frame_for_marksheet.pack()  # This line will pack the frame into the root window

            Canvas1 = Canvas(self.frame_for_marksheet, width=1000, height=800, highlightthickness=2, highlightbackground="black")
            Canvas1.pack()
            Canvas1.create_text(300, 0, text="Student Marks", anchor=NW, font=("Wide Latin", 18))
            Canvas1.create_image(0, 0, image=self.image7, anchor=NW)

            f1 = Frame(Canvas1, width=330, height=160, highlightthickness=0.5, highlightbackground="Black")
            f1.pack()
            Canvas1.create_window(50, 60, window=f1, anchor=NW)
            f2 = Frame(Canvas1, width=100, height=100, highlightthickness=0.5, highlightbackground="Black")
            f2.pack()
            image_path = convert_to_og(data[9],
                                       f"C:\\Users\\rauna\\PycharmProjects\\Student_UI\\student_pic\\{self.Roll_Number}.png")
            print(image_path)
            if image_path:
                image = Image.open(image_path)
                self.pic = ImageTk.PhotoImage(image)
                f2l = Label(f2, image=self.pic)
                f2l.pack()
            else:
                print("Error in converting binary data to image.")

            Canvas1.create_window(830, 60, window=f2, anchor=NW)
            f3 = Frame(Canvas1, width=900, height=320, highlightthickness=0.5, highlightbackground="Black")
            f3.pack()
            Canvas1.create_window(50, 280, window=f3, anchor=NW)
            f4 = Frame(Canvas1, width=900, height=40, highlightthickness=0.5, highlightbackground="Black")
            f4.pack()
            Canvas1.create_window(50, 620, window=f4, anchor=NW)

            # frame1 content

            l1_for_marks = Label(f1, text=f"Name: {data[1]}", font=("Bell MT", 11, "bold"))
            l1_for_marks.place(x=10, y=10)
            l2_for_marks = Label(f1, text=f"Roll No.: {data[0]}", font=("Bell MT", 11, "bold"))
            l2_for_marks.place(x=10, y=30)
            l3_for_marks = Label(f1, text=f"Fathers Name: {data[2]}", font=("Bell MT", 11, "bold"))
            l3_for_marks.place(x=10, y=50)
            l4_for_marks = Label(f1, text=f"Mothers Name: {data[3]}", font=("Bell MT", 11, "bold"))
            l4_for_marks.place(x=10, y=70)
            l5_for_marks = Label(f1, text=f"Gender: {data[4]}", font=("Bell MT", 11, "bold"))
            l5_for_marks.place(x=10, y=90)
            l6_for_marks = Label(f1, text=f"Institute: {data[8]}", font=("Bell MT", 11, "bold"))
            l6_for_marks.place(x=10, y=110)
            l7_for_marks = Label(f1, text=f"Mobile No. : {data[5]}", font=("Bell MT", 11, "bold"))
            l7_for_marks.place(x=10, y=130)

            # Headings in Frame3

            result_canva = Canvas(f3, width=900, height=320)
            result_canva.pack()
            result_canva.create_rectangle(0, 0, 905, 40)  # Heading main
            result_canva.create_rectangle(0, 0, 240, 325)  # Subject column
            result_canva.create_text(115, 20, text="Subject", font=("bell mt", 15, "bold"))

            result_canva.create_rectangle(240, 0, 520, 325)  # UT 1 column
            result_canva.create_text(380, 20, text="Unit-I", font=("bell mt", 15, "bold"))
            result_canva.create_rectangle(520, 0, 800, 325)  # UT 2 column
            result_canva.create_text(660, 20, text="Unit-II", font=("bell mt", 15, "bold"))
            result_canva.create_text(850, 20, text="Total", font=("bell mt", 15, "bold"))

            # sub Headings
            result_canva.create_text(275, 55, text="I.A", font=("bell mt", 8, "bold"))
            result_canva.create_text(345, 55, text="Max Marks", font=("bell mt", 8, "bold"))
            result_canva.create_text(415, 55, text="Theory", font=("bell mt", 8, "bold"))
            result_canva.create_text(485, 55, text="Max Marks", font=("bell mt", 8, "bold"))
            result_canva.create_text(555, 55, text="I.A", font=("bell mt", 8, "bold"))
            result_canva.create_text(625, 55, text="Max Marks", font=("bell mt", 8, "bold"))
            result_canva.create_text(695, 55, text="Theory", font=("bell mt", 8, "bold"))
            result_canva.create_text(765, 55, text="Max Marks", font=("bell mt", 8, "bold"))

            result_canva.create_rectangle(240, 40, 800, 70)  # sub heading
            result_canva.create_rectangle(240, 40, 310, 325)
            result_canva.create_rectangle(310, 40, 380, 325)
            result_canva.create_rectangle(380, 40, 450, 325)
            result_canva.create_rectangle(450, 40, 520, 325)
            result_canva.create_rectangle(520, 40, 590, 325)
            result_canva.create_rectangle(590, 40, 660, 325)
            result_canva.create_rectangle(660, 40, 730, 325)
            result_canva.create_rectangle(730, 40, 800, 325)

            # Entry Widgets In frame 3
            result_canva.create_text(115, 110, text="English", font=("Microsoft JhengHei UI Light", 12))

            result_canva.create_text(275, 110, text=data[10], font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(345, 110, text="20", font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(415, 110, text=data[11], font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(485, 110, text="80", font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(555, 110, text=data[12], font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(625, 110, text="20", font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(695, 110, text=data[13], font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(765, 110, text="80", font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(115, 150, text="Maths", font=("Microsoft JhengHei UI Light", 12))

            result_canva.create_text(275, 150, text=data[14], font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(345, 150, text="20", font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(415, 150, text=data[15], font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(485, 150, text="80", font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(555, 150, text=data[16], font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(625, 150, text="20", font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(695, 150, text=data[17], font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(765, 150, text="80", font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(115, 190, text="Hindi", font=("Microsoft JhengHei UI Light", 12))

            result_canva.create_text(275, 190, text=data[18], font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(345, 190, text="20", font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(415, 190, text=data[19], font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(485, 190, text="80", font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(555, 190, text=data[20], font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(625, 190, text="20", font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(695, 190, text=data[21], font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(765, 190, text="80", font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(115, 230, text="Science", font=("Microsoft JhengHei UI Light", 12))

            result_canva.create_text(275, 230, text=data[22], font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(345, 230, text="20", font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(415, 230, text=data[23], font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(485, 230, text="80", font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(555, 230, text=data[24], font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(625, 230, text="20", font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(695, 230, text=data[25], font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(765, 230, text="80", font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(115, 270, text="Social Science", font=("Microsoft JhengHei UI Light", 12))

            result_canva.create_text(275, 270, text=data[26], font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(345, 270, text="20", font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(415, 270, text=data[27], font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(485, 270, text="80", font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(555, 270, text=data[28], font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(625, 270, text="20", font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(695, 270, text=data[29], font=("Microsoft JhengHei UI Light", 9))

            result_canva.create_text(765, 270, text="80", font=("Microsoft JhengHei UI Light", 9))

            def calc_total(a, d, g, j):
                return round(((a + d + g + j) / 200) * 100, 2)

            t1e = calc_total(int((data[10])), int((data[11])), int((data[12])),
                             int((data[13])))
            T_Re = Label(result_canva,
                         text=t1e,
                         font=("Microsoft JhengHei UI Light", 10, "bold"), highlightthickness=0.5,
                         highlightbackground="red")
            result_canva.create_window(850, 110, window=T_Re)

            t1m = calc_total(int((data[14])), int((data[15])),
                             int((data[16])), int((data[17])))
            T_Rm = Label(result_canva,
                         text=t1m,
                         font=("Microsoft JhengHei UI Light", 10, "bold"), highlightthickness=0.5,
                         highlightbackground="red")
            result_canva.create_window(850, 150, window=T_Rm)

            t1h = calc_total(int((data[18])), int((data[19])), int((data[20])),
                             int((data[21])))
            T_Rh = Label(result_canva,
                         text=t1h,
                         font=("Microsoft JhengHei UI Light", 10, "bold"), highlightthickness=0.5,
                         highlightbackground="red")
            result_canva.create_window(850, 190, window=T_Rh)

            t1sc = calc_total(int((data[22])), int((data[23])), int((data[24])),
                              int((data[25])))
            T_Rsc = Label(result_canva,
                          text=t1sc,
                          font=("Microsoft JhengHei UI Light", 10, "bold"), highlightthickness=0.5,
                          highlightbackground="red")
            result_canva.create_window(850, 230, window=T_Rsc)

            t1ss = calc_total(int((data[26])), int((data[27])), int((data[28])),
                              int((data[29])))
            T_Rss = Label(result_canva,
                          text=t1ss,
                          font=("Microsoft JhengHei UI Light", 10, "bold"), highlightthickness=0.5,
                          highlightbackground="red")
            result_canva.create_window(850, 270, window=T_Rss)

            # frame 4 content
            Total_obtained_marks = t1e + t1ss + t1sc + t1h + t1m
            percentage = (Total_obtained_marks / 500) * 100
            label_in_f4 = Label(f4,
                                text=f"Maximum Marks = 500  ,  Obtained Marks = {Total_obtained_marks} , Percentage = {percentage} %",
                                font=("bell mt", 15, "bold"))
            label_in_f4.place(x=0, y=0)

            def takeScreenshot():
                # Get the region of the canvas
                x, y = Canvas1.winfo_rootx(), Canvas1.winfo_rooty()
                w, h = Canvas1.winfo_width(), Canvas1.winfo_height()

                # Capture the screenshot within the canvas region
                pyautogui.screenshot(
                    f'C:\\Users\\rauna\PycharmProjects\\Student_UI\\student_marksheet\\{data[1]}_Marksheet.png',
                    region=(x, y, w, h))
                msgdel = messagebox.showinfo("Marksheet Saved Successfully ",
                                             f"Location : 'C:\\Users\\rauna\PycharmProjects\\Student_UI\\student_marksheet\\{data[1]}_Marksheet.png")

                # Back Button

            def back():
                self.frame_for_marksheet.pack_forget()
                # Show detail entry content
                self.detail_entry()

            back_button = Button(Canvas1, text="Back", width=10, font=("bell mt", 8, "bold"),
                                 bg="yellow",
                                 fg='Black', command=back)
            Canvas1.create_window(400, 750, window=back_button)
            print_button = Button(Canvas1, text="Print", width=10, font=("bell mt", 8, "bold"), bg="blue",
                                  fg='Black', command=takeScreenshot)
            Canvas1.create_window(600, 750, window=print_button)
        else:

            self.error2 = messagebox.showinfo("ERROR",
                                              "Data Not Foundt !")

            # Show detail entry content
            self.detail_entry()

if __name__ == "__main__":
    obj = Main()
