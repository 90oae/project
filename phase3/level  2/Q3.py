numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]

positive_numbers = [num for num in numbers if num > 0]
negative_numbers = [num for num in numbers if num < 0]

print("الأعداد الموجبة هي:", positive_numbers)
print("الأعداد السالبة هي:", negative_numbers)