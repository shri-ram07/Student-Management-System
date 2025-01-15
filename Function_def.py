from tkinter import *


def about_command_function():
    About=Toplevel()
    About.title("About")
    About.geometry("755x241")
    About.maxsize(width=755, height=241)
    bg = PhotoImage(file=r"C:\Users\rauna\PycharmProjects\Student_UI\PNG\About.png")
    canvas1 = Canvas(About, width=755, height=241)
    canvas1.pack(fill=BOTH, expand=True)
    canvas1.create_image(0, 0, image = bg, anchor="nw")
    About.mainloop()

def Help_command_function():
    Help=Toplevel()
    Help.title("Help")
    Help.geometry("394x217")
    Help.maxsize(width=394, height=217)
    bg = PhotoImage(file=r"C:\Users\rauna\PycharmProjects\Student_UI\PNG\Help.png")
    canvas2=Canvas(Help,height=217,width=394)
    canvas2.pack(fill=BOTH, expand=True)
    canvas2.create_image(0,0,image=bg, anchor="nw")
    Help.mainloop()


def student_auth():
    pass
def teacher_auth():
    pass





#functions for converting photos to binary
def convert_to_binary(fileName):
    with open(fileName, 'rb') as file:
        bin = file.read()
    return bin
def convert_to_og(bin, filename):
    with open(filename, 'wb') as file:
        data = file.write(bin)
    return(filename)






