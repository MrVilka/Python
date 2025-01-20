from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Калькулятор')
window.geometry('400x400')
icon = PhotoImage(file='imt.png')
window.iconphoto(False, icon)

def calc():
    a = str(r.get())
    aa = list(a)
    n, z, n2, v = '', '', '', 0.0
    abc = 0
    for i in a:
        if i.isdigit() and abc == 0:
            n += i
        elif i in '+-*/':
            z += i
            abc = 1
        elif i.isdigit() and abc == 1:
            n2 += i
    if z == '+':
        v = int(n) + int(n2)
    elif z == '-':
        v = int(n) - int(n2)
    elif z == '*':
        v = int(n) * int(n2)
    elif z == '/':
        try:
            v = int(n) / int(n2)
        except ZeroDivisionError:
            v = 'Error'
    if z != '' and n != '' and n2 != '':
        r.delete(0, 'end')
        r.insert(0, v)
def delete():
    a = str(r.get())
    aa = list(a)
    aa.pop()
    v = ''.join(aa)
    r.delete(0, 'end')
    r.insert(0, v)

def btn_action(value):
    a = r.get()
    a += str(value)
    r.delete(0, 'end')
    r.insert(0, a)

def packs():
    padding = 10
    btn_width = 5
    btn_height = 2
    font = ("Arial", 14)

    # Label and Entry widget at the top
    txt.grid(row=0, column=0, columnspan=4, pady=padding)
    r.grid(row=1, column=0, columnspan=4, pady=padding, padx=padding)

    # Create number buttons dynamically (1-9)
    for i in range(3):
        for j in range(3):
            btn_num = i * 3 + j + 1
            action = lambda value=btn_num: btn_action(value)
            btnn = Button(window, text=f'{btn_num}', width=btn_width, height=btn_height,
                         font=font, command=action)
            btnn.grid(row=i+2, column=j, padx=padding, pady=padding)

    # Create operator buttons (+, -, *, /)
    operators = ['+', '-', '*', '/']
    for i, operator in enumerate(operators):
        action = lambda value=operator: btn_action(value)
        btn_operator = Button(window, text=operator, width=btn_width, height=btn_height,
                             font=font, command=action)
        btn_operator.grid(row=i+2, column=3, padx=padding, pady=padding)

    # Create 0 button, which spans two columns
    action = lambda value=0: btn_action(value)
    btn0 = Button(window, text="0", width=btn_width, height=btn_height,
                  font=font, command=action)
    btn0.grid(row=5, column=0, columnspan=2, padx=padding, pady=padding)

    # Create Calculate button
    btn.grid(row=5, column=2, pady=padding)

    # Create Backspace button
    btn2.grid(row=5, column=3, pady=padding)
    padding = 10
    btn_width = 5
    btn_height = 2

    txt.grid(row=0, column=0, columnspan=4, pady=padding)
    r.grid(row=1, column=0, columnspan=4, pady=padding, padx=padding)

    for i in range(3):
        for j in range(3):
            btn_num = i * 3 + j + 1
            action = lambda value=btn_num: btn_action(value)
            btnn = Button(window, text=f'{btn_num}', width=btn_width, height=btn_height,
                         font=("Arial", 14), command=action)
            btnn.grid(row=i+2, column=j, padx=padding, pady=padding)

    operators = ['+', '-', '*', '/']
    for i, operator in enumerate(operators):
        action = lambda value=operator: btn_action(value)
        btn_operator = Button(window, text=operator, width=btn_width, height=btn_height,
                             font=("Arial", 14), command=action)
        btn_operator.grid(row=i+2, column=3, padx=padding, pady=padding)

    action = lambda value=0: btn_action(value)
    btn0 = Button(window, text="0", width=btn_width, height=btn_height,
                  font=("Arial", 14), command=action)
    btn0.grid(row=5, column=0, columnspan=2, padx=padding, pady=padding)

    btn.grid(row=5, column=2, columnspan=1, pady=padding)
    btn2.grid(row=5, column=3, columnspan=1, pady=padding)

r = Entry(window, font=("Arial", 14), justify='center')
txt = Label(window, text="Calculator", font=("Arial", 16, "bold"))
btn = Button(window, text="Calculate", font=("Arial", 16, "bold"), command=calc)
btn2 = Button(window, text="Backspace", font=("Arial", 16, "bold"), command=delete)

packs()

# Start the Tkinter event loop
window.mainloop()
