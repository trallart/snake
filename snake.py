import tkinter
import random

class Figure:
    def __init__(self, start, end, level, sym='*'):
        self.plist = (x for x in list(range(0, 300, 5)) if start <= x <= end)
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
        Figure.__init__(self, start, end, level, sym)


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
        self.NUMBER_SCALE = 5  # масштам точек рядом

        self.tail = tail  # координата хвоста змейки (объект типа Point)
        self.len = int(len)  # длина змейки
        self.direction = direction  # начальное направление движения змейки
        self.sym = '*'  # символ змейки
        self.canv = obj  # Объект на котором змейка рисутеся (Canvas)
        self.plist = self.point_snake()  # построение змейки

        self.preview = None  # начальное значение предыдущего нажатия клавиши движения
        self.motion = True  # обработка нажатимя кнопок

        # Построение стен
        self.walls_left = VerticalLine(20, 260, 10, '|')
        self.walls_right = VerticalLine(20, 260, 290, '|')
        self.walls_up = HorizontalLine(11, 285, 10, '-')
        self.walls_down = HorizontalLine(11, 285, 270, '-')
        walls = [ self.walls_left, self.walls_right, self.walls_up, self.walls_down,]
        list(map(lambda x: x.draw(self.canv), walls))  # прорисовка линий стенки

        # Построеие яблока
        self.apple = Point(random.randint(self.walls_left.level + 2 * self.NUMBER_SCALE,
                                          self.walls_right.level / 2 - self.NUMBER_SCALE),
                           random.randint(self.walls_up.level + self.NUMBER_SCALE,
                                          self.walls_down.level / 2 - self.NUMBER_SCALE), canv, '*')  # создание яблока

        self.apple.tag = 'apple'
        self.apple.draw()

    def point_snake(self):
        plist = []
        i = 0
        while i < self.len:
            if i == 0:
                p = Point(self.tail.x, self.tail.y, self.tail.canv, '+', direction=self.direction)
            else:
                p = Point(self.tail.x, self.tail.y, self.tail.canv, self.sym, direction=self.direction)
            p.Move(i*self.NUMBER_SCALE)
            p.draw()
            plist.append(p)
            i += 1
        return plist

    def game_over(self):
        self.canv.delete('all')
        self.canv.create_text(150, 100, text='GAME OVER', font='Arial 16')

    def apple_eat(self):
        """
        Проверка съела ли змейка еду
        :return: Удленненная змейка, в случае если еда была съедена
        """
        if -self.NUMBER_SCALE < self.plist[0].x - self.apple.x < self.NUMBER_SCALE and -self.NUMBER_SCALE < self.plist[
            0].y - self.apple.y < self.NUMBER_SCALE:
            self.len += 1  # увеличение длины змейки
            self.canv.delete(self.apple.tag)
            # Создание нового яблока и проверка, что он не попал на хвост змеи
            while True:
                var = True
                self.apple = Point(random.randint(self.walls_left.level + 2 * self.NUMBER_SCALE,
                                                  self.walls_right.level / 2 - self.NUMBER_SCALE),
                                   random.randint(self.walls_up.level + self.NUMBER_SCALE,
                                                  self.walls_down.level / 2 - self.NUMBER_SCALE), canv,
                                   '*')  # создание яблока
                for index in self.plist:
                    if [self.apple.x, self.apple.y] == [index.x, index.y]:
                        var = False
                        self.canv.delete(self.apple.tag)
                        break
                if var is True:
                    break
            self.apple.tag = 'apple'
            self.apple.draw()
            # Добавление точки к хвосту
            p = Point(self.plist[-1].x, self.plist[-1].y, self.canv, '*', direction=self.plist[-1].direction)
            p.Move(self.NUMBER_SCALE)
            p.draw()
            self.plist.append(p)

    def wall(self):
        """
        Проверка столкновения змейки со стенокой
        """
        if (self.plist[0].x < self.walls_left.level or self.plist[0].x >= self.walls_right.level / 2) or \
                (self.plist[0].y < self.walls_up.level or self.plist[0].y >= self.walls_down.level / 2):
            self.game_over()  # Игра окончена
            # self.canv.delete('all')
            # self.canv.create_text(150, 100, text='GAME OVER', font='Arial 16')


    def Move(self):
        """
        Основной цикл игры
        """
        # цикл тела движения змейки
        for i, point in enumerate(self.plist):
            # Если это не голова
            if i != 0:
                # Движение текущей точки вниз:
                if point.direction == 'DOWN':
                    # print('Движение в низ')
                    if ['LEFT', 'RIGHT'].count(self.plist[i-1].direction) and self.plist[i].y == self.plist[i-1].y:
                        point.direction = self.plist[i-1].direction
                        # Если второй элемент еще не повернул, то обработка кнопок не выполняется
                        if i == 1:
                            self.motion = True
                # Движение текущей точки вверх
                elif point.direction == 'UP':
                    if ['LEFT', 'RIGHT'].count(self.plist[i-1].direction) and self.plist[i].y == self.plist[i-1].y:
                        point.direction = self.plist[i-1].direction
                        if i == 1:
                            self.motion = True
                # Движение текущей точки влево
                elif point.direction == 'LEFT':
                    if ['UP', 'DOWN'].count(self.plist[i - 1].direction) and self.plist[i].x == self.plist[i-1].x:
                        point.direction = self.plist[i - 1].direction
                        if i==1:
                            self.motion = True
                # Движение текущей точки вправо
                elif point.direction == 'RIGHT':
                    if ['UP', 'DOWN'].count(self.plist[i - 1].direction) and self.plist[i].x == self.plist[i-1].x:
                        point.direction = self.plist[i - 1].direction
                        if i ==1:
                            self.motion = True

                # Проверка на столкновение с собственным хвостом
                if -self.NUMBER_SCALE/2< self.plist[0].x - point.x <2 and -2 < self.plist[0].y - point.y < self.NUMBER_SCALE/2:
                    self.game_over()
                    # self.canv.delete('all')
                    # self.canv.create_text(150, 100, text='GAME OVER', font='Arial 16')

            point.given()  # изсенение направления движения точки

            # Вызов метода проверки съедено ли яблоко
            self.apple_eat()


            # Проверка столкновения змейки со стенкой
            self.wall()

        # Цикл движения
        self.canv.after(20, self.Move)

    def change_direction(self, event):
        """
        Обработка нажатия клавиш
        :param event:
        :return:
        """
        if self.motion == True and self.preview != event.keysym:
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
        self.preview = event.keysym  # предыдущее значение нажатой клавиши


