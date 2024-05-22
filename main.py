import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import *
import math

window = Tk()

window.title("Калькулятор площади треугольника")
window.geometry("500x250")

frame = Frame(window, padx=10, pady=10)
frame.pack(expand=True, fill=Y)

global_widgets = frame.winfo_children()

lbl = Label(frame, text="Выберите способ расчета площади")
lbl.grid(row=1, column=1)

def selected(event):
    selection = combobox.get()
    if selection == "Через основание и высоту":
        method_with_base_and_height()
    elif selection == "Через две стороны и угол":
        method_with_sides_and_angle()

methods = ["Через основание и высоту",
           "Через две стороны и угол"]

def show_result(area):
    area = round(area, 2)
    messagebox.showinfo('Результат', f'Площадь треугольника = {area}')

# Через основание и высоту
def calculate_area_with_base_and_height(base, height):
    base = float(base)
    height = float(height)
    area = float(base * height / 2)
    show_result(area)

# Через 2 стороны и угол
def calculate_area_with_sides_and_angle(a, b, alpha, angle_unit):
    a = float(a)
    b = float(b)
    alpha = float(alpha)
    if angle_unit == "degrees":
        alpha = convert_degrees_to_radians(alpha)
    area = (a * b * math.sin(alpha)) / 2
    show_result(area)

def convert_degrees_to_radians(alpha):
    return math.pi / 180 * alpha
# ---------------------

def clear_extra_widgets():
    for widget in frame.winfo_children():
        if widget not in global_widgets:
            widget.destroy()

def method_with_base_and_height():
    clear_extra_widgets()

    func = lambda: calculate_area_with_base_and_height(base_ent.get(), height_ent.get())

    base_lbl = Label(frame, text="Основание треугольника -")
    base_lbl.grid(row=3, column=1, pady=10)
    base_ent = Entry(frame) # state="disabled"
    base_ent.grid(row=3, column=2)

    height_lbl = Label(frame, text="Высота треугольника -")
    height_lbl.grid(row=4, column=1, pady=10)
    height_ent = Entry(frame)
    height_ent.grid(row=4, column=2)

    calc_btn = Button(frame, text="Рассчитать площадь", command=func)
    calc_btn.grid(row=5, column=2)

# Через 2 стороны и угол
def method_with_sides_and_angle():
    clear_extra_widgets()

    cmd = lambda: calculate_area_with_sides_and_angle(a_ent.get(), b_ent.get(), alpha_ent.get(), var.get())

    var = StringVar()
    var.set("degrees")
    degrees_rdb = Radiobutton(frame, text='град.', variable=var, value="degrees")
    radians_rdb = Radiobutton(frame, text='рад.', variable=var, value="radians")
    degrees_rdb.grid(row=5, column=3)
    radians_rdb.grid(row=5, column=4)

    a_lbl = Label(frame, text="Сторона A")
    a_lbl.grid(row=3, column=1, pady=10)
    a_ent = Entry(frame)
    a_ent.grid(row=3, column=2)

    b_lbl = Label(frame, text="Сторона B")
    b_lbl.grid(row=4, column=1, pady=10)
    b_ent = Entry(frame)
    b_ent.grid(row=4, column=2)

    alpha_lbl = Label(frame, text="Угол α")
    alpha_lbl.grid(row=5, column=1, pady=10)
    alpha_ent = Entry(frame)
    alpha_ent.grid(row=5, column=2)

    calc_btn = Button(frame, text='Рассчитать площадь', command=cmd)
    calc_btn.grid(row=6, column=2)

combobox = Combobox(frame, values=methods, width=30, state="readonly")
combobox.grid(row=2, column=1)
combobox.set("Через основание и высоту")
combobox.bind("<<ComboboxSelected>>", selected)

window.mainloop()
