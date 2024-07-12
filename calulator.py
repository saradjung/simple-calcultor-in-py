from tkinter import *
def click(button):
    global text_equation

    text_equation=text_equation+str(button)
    label_equation.set(text_equation)
def equals():
    global text_equation
    try:
        result=str(eval(text_equation))
        label_equation.set(result)
        text_equation=result
    except SyntaxError:
        label_equation.set("Syntax Error")
    except ZeroDivisionError:
        label_equation.set("Zero Division Error")
def clear():
    global text_equation

    text_equation=""
    label_equation.set("")

window=Tk()
window.title("SImple Calculator")
window.geometry("500x500")
text_equation=""
label_equation=StringVar()
label=Label(window,width=50,height=2,bg='white',textvariable=label_equation)
label.pack()
print("")
frame=Frame(window)
button1=Button(frame,text="1",width=7,height=2,command=lambda: click('1'))
button1.grid(row=0,column=0)
button2=Button(frame,text="2",width=7,height=2,command=lambda: click('2'))
button2.grid(row=0,column=1)
button3=Button(frame,text="3",width=7,height=2,command=lambda: click('3'))
button3.grid(row=0,column=2)
button4=Button(frame,text="4",width=7,height=2,command=lambda: click('4'))
button4.grid(row=1,column=0)
button5=Button(frame,text="5",width=7,height=2,command=lambda: click('5'))
button5.grid(row=1,column=1)
button6=Button(frame,text="6",width=7,height=2,command=lambda: click('6'))
button6.grid(row=1,column=2)
button7=Button(frame,text="7",width=7,height=2,command=lambda: click('7'))
button7.grid(row=2,column=0)
button8=Button(frame,text="8",width=7,height=2,command=lambda: click('8'))
button8.grid(row=2,column=1)
button9=Button(frame,text="9",width=7,height=2,command=lambda: click('9'))
button9.grid(row=2,column=2)
button0=Button(frame,text="0",width=7,height=2,command=lambda: click('0'))
button0.grid(row=3,column=0)
buttondot=Button(frame,text=".",width=7,height=2,command=lambda: click('.'))
buttondot.grid(row=3,column=1)

button_mul=Button(frame,text="*",width=7,height=2,command=lambda: click('*'))
button_mul.grid(row=0,column=4)
button_add=Button(frame,text="+",width=7,height=2,command=lambda: click('+'))
button_add.grid(row=0,column=5)
button_div=Button(frame,text="/",width=7,height=2,command=lambda: click('/'))
button_div.grid(row=1,column=4)
button_sub=Button(frame,text="-",width=7,height=2,command=lambda: click('-'))
button_sub.grid(row=1,column=5)
button_equal=Button(frame,text="=",width=14,height=2,bg='#5af043',command=lambda: equals())
button_equal.grid(row=2,column=4,columnspan=2)



frame.pack()
button_clear=Button(window,text='Clear',width=14,height=2,bg="#f25a3f",command=lambda:clear())
button_clear.pack()

window.mainloop()