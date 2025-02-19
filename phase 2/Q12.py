#الفرق الرئيسي بين القائمة والـ tuple هو أن القائمة يمكن أن تتغير بعد إنشائها, بينما لا يمكن تغيير tuple بعد إنشائها.

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

my_tuple = (1, 2, 3)
try:
    my_tuple.append(4)
except AttributeError:
    print("لا يمكن إضافة عنصر إلى tuple.")