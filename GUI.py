from tkinter import *
import calendar

n = int(input("Enter the year: "))
text = calendar.calendar(n)
root = Tk()
root.geometry("550x600")
root.title("CALENDAR")
label1 = Label(root,text="MAHALAKSHMI",bg='dark gray',font=("consolas",28,'bold'))
label1.grid(row=1,column=1)
root.config(background="white")
l1=Label(root,text=text,font=("consolas",10,'bold'))
l1.grid(row=2,column=1,padx=10)
root.mainloop()