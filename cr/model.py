'''
Модель данных для представления трехмерного кубика.
Модель универсальная, может быть применима для хранения кубов
с любым количеством ячеек на грани.

Модель состоит из кубиков.
Кубик это отдельный кубик находящийся на поверности.
т.е. кубики находящиеся внутри куба в модели не ведутся.
кубики могут быть угловыми, реберными или на грани.
Отличие их в том сколько видимых граней с цветом они содержат.
соответственно у кубика на углу - 3
У кубика на ребре - 2
у кубика на грани - 1

для кодирования положения кубика используем систему координат
x-y-z
для кодирования цветов кубиков используем три его атрибута:
x_color, y_color, z_color
для кубиков у которых менее трех цветов, не используемые
заполнены специальным значением 0.
цвета кодируем числами от 1 до 6.

чтобы трансформировать грань (повернуть ее) надо
трансформировать все кубики входящие в нее.
Кубики входящие в определенную грань, имеют одинаковую
координату по этой оси.

'''


from math import *


class Cubic(object):
    """Базовый класс для отдельного кубика на поверхности
    нашего куба.
    На входе tuple c координатами в кубе (x, y, z)
    и tuple с цветами по осям (x, y, z)"""

    def __init__(self, position, colors):
        super(Cubic, self).__init__()
        # Храним координаты и цвета в виде массивов,
        # чтобы потом манипулировать отдельными элементами
        self.position = list(position)
        self.colors = list(colors)

    def __repr__(self):
        return 'position:{}, colors:{}'.format(self.position, self.colors)

    def transform(self, axe, clockwise=True):
        '''Осуществить вращение кубика.
        Параметры:
        axe - ось вокруг которой вращать 0-x, 1-y, 2-z
        clockwise - направление вращения True - по
        часовой стрелке.
        При вращении меняем координаты кубика и цвета по осям.

        '''
        self.move(axe, clockwise)
        self.swap_colors(axe)

    def rotate(self, position, axe, angle):
        '''Осуществить преобразование координат при повороте
        на указанный угол вокруг указанной оси'''
        radian_angle = radians(angle)
        # TODO Сделать
        res = list(position)
        # Индекс первой координаты для преобразования
        first = (axe + 2) % 3
        # Индекс второй координаты для преобразования
        second = (axe + 1) % 3
        # Используем округление,
        # т.к. тригонометрия дает погрешность в последних знаках
        res[first] = round(position[first] * cos(radian_angle) +
                           position[second] * sin(radian_angle), 5)
        res[second] = round(-position[first] * sin(radian_angle) +
                            position[second] * cos(radian_angle), 5)
        return res

    def move(self, axe, clockwise=True):
        '''Осуществить смену координат кубика в ходе вращения
        вокруг указанной оси в указанном направлении'''
        angle = 90
        self.position = self.rotate(self.position, axe, angle)
        pass

    def swap_colors(self, axe):
        '''Осуществить смену цветом по осям в ходе вращения.
        Алгоритм: цвет по оси вращения не меняется,
        а цвета по оставшимся осям меняются между собой.'''
        axes = [0, 1, 2]
        # Удаление элемента по значению
        axes.remove(axe)
        self.colors[axes[0]], self.colors[axes[1]] = self.colors[axes[1]], self.colors[axes[0]]

class Model(object):
    """Модель содержит все внешние кубики нашего куба."""
    def __init__(self, dimension):
        super(Model, self).__init__()
        self.dimension = dimension
        self.cubics = []
        self.build_cubics(self.dimension)

    def build_cubics(self, dimension, with_colors=False):
        '''Заполнить массив поверхностных кубиков'''
        for _x in range(0, dimension):
            for _y in range(0, dimension):
                for _z in range(0, dimension):
                    new_cubic = Cubic((_x, _y, _z), (0, 0, 0))
                    self.cubics.append(new_cubic)


