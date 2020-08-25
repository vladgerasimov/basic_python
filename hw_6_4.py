"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f'{self.name} едет')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    max_speed = 60

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > self.max_speed:
            print(f'Превышение скорости! Ваша скорость сейчас {self.speed}км\ч, а ограничение {self.max_speed}км\ч!')
        else:
            print(self.speed)


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    max_speed = 40

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > self.max_speed:
            print(f'Превышение скорости! Ваша скорость сейчас {self.speed}км\ч, а ограничение {self.max_speed}км\ч!')
        else:
            print(self.speed)


class PoliceCar(Car):
    is_police = True

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


town_car = TownCar(50, 'green', 'town car')
town_car.show_speed()
town_car.turn('направо')
town_car.stop()
print(town_car.is_police)

sport_car = SportCar(200, 'red', 'sport car')
sport_car.show_speed()
print(sport_car.name)

work_car = WorkCar(45, 'white', 'work car')
work_car.go()
work_car.show_speed()

police_car = PoliceCar(200, 'black', 'police car')
police_car.show_speed()
police_car.turn('обратно')
print(police_car.is_police)