def start(event):
    p = Point(100, 100, canv, '*', 'UP')  # Координаты и направление появления змейки
    snake = Snake(p, 3, 'UP', canv)
    snake.Move()
    root.bind('<Up>', snake.change_direction)
    root.bind('<Down>', snake.change_direction)
    root.bind('<Left>', snake.change_direction)
    root.bind('<Right>', snake.change_direction)
    start_button.destroy()
    # start_button['state'] = 'disabled'



root = tkinter.Tk()
root.title('Snake')
root.geometry('320x330+300+300')
root.resizable(width=False, height=False)
frame_1 = tkinter.Frame(root, width=310, height=300 , borderwidth=1, bg ='white')
canv=tkinter.Canvas(frame_1, width=300, height=280, cursor=None)
frame_2 = tkinter.Frame(root, width=20, height=5 , borderwidth=1, )
frame_3 = tkinter.Frame(root, width=20, height=5 , borderwidth=1, )
start_button = tkinter.Button(frame_2, text="Start", width=12, height=5, bg ='white', fg = 'black', font='Arial-14')
exit_button = tkinter.Button(frame_3, text="Exit", width=12, height=5, bg ='white', fg = 'black', font='Arial-14')



frame_1.pack()
frame_2.pack(side='left', padx=20)
frame_3.pack(side='right', padx=20)
canv.pack()  # отображение объекта на экране
start_button.pack(side='left', padx=0, pady =0)
exit_button.pack(side='right', padx=0, pady =0)


snake = start_button.bind('<Button-1>', start)
exit_button.bind('<Button-1>', exit)

root.mainloop()




