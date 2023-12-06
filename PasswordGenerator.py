import random
from tkinter import *
from tkinter import messagebox

pw = Tk()
pw.geometry("600x400")
pw.resizable(0,0)
pw.title("PASSWORD GENERATOR")

label=Label(pw, text="Password Generator", fg = "#1E90FF" ,font=("Arial", 22, "bold", "underline"))
label.grid(column=0, row=0, padx=150, pady=10)

def generate():
    try:
        char=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
              'Q','R','S','T','U','V','W','X','Y','Z',
              'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
              'q','r','s','t','u','v','w','x','y','z',
              '0','1','2','3','4','5','6','7','8','9',
              '!','@','#','$','%','^','&','*']
        
        password= ""
        length_input = int(get_l.get())  # Changed variable name from len to length_input
        get_pw.delete(0, END)
        
        if length_input <= 0:
            messagebox.showwarning("Password length","Please enter a valid password length in number greater than 0")
        else:
            for i in range(length_input):
                password += random.choice(char)
            get_pw.insert(0, password)
       
    except ValueError:
        messagebox.showwarning("Password length","Please enter a valid password length in number")

def accept():
    exit()

def reset():
    get_l.delete(0, END)
    u_in.delete(0,END)
    get_pw.delete(0,END)

frame = Frame(pw)
frame.grid(column=0,row=1)

un = Label(frame, text="Enter your username: ", font=("Arial", 12))
un.grid(column=0, row=2, sticky=W)

u_in = Entry(frame)
u_in.grid(column=1, row= 2,padx=10,pady=10)

pw_len= Label(frame, text="Enter length of password: ", font=("Arial",12))
pw_len.grid(column=0,row=3, sticky=W)

get_l=Entry(frame)
get_l.grid(column=1, row=3,padx=10,pady=10)

gen_pw=Label(frame, text="Generated password:", font=("Arial",12))
gen_pw.grid(column=0, row=4, sticky=W)

get_pw=Entry(frame)
get_pw.grid(column=1, row=4, padx=10,pady=10)

gen_b=Button(frame, text="Generate", font=("Arial",12,"bold"),fg="#111111",bg="sky blue",command=generate)
gen_b.grid(column=1, row=5, padx=10, pady= 10)

accb = Button(frame, text="Accept",font=("Arial",12,"bold"), fg="#111111",bg="sky blue", command=accept)
accb.grid(column=1, row=6, padx=10, pady=10)

resetb = Button(frame, text="  Reset  ", font=("Arial", 12, "bold"), fg="#111111",bg="sky blue",command=reset)
resetb.grid(column=1, row=7,padx=10, pady=10) 

pw.mainloop()
