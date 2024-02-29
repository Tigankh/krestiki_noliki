import tkinter
from button_back import *
from tkmacosx import Button

window = tkinter.Tk()

window.title('Крестики нолики')
window.geometry('810x710')

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# labels
label0 = tkinter.Label(text='\t\tХоди)))))\t\t      ', font=('Arial', 40), background='yellow')
label0.grid(columnspan=6, column=0, row=0)

# buttons
btn1 = Button(text='1', font=('impact', 70), background='green', height=210,
              command=lambda: o(lst, btn1, lst_buttons, label0))
btn1.grid(column=0, row=4)

btn2 = Button(text='2', font=('impact', 70), background='green', height=210,
              command=lambda: o(lst, btn2, lst_buttons, label0))
btn2.grid(column=1, row=4)

btn3 = Button(text='3', font=('impact', 70), background='green', height=210,
              command=lambda: o(lst, btn3, lst_buttons, label0))
btn3.grid(column=2, row=4)

btn4 = Button(text='4', font=('impact', 70), background='green', height=210,
              command=lambda: o(lst, btn4, lst_buttons, label0))
btn4.grid(column=0, row=5)

btn5 = Button(text='5', font=('impact', 70), background='green', height=210,
              command=lambda: o(lst, btn5, lst_buttons, label0))
btn5.grid(column=1, row=5)

btn6 = Button(text='6', font=('impact', 70), background='green', height=210,
              command=lambda: o(lst, btn6, lst_buttons, label0))
btn6.grid(column=2, row=5)

btn7 = Button(text='7', font=('impact', 70), background='green', height=210,
              command=lambda: o(lst, btn7, lst_buttons, label0))
btn7.grid(column=0, row=6)

btn8 = Button(text='8', font=('impact', 70), background='green', height=210,
              command=lambda: o(lst, btn8, lst_buttons, label0))
btn8.grid(column=1, row=6)

btn9 = Button(text='9', font=('impact', 70), background='green', height=210,
              command=lambda: o(lst, btn9, lst_buttons, label0))
btn9.grid(column=2, row=6)

lst_buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]
window.mainloop()
