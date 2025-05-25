a = float(input("Ваше первое число: "))
c = input("Ваш операндум: (+,-,/,*,mod,div,pow)")
b = float(input("Ваше второе число: "))
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "/":
    if b != 0:
        print(a / b)
    else:
        print("Деление на 0!")
elif c == "*":
    print(a * b)
elif c == "mod":
    if b != 0:
        print(a % b)
    else:
        print("Деление на 0!")
elif c == "div":
    if b != 0:
        print(a // b)
    else:
        print("Деление на 0!")
elif c == "pow":
    print(a ** b)