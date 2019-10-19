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
  rad1 = Radiobutton(window,text='On', value=1)
 
  rad2 = Radiobutton(window,text='Off', value=2)
 
  
 
  rad1.grid(column=0, row=0)
 
  rad2.grid(column=1, row=0)
 
  
 
  
 

def clicked():
 
    lbl.configure(text="Button was clicked !!")
    window = Tk()
 
    window.title("Welcome to Smart Home")
     
    window.geometry('350x200')
 
    chk_state = BooleanVar()
 
    chk_state.set(True) 
 
    chk = Checkbutton(window, text='Heater', var=chk_state,command=on)
 
    chk.grid(column=0, row=4)


    chk_state = BooleanVar()
 
    chk_state.set(True) 
 
    chk = Checkbutton(window, text='Light', var=chk_state,command=on)
 
    chk.grid(column=0, row=8)

    chk_state = BooleanVar()
 
    chk_state.set(True) 
 
    chk = Checkbutton(window, text='Fan', var=chk_state,command=on)
 
    chk.grid(column=0, row=10)
 
    window.mainloop()
 
btn = Button(window, text="Click Next to continue", command=clicked)
 
 

 
btn.grid(column=10, row=5)
 
 
window.mainloop()
