from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def calculate(self):
        pass


class Topcoat(Clothes):
    def __init__(self, size):
        super().__init__(size)

    @property
    def calculate(self):
        return self.size/(6.5 + 0.5)


class Costume(Clothes):
    def __init__(self, size):
        super().__init__(size)

    @property
    def calculate(self):
        return (self.size * 2) + 0.3


topcoat = Topcoat(100)
print(f"Tissue size for topcoat: {topcoat.calculate}")

costume = Costume(200)
print(f"Tissue size for costume: {costume.calculate}")

print(f"Total tissue size: {topcoat.calculate + costume.calculate}")
