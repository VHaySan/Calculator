from tkinter import *
root = Tk()
root.title('Calculator')

text_Input = StringVar()
operator = ''

def btnClick(numbers):
    global operator
    operator +=str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ''
    text_Input.set(operator)

def btnEquals():
    global operator
    total = str(eval(operator))
    text_Input.set(total)

#using grid span across 4 columns
txtDisplay = Entry(root,
                    bd = 30, #border
                    font = ('arial', 20, 'bold'), #font, size, style
                    insertwidth = 4, #how wide insertion cursor
                    bg = 'light blue', #background color
                    justify='right', #result appear on right side using justify
                    textvariable= text_Input ).grid(columnspan = 4) 

btnClear = Button(root,
                  padx = 59, #padding for x 
                  pady = 15, #padding for y
                  bd = 8,
                  font = ('arial', 20,'bold'),
                  text = 'C',
                  bg = 'light blue',
                  command = btnClear).grid(row =1, columnspan = 2)

btnbracket1 = Button(root,
                     padx = 19,
                     pady = 15,
                     bd = 8,
                     font =('arial', 20, 'bold'),
                     text = '(',
                     bg = 'light blue',
                     command = lambda: btnClick('(')).grid(row = 1, column = 2)

btnbracket2 = Button(root,
                     padx = 19,
                     pady = 15,
                     bd = 8,
                     font =('arial', 20, 'bold'),
                     text = ')',
                     bg = 'light blue',
                     command = lambda: btnClick(')')).grid(row = 1, column = 3)

btn7 = Button(root,
                     padx = 16,
                     pady = 16,
                     bd = 8,
                     font =('arial', 20, 'bold'),
                     text = '7',
                     bg = 'light blue',
                     command = lambda: btnClick('7')).grid(row = 2, column = 0)

btn8 = Button(root,
                     padx = 16,
                     pady = 16,
                     bd = 8,
                     font =('arial', 20, 'bold'),
                     text = '8',
                     bg = 'light blue',
                     command = lambda: btnClick('8')).grid(row = 2, column = 1)

btn9 = Button(root,
                     padx = 16,
                     pady = 16,
                     bd = 8,
                     font =('arial', 20, 'bold'),
                     text = '9',
                     bg = 'light blue',
                     command = lambda: btnClick('9')).grid(row = 2, column = 2)

btndiv = Button(root,
                     padx = 19,
                     pady = 16,
                     bd = 8,
                     font =('arial', 20, 'bold'),
                     text = '/',
                     bg = 'light blue',
                     command = lambda: btnClick('/')).grid(row = 2, column = 3)

btn4 = Button(root,
                     padx = 16,
                     pady = 16,
                     bd = 8,
                     font =('arial', 20, 'bold'),
                     text = '4',
                     bg = 'light blue',
                     command = lambda: btnClick('4')).grid(row = 3, column = 0)

btn5 = Button(root,
                     padx = 16,
                     pady = 16,
                     bd = 8,
                     font =('arial', 20, 'bold'),
                     text = '5',
                     bg = 'light blue',
                     command = lambda: btnClick('5')).grid(row = 3, column = 1)

btn6 = Button(root,
                     padx = 16,
                     pady = 16,
                     bd = 8,
                     font =('arial', 20, 'bold'),
                     text = '6',
                     bg = 'light blue',
                     command = lambda: btnClick('6')).grid(row = 3, column = 2)

btnsub = Button(root,
                     padx = 19,
                     pady = 16,
                     bd = 8,
                     font =('arial', 20, 'bold'),
                     text = '-',
                     bg = 'light blue',
                     command = lambda: btnClick('-')).grid(row = 3, column = 3)

btn1 = Button(root,
                     padx = 16,
                     pady = 16,
                     bd = 8,
                     font =('arial', 20, 'bold'),
                     text = '1',
                     bg = 'light blue',
                     command = lambda: btnClick('1')).grid(row = 4, column = 0)

btn2 = Button(root,
                     padx = 16,
                     pady = 16,
                     bd = 8,
                     font =('arial', 20, 'bold'),
                     text = '2',
                     bg = 'light blue',
                     command = lambda: btnClick('2')).grid(row = 4, column = 1)

btn3 = Button(root,
                     padx = 16,
                     pady = 16,
                     bd = 8,
                     font =('arial', 20, 'bold'),
                     text = '3',
                     bg = 'light blue',
                     command = lambda: btnClick('3')).grid(row = 4, column = 2)

btnmultiply = Button(root,
                     padx = 19,
                     pady = 16,
                     bd = 8,
                     font =('arial', 20, 'bold'),
                     text = '*',
                     bg = 'light blue',
                     command = lambda: btnClick('*')).grid(row = 4, column = 3)

btn0 = Button(root,
                     padx = 16,
                     pady = 16,
                     bd = 8,
                     font =('arial', 20, 'bold'),
                     text = '0',
                     bg = 'light blue',
                     command = lambda: btnClick('0')).grid(row = 5, column = 0)

btndot = Button(root,
                     padx = 16,
                     pady = 16,
                     bd = 8,
                     font =('arial', 20, 'bold'),
                     text = '.',
                     bg = 'light blue',
                     command = lambda: btnClick('.')).grid(row = 5, column = 1)

btnequal = Button(root,
                     padx = 16,
                     pady = 16,
                     bd = 8,
                     font =('arial', 20, 'bold'),
                     text = '=',
                     bg = 'light blue',
                     command = btnEquals).grid(row = 5, column = 2)

btnplus = Button(root,
                     padx = 19,
                     pady = 16,
                     bd = 8,
                     font =('arial', 20, 'bold'),
                     text = '+',
                     bg = 'light blue',
                     command = lambda: btnClick('+')).grid(row = 5, column = 3)

root.mainloop()