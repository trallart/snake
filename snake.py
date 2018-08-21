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

    def __init__(self, x, y, sym='*', direction='LEFT'):
        self.x = x
        self.y = y
        self.sym = sym
        self.direction = direction

    def draw(self, obj):
        """
        Функция прорисовки символа на canvas
        :param obj: объект типа canvas
        :return: объект символа с заданными координатами на canvas
        """
        obj.create_text(self.x, self.y, text=self.sym, font='Arial 18')

    def Move(self, offset):
        if self.direction == 'LEFT':
            self.x += offset
        elif self.direction == 'RIGHT':
            self.x -= offset
        elif self.direction == 'UP':
            self.y -= offset
        elif self.direction == 'DOWN':
            self.y += offset
        else:
            print('Неправильное значение переменной direction')

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

class Snake:
    def __init__(self, tail, len, direction):
        # super().__init__(self, start, end, level, sym)

        self.tail = tail  # координата хвоста змейки (объект типа Point)
        self.len = len  # длина змейки
        self.direction = direction  # напраление
        self.sym = '#'

    def point_snake(self):
        plist = []
        i = 0
        while i < self.len:
            p = Point(self.tail.x, self.tail.y, direction=self.direction)
            p.Move(i)
            p.draw(canv)
            plist.append(p)
            i += 1
        self.plist = plist











root = tkinter.Tk()
root.geometry('300x280+300+300')

canv=tkinter.Canvas(root, width=300, height=280, cursor=None)

p1 = Point(100, 45, '*', 'RIGHT')


snake = Snake(p1, 30, 'DOWN')
poi = snake.point_snake()
print(poi)


canv.pack()  # отображение объекта на экране
root.mainloop()




