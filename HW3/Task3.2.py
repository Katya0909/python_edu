def my_func(name, lastname, b_year, city, email, tel):
    return f"Name - {name}; Lastname - {lastname}; Birthday - {b_year}; City - {city}; Email - {email}; Phone - {tel}"


inp_name = input("enter your name: ")
inp_lastname = input("enter your lastname: ")
inp_birthday = input("enter your year of birth: ")
inp_city = input("enter the city you live in: ")
inp_email = input("enter your email: ")
inp_tel = input("enter your phone number: ")


print(my_func(lastname=inp_lastname, name=inp_name, b_year=inp_birthday, city=inp_city, email=inp_email, tel=inp_tel))

