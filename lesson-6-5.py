"""
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'\nЗапуск отрисовки')


class Pen:

    def __init__(self):
        pass

    def draw(self):
        print(f'\nЗапуск отрисовки ручкой')


class Pencil:

    def __init__(self):
        pass

    def draw(self):
        print(f'\nЗапуск отрисовки карандашом')


class Handle:

    def draw(self):
        print(f'\nЗапуск отрисовки маркером')


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()

