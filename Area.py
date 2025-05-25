n = input()
if n == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(s)
elif n == "прямоугольник":
    a = int(input())
    b = int(input())
    print(a * b)
elif n == "круг":
    a = int(input())
    print((a ** 2) * 3.14)