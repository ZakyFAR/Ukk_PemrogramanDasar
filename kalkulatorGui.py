from tkinter import *

# Window
root = Tk()
root.title("Kalkulator")
root.geometry("312x324")
root.resizable(0, 0)


# Click Function
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


# Clear Function
def btn_clear():
    global expression
    expression = ""
    input_text.set("")


# Equal Function
def btn_samadengan():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
        expression=result
    except(ValueError,SyntaxError,TypeError, ZeroDivisionError):#ErrorHandling
        input_text.set("Eror!!! Gan")

expression = ""

# Fetch Data of Input
input_text = StringVar()


# Input Frame
input_frame = Frame(root, width=312, height=50, bd=0)
input_frame.pack(side=TOP)


# Frame for Input Field
input_field = Entry(input_frame, font=("Times New Roman", 18, "bold"),
                textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)


# Frame for Buttons
btns_frame = Frame(root, width=312, height=272)
btns_frame.pack()


#first row
divide = Button(btns_frame, text = "/", fg = "white", width = 10, height=3, bd=0,
            bg="#3F559E", cursor="hand2", command=lambda: btn_click("/")
            ).grid(row=0, column=0, padx=1, pady=1)

seven = Button(btns_frame, text = "7", fg = "black", width = 10, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: btn_click("7")
            ).grid(row=0, column=1, padx=1, pady=1)

eight = Button(btns_frame, text = "8", fg = "black", width = 10, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: btn_click("8")
            ).grid(row=0, column=2, padx=1, pady=1)

nine = Button(btns_frame, text = "9", fg = "black", width = 10, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: btn_click("9")
            ).grid(row=0, column=3, padx=1, pady=1)

#second Row

mutiply = Button(btns_frame, text = "*", fg = "white", width = 10, height=3, bd=0,
            bg="#3F559E", cursor="hand2", command=lambda: btn_click("*")
            ).grid(row=1, column=0, padx=1, pady=1)

four = Button(btns_frame, text = "4", fg = "black", width = 10, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: btn_click("4")
            ).grid(row=1, column=1, padx=1, pady=1)

five = Button(btns_frame, text = "5", fg = "black", width = 10, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: btn_click("5")
            ).grid(row=1, column=2, padx=1, pady=1)

six = Button(btns_frame, text = "6", fg = "black", width = 10, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: btn_click("6")
            ).grid(row=1, column=3, padx=1, pady=1)

#third Row

subtract = Button(btns_frame, text = "-", fg = "white", width = 10, height=3, bd=0,
            bg="#3F559E", cursor="hand2", command=lambda: btn_click("-")
            ).grid(row=2, column=0, padx=1, pady=1)

one = Button(btns_frame, text = "1", fg = "black", width = 10, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: btn_click("1")
            ).grid(row=2, column=1, padx=1, pady=1)

two = Button(btns_frame, text = "2", fg = "black", width = 10, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: btn_click("2")
            ).grid(row=2, column=2, padx=1, pady=1)

three = Button(btns_frame, text = "3", fg = "black", width = 10, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: btn_click("3")
            ).grid(row=2, column=3, padx=1, pady=1)

#Fourth Row
addition = Button(btns_frame, text = "+", fg = "white", width = 10, height=3, bd=0,
            bg="#3F559E", cursor="hand2", command=lambda: btn_click("+")
            ).grid(row=3, column=0, padx=1, pady=1)

twozero = Button(btns_frame, text = "00", fg = "black", width = 10, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: btn_click("00")
            ).grid(row=3, column=1, columnspan=1, padx=1, pady=1)

zero = Button(btns_frame, text = "0", fg = "black", width = 10, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: btn_click("0")
            ).grid(row=3, column=2, columnspan=1, padx=1, pady=1)

point = Button(btns_frame, text = ".", fg = "black", width = 10, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: btn_click(".")
            ).grid(row=3, column=3, columnspan=1, padx=1, pady=1)

#Fifth Row
equals = Button(btns_frame, text = "=", fg = "white", width = 10, height=3, bd=0,
            bg="#3F559E", cursor="hand2", command=lambda: btn_samadengan()
            ).grid(row=4, column=0, padx=1, pady=1)
clear = Button(btns_frame, text = "Clear", fg = "black", width = 32, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: btn_clear()
            ).grid(row=4, column=1, columnspan=3, padx=1, pady=1)




root.mainloop()