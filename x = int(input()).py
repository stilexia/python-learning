x = int(input())
h = int(input())
m = int(input())

x += h * 60 + m

print(x // 60)
print(x % 60)