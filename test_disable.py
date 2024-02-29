import tkinter
from tkmacosx import Button

window = tkinter.Tk()

window.title('Отключение кнопки')
window.geometry('810x710')

btn = Button(text='push', bg='green', command=lambda: disable(btn=btn))
btn.grid(row=0, column=2)


def disable(btn: tkinter.Button):
    btn['state'] = 'disabled'
    # btn.configure(text='you vin')


window.mainloop()
