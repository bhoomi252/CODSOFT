import tkinter as tk

calculation=""

def addc(symbol):
    global calculation
    calculation += str(symbol)
    result.delete(1.0,'end')
    result.insert(1.0, calculation)

def evcalc():
    global calculation
    print(calculation)
    try:
        calculation=str(eval(calculation))
        result.delete(1.0,'end')
        result.insert(1.0, calculation )
    except:
        clr()
        result.insert(1.0,'error')

def clr():
    global calculation
    calculation=''
    result.delete(1.0,'end')

root = tk.Tk()
root.geometry('300x275')
root.title('Calculator')

result = tk.Text(root,height=2,width=16,font=("Arial",24))
result.grid(columnspan=5)

b1 = tk.Button(root,text='1', command=lambda: addc(1),width=5,font=('Arial',14))
b1.grid(row=4,column=1)

b2 = tk.Button(root,text='2', command=lambda: addc(2),width=5,font=('Arial',14))
b2.grid(row=4,column=2)

b3 = tk.Button(root,text='3', command=lambda: addc(3),width=5,font=('Arial',14))
b3.grid(row=4,column=3)

b4 = tk.Button(root,text='4', command=lambda: addc(4),width=5,font=('Arial',14))
b4.grid(row=3,column=1)

b5 = tk.Button(root,text='5', command=lambda: addc(5),width=5,font=('Arial',14))
b5.grid(row=3,column=2)

b6 = tk.Button(root,text='6', command=lambda: addc(6),width=5,font=('Arial',14))
b6.grid(row=3,column=3)

b7 = tk.Button(root,text='7', command=lambda: addc(7),width=5,font=('Arial',14))
b7.grid(row=2,column=1)

b8 = tk.Button(root,text='8', command=lambda: addc(8),width=5,font=('Arial',14))
b8.grid(row=2,column=2)

b9 = tk.Button(root,text='9', command=lambda: addc(9),width=5,font=('Arial',14))
b9.grid(row=2,column=3)

b0 = tk.Button(root,text='0', command=lambda: addc(0),width=5,font=('Arial',14))
b0.grid(row=5,column=2)

ba = tk.Button(root,text='+', command=lambda: addc('+'),width=5,font=('Arial',14))
ba.grid(row=5,column=4)

bs = tk.Button(root,text='-', command=lambda: addc('-'),width=5,font=('Arial',14))
bs.grid(row=4,column=4)

bm = tk.Button(root,text='*', command=lambda: addc('*'),width=5,font=('Arial',14))
bm.grid(row=3,column=4)

bd = tk.Button(root,text='/', command=lambda: addc('/'),width=5,font=('Arial',14))
bd.grid(row=2,column=4)

be = tk.Button(root,text='=', command= evcalc ,width=5,font=('Arial',14))
be.grid(row=5,column=3)

bclr = tk.Button(root,text='C', command= clr,width=5,font=('Arial',14))
bclr.grid(row=5,column=1)

root.mainloop()
