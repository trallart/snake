import tkinter
import time

class Figure:
    def __init__(self, start, end, level, sym='*'):
        self.plist = (x for x in list(range(300)) if start <= x <= end)
        self.level = level
        self.sym = sym


class Point:
    """
    Создание символа с координатами x и y на canvas
    """

    def __init__(self, x, y, obj, sym='*', direction='DOWN'):
        self.x = x
        self.y = y
        self.sym = sym
        self.direction = direction
        self.canv = obj


    def draw(self):
        self.point = self.canv.create_text(self.x, self.y, text=self.sym, font='Arial 18', tag='n1')
        self.canv.move(self.point, self.x, self.y)

    def given(self):
        """
        Функция прорисовки символа на canvas
        :param obj: объект типа canvas
        :return: объект символа с заданными координатами на canvas
        """
        # obj.delete('n1')
        if self.direction == 'LEFT':
            x = -1
            y = 0
        elif self.direction == 'RIGHT':
            x = 1
            y = 0
        elif self.direction == 'UP':
            x = 0
            y = -1
        elif self.direction == 'DOWN':
            x = 0
            y = 1
        else:
            print('Неправильное значение переменной direction')
            x = 0
            y = 0

        self.canv.move(self.point, x, y)
        self.x = self.x + x
        self.y = self.y + y

        # print(self.x, 'njxrb', self.y)
        # self.canv.after(20, self.given)

    def Move(self, offset):
        if self.direction == 'LEFT':
            self.x += offset
        elif self.direction == 'RIGHT':
            self.x -= offset
        elif self.direction == 'UP':
            self.y += offset
        elif self.direction == 'DOWN':
            self.y -= offset
        else:
            print('Неправильное значение переменной direction')




class HorizontalLine(Figure):
    """
    Класс горизонтальной линии
    """
    def __init__(self, start, end, level, sym='*'):
        Figure.__init__(self, start, end, level, sym='*')


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
    def __init__(self, tail, len, direction, obj):
        # super().__init__(self, start, end, level, sym)

        self.tail = tail  # координата хвоста змейки (объект типа Point)
        self.len = int(len)  # длина змейки
        self.direction = direction  # начальное направление движения змейки
        self.motion = True  # обработка нажатимя кнопок
        self.sym = '*'  # символ змейки
        self.canv = obj  # Объект на котором змейка рисутеся (Canvas)
        self.plist = self.point_snake()  # список точек змейки



    def point_snake(self):
        plist = []
        i = 0
        while i < self.len:
            if i == 0:
                p = Point(self.tail.x, self.tail.y, canv, '+', direction=self.direction)
            else:
                p = Point(self.tail.x, self.tail.y, canv, self.sym, direction=self.direction)
            p.Move(i*5)
            p.draw()
            plist.append(p)
            i += 1
        # plist = plist.reverse()
        return plist


    def Move(self):
        for i, point in enumerate(self.plist):
            # Если это не голова и направление предыдущего символа не совпадает с направление текущего символа
            if i != 0:  # and self.plist[i].direction != self.plist[i-1].direction:
                # Движение текущей вниз:
                if point.direction == 'DOWN':
                    # print('Движение в низ')
                    if ['LEFT', 'RIGHT'].count(self.plist[i-1].direction) and self.plist[i].y == self.plist[i-1].y-5:
                        point.direction = self.plist[i-1].direction
                        # Если второй элемент еще не повернул, то обработка кнопок не выполняется
                        if i == 1:
                            self.motion = True
                # Движение текущей вверх
                elif point.direction == 'UP':
                    if ['LEFT', 'RIGHT'].count(self.plist[i-1].direction) and self.plist[i].y == self.plist[i-1].y-5:
                        point.direction = self.plist[i-1].direction
                        if i == 1:
                            self.motion = True
                # Движение текущей вверх
                elif point.direction == 'LEFT':
                    # print('ДИВЕЖЕНИЕ В ЛЕВО')
                    if ['UP', 'DOWN'].count(self.plist[i - 1].direction) and self.plist[i].x == self.plist[i-1].x:
                        point.direction = self.plist[i - 1].direction
                        if i==1:
                            self.motion = True
                # Движение текущей вверх
                elif point.direction == 'RIGHT':
                    if ['UP', 'DOWN'].count(self.plist[i - 1].direction) and self.plist[i].x == self.plist[i-1].x:
                        point.direction = self.plist[i - 1].direction
                        if i ==1:
                            self.motion = True
                            print('right')
            point.given()
            # print(self.motion)
        self.canv.after(50, self.Move)

    def change_direction(self, event):
        if self.motion == True:
            if event.keysym == 'Up' and self.plist[0].direction !='DOWN':
                self.plist[0].direction = 'UP'
                self.motion = False
            elif event.keysym == 'Down' and self.plist[0].direction != 'UP':
                self.plist[0].direction = 'DOWN'
                self.motion = False
            elif event.keysym == 'Left' and self.plist[0].direction != 'RIGHT':
                self.plist[0].direction = 'LEFT'
                self.motion = False
            elif event.keysym == 'Right' and self.plist[0].direction != 'LEFT':
                self.plist[0].direction = 'RIGHT'
                self.motion = False








root = tkinter.Tk()
root.geometry('300x280+300+300')

canv=tkinter.Canvas(root, width=300, height=300, cursor=None)
HorizontalLine1 = HorizontalLine(0, 300, 10, '-')
HorizontalLine1.draw(canv)
HorizontalLine2 = HorizontalLine(0, 300, 279, '-')
HorizontalLine2.draw(canv)
VerticalLine1 = VerticalLine(0, 280, 5, '-')
VerticalLine1.draw(canv)
VerticalLine2 = VerticalLine(0, 280, 295, '-')
VerticalLine2.draw(canv)


p1 = Point(100, 100, canv, '*', 'RIGHT')
# p1.draw()
# p1.given()


snake = Snake(p1, 15, 'UP', canv)
# snake.point_snake()

root.bind('<Up>', snake.change_direction)
root.bind('<Down>', snake.change_direction)
root.bind('<Left>', snake.change_direction)
root.bind('<Right>', snake.change_direction)
snake.Move()
canv.pack()  # отображение объекта на экране
root.mainloop()




