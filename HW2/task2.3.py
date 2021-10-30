# as a list
month = int(input("enter the month of the year as an integer (1-12): "))
timeoftheyear = [
    "winter",
    "winter",
    "spring",
    "spring",
    "spring",
    "summer",
    "summer",
    "summer",
    "autumn",
    "autumn",
    "autumn",
    "winter"
]
print("Time of the year from the list: " + timeoftheyear[month-1])

time_of_the_year = {
    1: "winter",
    2: "winter",
    3: "spring",
    4: "spring",
    5: "spring",
    6: "summer",
    7: "summer",
    8: "summer",
    9: "autumn",
    10: "autumn",
    11: "autumn",
    12: "winter",
}
print("Time of the year from the dictionary: " + time_of_the_year.get(month))
