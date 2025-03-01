sentence = input("ادخل الجملة: ")
sentence = sentence.lower()

char_count = {}

for char in sentence:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("عدد مرات تكرار كل حرف:")
for char, count in char_count.items():
    print(f"{char}: {count}")