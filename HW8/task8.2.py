class ZeroDivision(ZeroDivisionError):
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    def division(self):
        try:
            result = self.dividend / self.divider
        except ZeroDivisionError as err:
            result = "division is impossible"
            print(err)
        return result


test = ZeroDivision(
    dividend=100,
    divider=0
)

print(f"Division result: {test.division()}")
