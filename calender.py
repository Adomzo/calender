from tkinter import *
import calendar
screen = Tk()
screen.config(background='blue')
screen.title('calender app')
screen.geometry('400x300')
def showcalender():
    screen2 = Tk()
    screen2.config(background='blue')
    screen2.title('calender app')
    screen2.geometry('850x1000')
    fetch_yr=int(year.get())
    calendertext=calendar.calendar(fetch_yr)
    calendercontent=Label(screen2,text=calendertext,font=('arial',20))
    calendercontent.grid(row=6,column=1,padx=50)
app=Label(screen,text='Calender App',bg = 'blue',font=('arial',40,'bold'))
app.grid(row=1,column =1, padx=45,pady=30)
question= Label(screen,text='Enter any year: ',bg='blue',font=('times',20))
question.grid(row=2,column=1,pady=10)
year = Entry(screen,bg='black')
year.grid(row=3,column=1,pady=10)
button = Button(screen,text='SUBMIT',fg='green',bg='black',command=showcalender)
button.grid(row=4,column=1)
exitbtn=Button(screen,text='EXIT',bg='black',fg='red',command=exit)
exitbtn.grid(row=5,column=1,pady=15)
screen.mainloop()
