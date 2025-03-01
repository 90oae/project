import matplotlib.pyplot as plt
import numpy as np

# بيانات درجات الحرارة في مدينتين على مدار شهر كامل
city1_temps = np.array([20, 22, 25, 28, 30, 32, 34, 36, 35, 33, 30, 25])
city2_temps = np.array([18, 20, 22, 25, 28, 30, 32, 34, 33, 31, 28, 22])

# رسم خطوط لدرجات الحرارة في المدينتين
plt.plot(city1_temps, label='مدينة 1')
plt.plot(city2_temps, label='مدينة 2')

# إضافة عنوان للمخطط
plt.title('درجات الحرارة في م')