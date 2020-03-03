#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.2
#  in conjunction with Tcl version 8.6
#    Mar 02, 2020 06:32:58 PM +0200  platform: Windows NT

import sys
import tkinter

import globals
from functools import partial
import tkinter.messagebox
import ClientGUI

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1(root)
    root.protocol('WM_DELETE_WINDOW', destroy_Toplevel1)
    root.mainloop()


w = None


def show():
    global ing
    ing = globals.current_meal.ing_map
    vp_start_gui()


def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    return (w, top)


def destroy_Toplevel1():
    globals.main_win.deiconify()
    globals.current_meal = None


class Toplevel1:

    def finish_meal(self):
        correct_order = False
        for i in range(len(self.ing_indexes)):
            numOfIng = self.amount_lst.get(i)
            if int(numOfIng) > 0:
                correct_order = True
                break

        if not correct_order:
            tkinter.messagebox.showerror(title="Eror", message="At list one amount's ingredient must be more then zero!")
        else:
            ClientGUI.clean_lst()
            globals.main_win.deiconify()
            globals.cart.append(globals.current_meal)
            globals.current_meal = None
            ClientGUI.render_lst()
            ClientGUI.top.index += 1
            print(globals.cart)
            root.destroy()


    def update(self, index):
        new_val = globals.current_meal.ing_map.get(self.ing_indexes[index])
        self.amount_lst.delete(index)
        self.amount_lst.insert(index, new_val)
        self.Total_time.configure(text= 'Total time: '+ str(globals.current_meal.seconds))
        self.Total_price.configure(text='Total price: ' + str(globals.current_meal.price))


    def increase_ing(self, index):
        ing = self.ing_indexes[index]
        print(ing)
        globals.current_meal.add_ingredient(ing)
        self.update(index)

    def decrease_ing(self, index):
        ing = self.ing_indexes[index]
        print(ing)
        globals.current_meal.minus_ingredient(ing)
        self.update(index)

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 13 -weight bold"

        top.geometry("600x450+650+150")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        globals.main_win.withdraw()

        self.buttons = []

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.333, rely=0.022, height=36, width=214)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Select ingreadiets''')

        self.OkIng_b = tk.Button(top, command=self.finish_meal)
        self.OkIng_b.place(relx=0.467, rely=0.889, height=33, width=50)
        self.OkIng_b.configure(activebackground="#ececec")
        self.OkIng_b.configure(activeforeground="#000000")
        self.OkIng_b.configure(background="#d9d9d9")
        self.OkIng_b.configure(disabledforeground="#a3a3a3")
        self.OkIng_b.configure(foreground="#000000")
        self.OkIng_b.configure(highlightbackground="#d9d9d9")
        self.OkIng_b.configure(highlightcolor="black")
        self.OkIng_b.configure(pady="0")
        self.OkIng_b.configure(text='''Ok''')

        self.ing_lst = tk.Listbox(top)
        self.ing_lst.place(relx=0.133, rely=0.222, relheight=0.573
                           , relwidth=0.173)
        self.ing_lst.configure(background="white")
        self.ing_lst.configure(disabledforeground="#a3a3a3")
        self.ing_lst.configure(font="TkFixedFont")
        self.ing_lst.configure(foreground="#000000")

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.15, rely=0.156, height=26, width=84)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Ingreadents''')

        self.amount_lst = tk.Listbox(top)
        self.amount_lst.place(relx=0.567, rely=0.222, relheight=0.573
                              , relwidth=0.173)
        self.amount_lst.configure(background="white")
        self.amount_lst.configure(disabledforeground="#a3a3a3")
        self.amount_lst.configure(font="TkFixedFont")
        self.amount_lst.configure(foreground="#000000")

        global ing
        i = 0
        j = 0
        SPACE = 0.02
        self.ing_indexes = list(ing.keys())

        for item in ing:
            self.ing_lst.insert(i, item)
            self.amount_lst.insert(i, 0)
            action_with_arg = partial(self.increase_ing, i)
            self.buttons.append(tk.Button(top, command=action_with_arg))
            action_with_arg = partial(self.decrease_ing, i)
            self.buttons.append(tk.Button(top, command=action_with_arg))
            plusB = self.buttons[j]
            minusB = self.buttons[j + 1]
            plusB.place(relx=0.75, rely=0.222 + (j * SPACE), height=12, width=30)
            plusB.configure(activebackground="#ececec")
            plusB.configure(activeforeground="#000000")
            plusB.configure(background="#d9d9d9")
            plusB.configure(disabledforeground="#a3a3a3")
            plusB.configure(foreground="#000000")
            plusB.configure(highlightbackground="#d9d9d9")
            plusB.configure(highlightcolor="black")
            plusB.configure(pady="0")
            plusB.configure(text='''+''')

            minusB.place(relx=0.8, rely=0.222 + (j * SPACE), height=12, width=30)
            minusB.configure(activebackground="#ececec")
            minusB.configure(activeforeground="#000000")
            minusB.configure(background="#d9d9d9")
            minusB.configure(disabledforeground="#a3a3a3")
            minusB.configure(foreground="#000000")
            minusB.configure(highlightbackground="#d9d9d9")
            minusB.configure(highlightcolor="black")
            minusB.configure(pady="0")
            minusB.configure(text='''-''')

            i = i + 1
            j = j + 2


        self.Label2_1 = tk.Label(top)
        self.Label2_1.place(relx=0.567, rely=0.156, height=26, width=84)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#d9d9d9")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''Amount''')

        self.Total_price = tk.Label(top)
        self.Total_price.place(relx=0.33, rely=0.356, height=26, width=125)
        self.Total_price.configure(background="#d9d9d9")
        self.Total_price.configure(disabledforeground="#a3a3a3")
        self.Total_price.configure(font=font9)
        self.Total_price.configure(foreground="#ff0000")
        self.Total_price.configure(text='''Price:''' + str(globals.current_meal.price))

        self.Total_time = tk.Label(top)
        self.Total_time.place(relx=0.33, rely=0.5, height=26, width=125)
        self.Total_time.configure(background="#d9d9d9")
        self.Total_time.configure(disabledforeground="#a3a3a3")
        self.Total_time.configure(font=font9)
        self.Total_time.configure(foreground="#ff0000")
        self.Total_time.configure(text='''Total time: ''' + str(globals.current_meal.seconds))