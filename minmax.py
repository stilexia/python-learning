a = int(input())
b = int(input())
c = int(input())
if a >= c and a >= b:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

if a <= c and a <= b:
    print(a)
elif b <= c and b <= a:
    print(b)
else:
    print(c)

if (a >= b and a <= c) or (a <= b and a >= c):
    print(a)
elif (b >= a and b <= c) or (b <= a and b >= c):
    print(b)
else:
    print(c)