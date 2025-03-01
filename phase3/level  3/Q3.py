def calculate(operation, num1, num2):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "لا يمكن قسمة على الصفر"
    else:
        return "عملية غير مدعومة"

def main():
    print("اختر العملية:")
    print("1. الجمع")
    print("2. الطرح")
    print("3. الضرب")
    print("4. القسمة")
    
    choice = input("الاختيار: ")
    
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("العدد الأول: "))
        num2 = float(input("العدد الثاني: "))
        
        if choice == '1':
            operation = 'add'
        elif choice == '2':
            operation = 'subtract'
        elif choice == '3':
            operation = 'multiply'
        else:
            operation = 'divide'
        
        result = calculate(operation, num1, num2)
        print(f"النتيجة: {result}")
    else:
        print("اختيار غير صالح")

if __name__ == "__main__":
    main()