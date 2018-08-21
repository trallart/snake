import tkinter


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
        return obj.create_text(self.x, self.y, text=self.sym, font='Arial 18')


root = tkinter.Tk()
root.geometry('300x280+300+300')

canv=tkinter.Canvas(root, width=300, height=280, cursor=None)

p1 = Point(100, 45, '*')
# p1.draw(obj=canv)

p2 = Point(100, 100, '%')
# p2.x = 100
# p2.y = 100
# p2.sym = '*'
# p2.draw(canv)

plist = []
plist.append(p1)
plist.append(p2)

for i in plist:
    i.draw(canv)

canv.pack()  # отображение объекта на экране
root.mainloop()




