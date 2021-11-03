class OrganicCell:
    def __init__(self,cell_num: int):
        self.cell_number = cell_num

    def __add__(self, other):
        return OrganicCell(self.cell_number + other.cell_number)

    def __sub__(self, other):
        if self.cell_number - other.cell_number > 0:
            return OrganicCell(self.cell_number - other.cell_number)
        else:
            print("operation cannot be performed")

    def __mul__(self, other):
        return OrganicCell(self.cell_number * other.cell_number)

    def __truediv__(self, other):
        return OrganicCell(self.cell_number // other.cell_number)

    def make_order(self, num):
        return str((("*" * num) + '\n') * (self.cell_number // num)) + '*' * (self.cell_number % num)


cell = OrganicCell(12)
cell_2 = OrganicCell(5)

print(cell.make_order(5))
print(cell_2.make_order(8))

