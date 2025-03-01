numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("القائمة المحدثة هي:", unique_numbers)