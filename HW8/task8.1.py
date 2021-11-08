class Data:
    def __init__(self, date):
        self.input_date = date

    @classmethod
    def extract(cls, date):
        result_list = []
        date_list = cls(date=date).input_date.split('-')
        result_list.append(int(date_list[0]))
        result_list.append(int(date_list[1]))
        result_list.append(int(date_list[2]))
        return result_list

    @staticmethod
    def validate(date):
        date_list = date.split('-')
        print(date_list)
        if 32 < int(date_list[0]) < 0:
            return f"invalid input {date}"
        elif 12 < int(date_list[1]) < 1:
            return f"invalid input {date}"
        elif 0 > int(date_list[2]):
            return f"invalid input {date}"
        else:
            return f"date {date} is valid"


test_object = Data(
    date="12-08-2015"
)

extract = Data.extract("12-088-2015")
print(extract)

validate = Data.validate("12-088-2015")
print(validate)
