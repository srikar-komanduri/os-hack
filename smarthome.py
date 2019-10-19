from tkinter import *
 
from tkinter.ttk import *
 
window = Tk()
 
window.title("Welcome to Smart Home")
 
window.geometry('350x200')

 

lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)
def on():
  window = Tk()
 
  window.title("Choose Your option")
 
  window.geometry('350x200')
  print("On or Off")
 

def clicked():
 
    lbl.configure(text="Button was clicked !!")
    window = Tk()
 
    window.title("Welcome to Smart Home")
     
    window.geometry('350x200')
 
    chk_state = BooleanVar()
 
    chk_state.set(True) #set check state
 
    chk = Checkbutton(window, text='Heater', var=chk_state,command=on)
 
    chk.grid(column=0, row=4)


    chk_state = BooleanVar()
 
    chk_state.set(True) #set check state
 
    chk = Checkbutton(window, text='Light', var=chk_state)
 
    chk.grid(column=0, row=8)

    chk_state = BooleanVar()
 
    chk_state.set(True) #set check state
 
    chk = Checkbutton(window, text='Fan', var=chk_state)
 
    chk.grid(column=0, row=10)
 
    window.mainloop()
 
btn = Button(window, text="Click Next to continue", command=clicked)
 
 

 
btn.grid(column=10, row=5)
 
 
window.mainloop()
