class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.car_speed = speed
        self.car_color = color
        self.car_name = name
        self.car_is_police = is_police

    def car_go(self):
        print(f"The car {self.car_name} start moving.")

    def car_stop(self):
        print(f"The car {self.car_name} stopped.")

    def car_direction(self, direction):
        print(f"The car {self.car_name} turned {direction}.")

    def show_speed(self):
        print(f"Current speed: {self.car_speed}.")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Current speed: {self.car_speed}.")
        if self.car_speed > 60:
            print(f"Car {self.car_name} exceeded speed.")


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Current speed: {self.car_speed}.")
        if self.car_speed > 40:
            print(f"Car {self.car_name} exceeded speed.")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)


car = Car(
    speed=120,
    color="red",
    name="Mazda",
    is_police=False
)

car.car_go()
car.car_stop()
car.car_direction("to the left")
car.show_speed()
print(f"Is this car police: {car.car_is_police}\n")

town_car = TownCar(
    speed=70,
    color="white",
    name="Volvo",
    is_police=False
)

town_car.car_go()
town_car.car_stop()
town_car.car_direction("to the left")
town_car.show_speed()
print(f"Is this car police: {town_car.car_is_police}\n")

sport_car = SportCar(
    speed=190,
    color="red",
    name="Dodge",
    is_police=False
)

sport_car.car_go()
sport_car.car_stop()
sport_car.car_direction("to the left")
sport_car.show_speed()
print(f"Is this car police: {sport_car.car_is_police}\n")

work_car = WorkCar(
    speed=50,
    color="red",
    name="MAN",
    is_police=False
)

work_car.car_go()
work_car.car_stop()
work_car.car_direction("to the left")
work_car.show_speed()
print(f"Is this car police: {work_car.car_is_police}\n")

police_car = PoliceCar(
    speed=210,
    color="black",
    name="ford",
    is_police=True
)

police_car.car_go()
police_car.car_stop()
police_car.car_direction("to the left")
police_car.show_speed()
print(f"Is this car police: {police_car.car_is_police}\n")
