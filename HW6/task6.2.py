class Road:
    r_height = 5
    r_weight = 25

    def __init__(self, road_length: int, road_width: int):
        self._r_length = road_length
        self._r_width = road_width

    def mass_calculate(self):
        mass_res = self._r_length * self._r_width * self.r_height * self.r_weight
        return mass_res


road_object = Road(
    road_length=5000,
    road_width=20
)
d = road_object.mass_calculate()

print(d)
