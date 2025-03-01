def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    print("1. تحويل من سيلسيوس إلى فهرنهايت")
    print("2. تحويل من فهرنهايت إلى سيلسيوس")
    print("3. خروج")

    choice = input("اختر الخيار: ")

    if choice == "1":
        celsius = float(input("ادخل درجة الحرارة في سيلسيوس: "))
        fahrenheit = convert_celsius_to_fahrenheit(celsius)
        print(f"درجة الحرارة في فهرنهايت هي: {fahrenheit}")
    elif choice == "2":
        fahrenheit = float(input("ادخل درجة الحرارة في فهرنهايت: "))
        celsius = convert_fahrenheit_to_celsius(fahrenheit)
        print(f"درجة الحرارة في سيلسيوس هي: {celsius}")
    elif choice == "3":
        break
    else:
        print("اختيار غير صحيح")