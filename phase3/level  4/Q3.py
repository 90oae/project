import pandas as pd

# قراءة الملف CSV
df = pd.read_csv('data.csv')

# عرض البيانات
print(df.head())

# حساب المتوسطات
mean = df.mean()
print("متوسطات:")
print(mean)

# حساب التباين
var = df.var()
print("تباين:")
print(var)

# حساب التوزيع
std = df.std()
print("توزيع:")
print(std)

# تصفي البيانات
df_cleaned = df.dropna()  # إزالة القيم الناقصة
df_cleaned = df_cleaned[df_cleaned['column_name'] > 0]  # تصفي القيم السلبية

# عرض البيانات النظيفة
print(df_cleaned.head())

# حساب المتوسطات بعد التصفية
mean_cleaned = df_cleaned.mean()
print("متوسطات بعد التصفية:")
print(mean_cleaned)