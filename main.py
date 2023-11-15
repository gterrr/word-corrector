from textblob import TextBlob
from tkinter import *

def correct_spelling():
    get_data=enter1.get()
    corr=TextBlob(get_data)
    data=corr.correct()
    enter2.delete(0,END)
    enter2.insert(0,data)



  # this is for gui
def main_window():
    global enter1,enter2
    win=Tk()
    # this is specify the width and height
    win.geometry("500x400")
    # if u add this then u wont able to resize the window
    win.resizable(False,False)
    # this is use for make the bg color u can use HEX code or the rgb codes
    win.config(bg="#8458B3")
    win.title("checkar")

    # this for text "incorrect spelling"
    lable1=Label(win,text="Incorrect Spelling",font=("calbri",25,"bold"),bg="#a28089",fg="black")
    lable1.place(x=100,y=20,height=50,width=300)

    # this is for the text box
    enter1=Entry(win,font=("calbri",20))
    enter1.place(x=50,y=80,height=50,width=400)

    lable2=Label(win,text="Correct Spelling",font=("calbri",25,"bold"),bg="#a28089",fg="black")
    lable2.place(x=100,y=140,height=50,width=300)

    enter2=Entry(win,font=("calbri",20))
    enter2.place(x=50,y=200,height=50,width=400)

    button=Button(win,text="Done",font=("calbri",25,"bold"),bg="#d0bdf4",command=correct_spelling)
    button.place(x=150,y=280,height=50,width=200)
    # this is for recall the funtion
    win.mainloop()


    


main_window()
