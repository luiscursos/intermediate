### Dates ###

from datetime import datetime
from datetime import time
from threading import current_thread

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


print_date(now)



year_2023 = datetime(2023, 1, 1)

print(year_2023)
print_date(year_2023)


current_time = time(21,5, 3)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

diff = year_2023 - now
print(diff)

from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)


current_date = date(2015, 1, 2)
print(current_date.year)
print(current_date.month)
print(current_date.day)


from datetime import timedelta
# EL time delta se utiliza para trabajar con franjas de fechas
start_timedelta = timedelta(200,100, 100, weeks = 30)
end_timedelta = timedelta(300,100, 100, weeks = 40)
print(end_timedelta-start_timedelta)
print(end_timedelta+start_timedelta)



ahora = datetime.now()

hora = ahora.hour
minuto = ahora.minute
segundo = ahora.second


reloj = time(hour=hora, minute=minuto, second=segundo)
print("Mi reloj ", reloj)