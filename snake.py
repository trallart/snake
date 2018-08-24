import tkinter
import time
import random

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
        self.tag = 'figure'


    def draw(self):
        self.point = self.canv.create_text(self.x, self.y, text=self.sym, font='Arial 14', tag=self.tag)
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
        self.x = self.x + x/2
        self.y = self.y + y/2
        # print(self.y)
        # print(self.canv.coord('n1'))
        # if self.y ==0:
        #     raise ValueError

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

        # self.apple = Point(30, 30, self.canv, '*')  # яблоко
        self.apple = Point(random.randint(0, 100), random.randint(0, 100), canv,  '*')  # яблоко
        self.apple.tag ='apple'
        # self.apple = Point(-80, -80, self.canv,  '*')  # яблоко

        self.plist = self.point_snake()  # список точек змейки


    def point_snake(self):
        plist = []
        i = 0
        while i < self.len:
            if i == 0:
                p = Point(self.tail.x, self.tail.y, self.tail.canv, '+', direction=self.direction)
            else:
                p = Point(self.tail.x, self.tail.y, self.tail.canv, self.sym, direction=self.direction)
            p.Move(i*5)
            p.draw()
            plist.append(p)
            i += 1
            # print(p.x,p.y)
        # plist = plist.reverse()
        # print('Z dspsdf.cm', len(plist))
        return plist


    def Move(self):
        # Рисуем яблоко
        self.apple.draw()
        # цикл тела движения змейки
        for i, point in enumerate(self.plist):
            # Если это не голова
            if i != 0:
                # Движение текущей вниз:
                if point.direction == 'DOWN':
                    # print('Движение в низ')
                    if ['LEFT', 'RIGHT'].count(self.plist[i-1].direction) and self.plist[i].y == self.plist[i-1].y:
                        point.direction = self.plist[i-1].direction
                        # Если второй элемент еще не повернул, то обработка кнопок не выполняется
                        if i == 1:
                            self.motion = True
                # Движение текущей вверх
                elif point.direction == 'UP':
                    if ['LEFT', 'RIGHT'].count(self.plist[i-1].direction) and self.plist[i].y == self.plist[i-1].y:
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
            point.given()

            # Проверка съела ли змейка еду
            # print('Координаты яблока:',self.apple.x, self.apple.y )
            # print('Координаты головы змеи:',self.plist[0].x, self.plist[0].y )

            if -5 < self.plist[0].x - self.apple.x < 5 and -5 < self.plist[0].y - self.apple.y < 5:
                self.len += 1  # увеличение длины змейки
                self.canv.delete(self.apple.tag)
                # Создание нового яблока и проверка, что он не попал на хвост змеи
                while True:
                    var = True
                    self.apple = Point(random.randint(0, 80), random.randint(0, 80), canv, '*') # создание яблока
                    for index in self.plist:
                        if [self.apple.x, self.apple.y] == [index.x, index.y]:
                            var = False
                            self.canv.delete(self.apple.tag)
                            break
                    if var is True:
                        break
                self.apple.tag = 'apple'
                p = Point(self.plist[-1].x, self.plist[-1].y, self.canv, '*', direction=self.plist[-1].direction)
                p.Move(5)
                p.draw()
                self.plist.append(p)


        self.canv.after(20, self.Move)

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
# HorizontalLine1 = HorizontalLine(0, 300, 10, '-')
# HorizontalLine1.draw(canv)
# HorizontalLine2 = HorizontalLine(0, 300, 279, '-')
# HorizontalLine2.draw(canv)
# VerticalLine1 = VerticalLine(0, 280, 5, '-')
# VerticalLine1.draw(canv)
# VerticalLine2 = VerticalLine(0, 280, 295, '-')
# VerticalLine2.draw(canv)


p1 = Point(100, 100, canv, '*', 'UP')
# p1.draw()
# p1.given()


snake = Snake(p1, 10, 'UP', canv)
# snake.point_snake()

root.bind('<Up>', snake.change_direction)
root.bind('<Down>', snake.change_direction)
root.bind('<Left>', snake.change_direction)
root.bind('<Right>', snake.change_direction)
snake.Move()
canv.pack()  # отображение объекта на экране
root.mainloop()




