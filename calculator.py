from tkinter import *

root = Tk()
root.title('Calculator')

entery = Entry(root, width= 32, borderwidth=5)
entery.grid(row=0,column=0, padx=10, pady=10, columnspan=3)

def click(number):
    
    current = entery.get()
    entery.delete(0,END)
    entery.insert(0,str(current) + str(number))

def clear():
    entery.delete(0,END)
def add():
    first_number = entery.get()
    global f_num 
    global math
    math = 'addition'
    f_num = int(first_number)
    entery.delete(0,END)
def equal():
    second_number = entery.get()
    entery.delete(0,END)
    
    if math == 'addition':
        entery.insert(0,f_num + int(second_number))
    if math == 'subtraction':
        entery.insert(0, f_num - int(second_number))
    if math == 'division':
        entery.insert(0, f_num / int(second_number))
    if math == 'multiplication':
        entery.insert(0, f_num * int(second_number))
def subtract():
    first_number = entery.get()
    global math
    math = 'subtraction'
    global f_num
    f_num = int(first_number)
    entery.delete(0,END)
def division():
    first_number = entery.get()
    global math
    math = 'division'
    global f_num
    f_num = int(first_number)
    entery.delete(0,END)
def multiplication():
    first_number = entery.get()
    global math
    global f_num
    math = 'multiplication'
    f_num = int(first_number)
    entery.delete(0,END)

# Defining the buttons
button_1 = Button(root, text= '1',padx= 40, pady=20, command=lambda: click(1))
button_2 = Button(root, text= '2',padx=40,  pady=20, command=lambda: click(2))
button_3 = Button(root, text= '3',padx=40,  pady=20, command=lambda: click(3))
button_4 = Button(root, text= '4',padx=40,  pady=20, command=lambda: click(4))
button_5 = Button(root, text= '5',padx=40,  pady=20, command=lambda: click(5))
button_6 = Button(root, text= '6',padx=40,  pady=20, command=lambda: click(6))
button_7 = Button(root, text= '7',padx=40,  pady=20, command=lambda: click(7))
button_8 = Button(root, text= '8',padx=40,  pady=20, command=lambda: click(8))
button_9 = Button(root, text= '9',padx=40,  pady=20, command=lambda: click(9))
button_0 = Button(root, text= '0',padx=40,  pady=20, command=lambda: click(0))
button_equal = Button(root, text='=', padx=91, pady=20, command=lambda: equal())
button_add = Button(root,text='+',padx=39,pady=20,command= add)
button_clear = Button(root, text='Clear', padx=79, pady=20, command=clear)
button_sub = Button(root, text='-',padx=40,pady=20, command=subtract)
button_div = Button(root,text='/', padx=40,pady=20,command= division)
button_mul = Button(root,text='*',padx=39,pady=20,command=multiplication)
# Printing the buttonsa

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1, columnspan=2)

button_equal.grid(row=5,column=1,columnspan=2)
button_add.grid(row=5,column=0)

button_sub.grid(row=6, column=0)
button_mul.grid(row=6,column=1)
button_div.grid(row=6,column=2)

root.mainloop()