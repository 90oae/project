from datetime import datetime

def calculate_time_difference(date1, date2):
    date1 = datetime.strptime(date1, "%d/%m/%Y")
    date2 = datetime.strptime(date2, "%d/%m/%Y")
    time_difference = date2 - date1
    return time_difference

date1 = input("ادخل التاريخ الأول (يوم/شهر/سنة): ")
date2 = input("ادخل التاريخ الثاني (يوم/شهر/سنة): ")

time_difference = calculate_time_difference(date1, date2)

days = time_difference.days
years = days // 365
months = (days % 365) // 30
days = (days % 365) % 30

print(f"الفاصل الزمني بين التاريخين هو {years} سنة {months} شهر {days} يوم")