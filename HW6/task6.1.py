import time


class TrafficLight:
    __color = "red"

    def running(self):
        while True:
            print(self.__color)
            time.sleep(7)
            self.__color = "yellow"
            print(self.__color)
            time.sleep(2)
            self.__color = "green"
            print(self.__color)
            time.sleep(10)
            self.__color = "red"


lights = TrafficLight()
lights.running()

