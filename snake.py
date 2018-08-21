import tkinter

class Figure:
    def __init__(self, start, end, level, sym='*'):
        self.plist = (x for x in list(range(300)) if start <= x <= end)
        self.level = level
        self.sym = sym


class Point:
    """
    Создание символа с координатами x и y на canvas
    """

    def __init__(self, x, y, sym):
        self.x = x
        self.y = y
        self.sym = sym

    def draw(self, obj):
        """
        Функция прорисовки символа на canvas
        :param obj: объект типа canvas
        :return: объект символа с заданными координатами на canvas
        """
        obj.create_text(self.x, self.y, text=self.sym, font='Arial 18')

class HorizontalLine(Figure):
    """
    Класс горизонтальной линии
    """
    def __init__(self, start, end, level, sym='*'):
        Figure.__init__(self, start, end, level, sym='*')

        # self.plist_x = (x for x in list(range(300)) if x_left <= x <= x_right)
        # self.y = y_lev
        # self.sym = sym


    def draw(self, obj):
        """
        Функция прорисовки символа на canvas
        :param obj: объект типа canvas
        :return: объект символа с заданными координатами на canvas
        """
        list(map((lambda x: obj.create_text(x, self.level, text=self.sym, font='Arial 16')), self.plist))


class VerticalLine (Figure):
    """
    Класс вертикальной линии
    """


    def draw(self, obj):
        """
        Функция прорисовки символа на canvas
        :param obj: объект типа canvas
        :return: объект символа с заданными координатами на canvas
        """
        list(map((lambda x: obj.create_text(self.level, x, text=self.sym, font='Arial 16')), self.plist))



root = tkinter.Tk()
root.geometry('300x280+300+300')

canv=tkinter.Canvas(root, width=300, height=280, cursor=None)

p1 = Point(100, 45, '*')
p2 = Point(100, 100, '%')

plist = []
plist.append(p1)
plist.append(p2)

for i in plist:
    i.draw(canv)

HorizontalLine = HorizontalLine(20, 70, 150, '*')
HorizontalLine.draw(canv)
#
VerticalLine = VerticalLine(0, 50, 20, '*')
VerticalLine.draw(canv)


# figure = Figure(20, 70, 100, 50, 80, 10)
# print(list(figure.plist_x))
# print(list(figure.draw))
# figure.draw(canv)


canv.pack()  # отображение объекта на экране
root.mainloop()




