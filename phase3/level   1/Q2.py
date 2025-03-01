def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

num = float(input("ادخل رقمًا: "))
if is_prime(num):
    print(f"{num} هو عدد أولي")
else:
    print(f"{num} ليس عدد أولي")