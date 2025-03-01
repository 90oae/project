def fibonacci(n):
    if n <= 0:
        return "دخل عدد إيجابي"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

n = int(input("ادخل عدد الأعداد في السلسلة الفيبوناتشي: "))

fib_sequence = fibonacci(n)

print(f"أول {n} أعداد في السلسلة الفيبوناتشي هي: {fib_sequence}")