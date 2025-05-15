import tkinter
import random

number_of_symbols=12

def generate(number_of_symbols=6):
    symbols = []
    for i in range(number_of_symbols):
        num = random.randint(1, 3)
        if num == 1:
            symbols.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
        elif num == 2:
            symbols.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        elif num == 3:
            symbols.append(random.choice('0123456789'))
    password = ''.join(str(symb) for symb in symbols)
    text.delete('1.0', tkinter.END)
    text.insert('1.0', password)
#создание окна
window=tkinter.Tk()
#цвет заднего фона
window.config(bg='black')
#Размер окна
window.geometry('800x800')
#заголовок окна
window.title('Password')
#текстовое поле
text=tkinter.Text(
    font=('arial',40,'bold'),
    height=1,
    width=number_of_symbols+1,
    bg='black',
    fg='white',
    borderwidth=10
)
#Расположение текстового поля по центру expand=1
text.pack(expand=1)
tkinter.Button(
    text='Generate',
    font=('arial',40,'bold'),
    command=lambda: generate(number_of_symbols),
    bg='black',
    fg='white',
    borderwidth=0
).pack(expand=1)

window.mainloop()