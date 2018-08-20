import tkinter

# Функция вывода символа на экран
def draw(obj, x, y, sym):
    """
    :param obj: имя объекта tkinter
    :param x: координатота по оси x
    :param y: координата по оси y
    :param sym: тип символа, отоброжающегося в окне
    :return: объект символа с заданными координатами на canvas
    """
    return obj.create_text(x, y, text=sym, font='Arial 18')


root = tkinter.Tk()
root.geometry('300x280+300+300')

x1 = 25
y1 = 50
sym_1 = '*'

x2 = 50
y2 = 100
sym_2= '#'

canv=tkinter.Canvas(root, width=300, height=280, cursor=None)
draw(canv, x1, y1, sym_1)
draw(canv, x2, y2, sym_2)
# canv.create_text(x1, y1, text=sym_1, font='Arial 18')
# canv.create_text(x2, y2, text=sym_2, font='Arial 18')
canv.pack()  # отображение объекта на экране
root.mainloop()
