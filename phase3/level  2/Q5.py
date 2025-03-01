numbers = input("ادخل قائمة من الأعداد: ")
numbers = [int(num) for num in numbers.split()]

max_num = max(numbers)
min_num = min(numbers)

print("أصغر رقم في القائمة:", min_num)
print("أكبر رقم في القائمة:", max_num)