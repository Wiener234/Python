import tkinter as tk
from tkinter import messagebox
from tkinter.colorchooser import askcolor
import pyautogui

def Choose():
    framechose.lift()


def Calculator():
    frame1.lift()

def pick_a_color():
    print(askcolor(title='Pick a color'))

def addition():
    op1 = float(operator1.get())
    op2 = float(operator2.get())

    ergebniss = op1 + op2

    ergebnissLabel.config(text=str(ergebniss))


def subtraktion():
    op1 = float(operator1.get())
    op2 = float(operator2.get())

    ergebniss = op1 - op2

    ergebnissLabel.config(text= str(ergebniss))

def multiplikation():
    op1 = float(operator1.get())
    op2 = float(operator2.get())

    ergebniss = op1 * op2

    ergebnissLabel.config(text= str(ergebniss))

def division():
    op1 = float(operator1.get())
    op2 = float(operator2.get())

    try:
        ergebniss = op1 / op2
        ergebnissLabel.config(text=str(ergebniss))
    except:
        messagebox.showwarning("Math. Error", "You can´t divide with 0")


def quadrieren():
    op1 = float(operator1.get())
    op2 = float(operator2.get())

    ergebniss = op1**op2

    ergebnissLabel.config(text= str(ergebniss))

def wurzel():
    op1 = float(operator1.get())
    op2 = float(operator2.get())

    try:
        ergebniss = op2**(1/op1)
        ergebnissLabel.config(text=str(ergebniss))
    except:
        messagebox.showwarning("Math. Error", "Op2 can´t be negative.")


def Save():
    password = str(passwort.get())
    username1 = str(username.get())
    file = open(r'C:\Users\nilsb\Documents\unins1111',"w")
    file.write(password)
    file.write("\n")
    file.write(username1)
    file.close()

def Load():
    userpassword = str(passwort.get())
    userusername = str(username.get())

    file = open(r'C:\Users\nilsb\Documents\unins1111',"r")
    password = file.readline()
    username1 = file.readline()


    if password == userpassword + "\n":
        if username1 == userusername:
            Choose()
        else:
            messagebox.showerror('Error', 'Username or password is wrong.')
    else:
            messagebox.showerror('Error', 'Username or password is wrong.')
    file.close()

def ImageLogin():
    if pyautogui.locateOnScreen('loginimage.png', confidence=0.9):
        Choose()
    else:
        messagebox.showerror('Error', 'Cant finde Image.')





#Window

root = tk.Tk()

root.geometry("175x170")
root.resizable(0, 0)
root.title("")
root.iconbitmap('icon_dLogin.ico')

#Frames
framenew =tk.Frame(root)
frame1 =tk.Frame(root)
framecolorpicker = tk.Frame(root)
framechose = tk.Frame(root)

framenew.lift()
#Frame0
passwortlabel = tk.Label(framenew, text= 'Passwort')
usernamelabel = tk.Label(framenew, text= 'Username')
username = tk.Entry(framenew)
passwort = tk.Entry(framenew)
buttonsave = tk.Button(framenew, text= 'Save', command= Save)
buttonload = tk.Button(framenew, text= 'Load', command= Load)
buttonimage = tk.Button(framenew, text= 'Login white Image', command= ImageLogin)


usernamelabel.place(x= 10,y= 10,width=55 ,height= 20)
passwortlabel.place(x= 10,y= 40,width=55 ,height= 20)
username.place(x= 90,y= 10,width=70 ,height= 20)
passwort.place(x= 90,y= 40,width=70 ,height= 20)
buttonsave.place(x= 57.5,y= 80,width=60 ,height= 20)
buttonload.place(x= 57.5,y= 110,width=60 ,height= 20)
buttonimage.place(x= 57.5,y= 140,width=60 ,height= 20)
framenew.place(x= 0, y= 0, width= 600, height= 500)


#Frame1
addition = tk.Button(frame1, text= '+', command= addition )
subtraktion = tk.Button(frame1, text= '-', command= subtraktion )
multiplikation = tk.Button(frame1, text= '*', command= multiplikation )
division = tk.Button(frame1, text= ':', command= division )
quadrieren = tk.Button(frame1, text= '^', command= quadrieren )
wurzel = tk.Button(frame1, text= '^()', command= wurzel )
operator1 = tk.Entry(frame1)
operator2 = tk.Entry(frame1)
op1 = tk.Label(frame1, text="Op.1", bg='#FFCFC9')
op2 = tk.Label(frame1, text="Op.2", bg='#FFCFC9')
backbutton = tk.Button(frame1, text= '<--', command= Choose)
ergebnissLabel = tk.Label(frame1, bg='#D5E88F', text='')


op1.place(x= 10, y=5, width= 70, height= 20)
op2.place(x= 95, y=5, width= 70, height= 20)
operator1.place(x= 10,y= 35,width= 70,height= 20)
operator2.place(x= 95,y= 35,width= 70,height= 20)
addition.place(x= 10, y=65, width= 20, height= 20)
subtraktion.place(x= 35, y=65, width= 20, height= 20)
multiplikation.place(x= 60, y=65, width= 20, height= 20)
division.place(x= 85, y=65, width= 20, height= 20)
quadrieren.place(x= 110, y=65, width= 20, height= 20)
wurzel.place(x= 135, y=65, width= 20, height= 20)
backbutton.place(x= 155, y=135, width= 20, height= 15)
ergebnissLabel.place(x= 15, y=110, width= 145, height= 20)


frame1.place(x= 0, y= 0, width= 600, height= 500)


#Framechose

buttonrechnen = tk.Button(framechose, text='Calculator', command= Calculator)
buttoncolor = tk.Button(framechose, text='Color picker', command= pick_a_color)

buttonrechnen.place(x= 15, y=40, width= 145, height= 20)
buttoncolor.place(x= 15, y=80, width= 145, height= 20)



framechose.place(x= 0, y= 0, width= 600, height= 500)




        

root.mainloop()



 



