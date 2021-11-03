class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.w_name = name
        self.w_surname = surname
        self.w_position = position
        self._w_income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        name = self.w_name
        surname = self.w_surname
        print(name, surname)

    def get_total_income(self):
        income = self._w_income["wage"] + self._w_income["bonus"]
        print(income)


worker_position = Position(
    name="Ivanov",
    surname="Vasil",
    position="DevOPs",
    wage=5000,
    bonus=200
)
worker_position.get_full_name()
worker_position.get_total_income()
