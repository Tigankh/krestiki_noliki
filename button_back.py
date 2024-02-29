import time
import tkinter
from test import *
from vin import *
from typing import List


def o(lst: list, btn: tkinter.Button, lst_buttons: list, lbl: tkinter.Label, znak: str = "O"):
    if btn.cget('text') == 'O' or btn.cget('text') == 'X':
        lbl.configure(text='\t\tЗанято!!!\t\t      ', bg='red')
        print('zanyato')
        return
    lbl.configure(text='\t\tХоди)))))\t\t      ', bg='yellow')
    lst[int(btn.cget('text')) - 1] = znak
    btn.configure(text=znak)
    if vin(lst) == 'O':
        disable_btns(lst_buttons)
        lbl.configure(text='\t\tvin man\t\t      ', bg='green')
        return 'vin man'
    if vin(lst) == 'X':
        disable_btns(lst_buttons)
        lbl.configure(text='vin computer')
        return
    if nichya(lst) == True:
        disable_btns(lst_buttons)
        lbl.configure(text='nichya')
        return 'nichya'

    if znak == 'O':
        num_field = robot(del_x_o(lst))  # мы выбрали номер поля, в которое сходит робот
        o(lst=lst, lbl=lbl, znak='X', btn=lst_buttons[num_field - 1], lst_buttons=lst_buttons)


def disable_btns(lst_buttons: List[tkinter.Button]) -> None:
    """
    Отключает все кнопки
    :param lst_buttons: список с кнопками которые хотим отключить
    :return:
    """
    for i in range(len(lst_buttons)):
        lst_buttons[i]['state'] = 'disabled'
