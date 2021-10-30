userstime = int(input("Введите время в секундах: "))
hours = userstime // 3600
hrs = userstime % 3600
minutes = hrs // 60
seconds = hrs % 60
if hours < 10:
    hours = '0' + str(hours)
if minutes < 10:
    minutes = '0' + str(minutes)
if seconds < 10:
    seconds = '0' + str(seconds)

print("Время: " + str(hours) + ":" + str(minutes) + ":" + str(seconds))
print('Time: {0}:{1}:{2}'.format(hours, minutes, seconds))
