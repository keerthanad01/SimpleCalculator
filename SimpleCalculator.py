from tkinter import *   #This framework provides Python users with a simple way to create GUI elements using the widgets found in the Tk toolkit. Tk widgets can be used to construct buttons, menus, data fields, etc. in a Python application.
import parser   #this interface is to allow Python code to edit the parse tree of a Python expression and create executable code from this.
from math import factorial
root = Tk()  #Creating an instance of Tk initializes this interpreter and creates the root window. 
root.title('Simple-Calculator')

# adding the input field 
display = Entry(root)  #The Entry widget is used to provde the single line text-box to the user to accept a value from the user. 
display.grid(row=0,columnspan=6,sticky=N+E+W+S)
#Code to add buttons to the Calculator
Button(root,text="1",command = lambda :get_variables(1)).grid(row=2,column=0, sticky=N+S+E+W)
Button(root,text=" 2",command = lambda :get_variables(2)).grid(row=2,column=1, sticky=N+S+E+W)
Button(root,text=" 3",command = lambda :get_variables(3)).grid(row=2,column=2, sticky=N+S+E+W)
 
Button(root,text="4",command = lambda :get_variables(4)).grid(row=3,column=0, sticky=N+S+E+W)
Button(root,text=" 5",command = lambda :get_variables(5)).grid(row=3,column=1, sticky=N+S+E+W)
Button(root,text=" 6",command = lambda :get_variables(6)).grid(row=3,column=2, sticky=N+S+E+W)
 
Button(root,text="7",command = lambda :get_variables(7)).grid(row=4,column=0, sticky=N+S+E+W)
Button(root,text=" 8",command = lambda :get_variables(8)).grid(row=4,column=1, sticky=N+S+E+W)
Button(root,text=" 9",command = lambda :get_variables(9)).grid(row=4,column=2, sticky=N+S+E+W)
 
#adding other buttons to the calculator
Button(root,text="AC",command=lambda :clear_all()).grid(row=5,column=0, sticky=N+S+E+W)
Button(root,text=" 0",command = lambda :get_variables(0)).grid(row=5,column=1, sticky=N+S+E+W)
Button(root,text=" .",command=lambda :get_variables(".")).grid(row=5, column=2, sticky=N+S+E+W)
 
 
Button(root,text="+",command= lambda :get_operation("+")).grid(row=2,column=3, sticky=N+S+E+W)
Button(root,text="-",command= lambda :get_operation("-")).grid(row=3,column=3, sticky=N+S+E+W)
Button(root,text="*",command= lambda :get_operation("*")).grid(row=4,column=3, sticky=N+S+E+W)
Button(root,text="/",command= lambda :get_operation("/")).grid(row=5,column=3, sticky=N+S+E+W)
 
# adding new operations
Button(root,text="pi",command= lambda :get_operation("*3.14")).grid(row=2,column=4, sticky=N+S+E+W)
Button(root,text="%",command= lambda :get_operation("%")).grid(row=3,column=4, sticky=N+S+E+W)
Button(root,text="(",command= lambda :get_operation("(")).grid(row=4,column=4, sticky=N+S+E+W)
Button(root,text="exp",command= lambda :get_operation("**")).grid(row=5,column=4, sticky=N+S+E+W)
 
Button(root,text="<-",command= lambda :undo()).grid(row=2,column=5, sticky=N+S+E+W)
Button(root,text="x!", command= lambda: fact()).grid(row=3,column=5, sticky=N+S+E+W)
Button(root,text=")",command= lambda :get_operation(")")).grid(row=4,column=5, sticky=N+S+E+W)
Button(root,text="^2",command= lambda :get_operation("**2")).grid(row=5,column=5, sticky=N+S+E+W)
Button(root,text="^2",command= lambda :get_operation("**2")).grid(row=5,column=5, sticky=N+S+E+W)
Button(root,text="=",command= lambda :calculate()).grid(columnspan=6, sticky=N+S+E+W)

# i keeps the track of current position on the input text field
i = 0
# Receives the digit as parameter and display it on the input field
def get_variables(num):
    global i
    display.insert(i,num)
    i+=1
    
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length
def clear_all():
    display.delete(0,END)
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"Error")
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")
def fact():
    entire_string = display.get()
    try:
        result = factorial(int(entire_string))
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")
root.mainloop()  #a method on the main window which we execute when we want to run our application. This method will loop forever, waiting for events from the user, until the user exits the program – either by closing the window, or by terminating the program with a keyboard interrupt in the console.
