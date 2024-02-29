import tkinter

count = 0


def add_korov(label: tkinter.Label):
    global count
    if count < 100:
        count += 1
        label.configure(text=f'на лугу {count} коров', background='blue')
    if count % 10 == 0:
        label.configure(text=f'на лугу {count} коров,  идем за сеном и кормим', background='yellow')


def dell_korov(label: tkinter.Label):
    global count
    if count % 10 == 0:
        label.configure(text=f'на лугу {count} коров,  идем за сеном и кормим', background='yellow')
    if count > 0:
        count -= 1
        label.configure(text=f'на лугу {count} коров', background='blue')

