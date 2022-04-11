"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.

"""


class Car:

    def __init__(self, name, speed, color, police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.police = police

    def go(self):
        return f'The {self.name} went.'

    def stop(self):
        return f'\nThe {self.name} has stopped.'

    def turn(self, direction):
        return f'\nThe {self.name} turned {direction}'

    def indicate_speed(self):
        return f'\nYour speed is {self.speed}'


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


class WorkCar(Car):

    def __init__(self, speed, color, name, police):
        super().__init__(speed, color, name, police)

    def indicate_speed(self):
        if self.speed > 40:
            return f'\nYour speed is higher than speed allowed! The speed of car {self.name} is {self.speed}'
        else:
            return f'The speed of car {self.name} is ok'


class TownCar(Car):
    def indicate_speed(self):
        if int(self.speed) > 60:
            return f'\nYour speed is higher than allow! Your speed is {self.speed}'
        else:
            return f'Speed of {self.name} is normal'


workCar = WorkCar('UAZ', 50, 'blue', False)

print('1:\n' + workCar.go(), workCar.indicate_speed(), workCar.turn('left'), workCar.stop())

townCar = TownCar('Ford', 60, 'white', False)

print('2:\n' + townCar.go(), townCar.indicate_speed(), townCar.turn('left'), townCar.stop())

sportCar = SportCar('AudiRS', 170, 'red', False)
print('3:\n' + sportCar.go(), sportCar.indicate_speed(), sportCar.turn('right'), sportCar.stop())

policeCar = PoliceCar('Kia', 100, 'yellow', True)
print('4:\n' + policeCar.go(), policeCar.indicate_speed(), policeCar.turn('left'), policeCar.stop())



