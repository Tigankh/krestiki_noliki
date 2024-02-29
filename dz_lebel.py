import tkinter
from tkmacosx import Button
from funcs_korov import *

window = tkinter.Tk()
def on_close():
    # window.geometry('720x800+500+100')
    window.destroy()

window.title('dz')

window.geometry('720x800')
window.resizable(False, False)
window.protocol('WM_DELETE_WINDOW', on_close)

label = tkinter.Label(text='на лугу 0 коров', font=('Arial', 50), background='blue', width=26, height=2)
label.grid(row=0, column=0, columnspan=4)

label_null = tkinter.Label(text='', width=26, height=15)
label_null.grid(row=1, column=0, columnspan=4)

button = Button(text='minus korova', font=('Arial', 20), background='red', width=150, height=130,
                command=lambda: dell_korov(label))
button.grid(row=2, column=1)

button2 = Button(text='plus korova', font=('Arial', 20), background='green', width=150, height=130,
                 command=lambda: add_korov(label))
button2.grid(row=2, column=2)


window.mainloop()