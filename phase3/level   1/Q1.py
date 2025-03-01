num_count = int(input("ادخل عدد الأرقام: "))
sum = 0

for i in range(num_count):
    num = float(input(f"ادخل الرقم {i+1}: "))
    sum += num

average = sum / num_count
print(f"المتوسط الحسابي هو: {average}")