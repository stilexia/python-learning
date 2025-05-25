a = int(input("Ваше первое число: "))
b = int(input("Ваше второе число: "))
if b == 0:
    print("Деление на ноль невозможно.")
    b = int(input("Введите ваше число заново: "))
    if b == 0:
        print("ты даун?")
    else:
        print(a / b)
else:
    print(a / b)