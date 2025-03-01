import numpy as np

# إنشاء مصفوفة من الأعداد العشوائية
array = np.random.rand(5, 5)

# طباعة المصفوفة
print("المصفوفة:")
print(array)

# حساب المتوسط
mean = np.mean(array)
print("\nالمتوسط:")
print(mean)

# حساب الانحراف المعياري
std = np.std(array)
print("\nالانحراف المعياري:")
print(std)