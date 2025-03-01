numbers = []
count = int(input("ادخل عدد الأرقام: "))

for i in range(count):
    num = float(input(f"ادخل الرقم {i+1}: "))
    numbers.append(num)

absolute_values = [abs(num) for num in numbers]
print("القيم المطلقة هي:", absolute_values)