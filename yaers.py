a = int(input("Ваш год:"))
if a % 4 == 0 or a % 400 == 0:
     print("Високосный")
elif a % 100:
        print("Обычный")
else:
  print("Обычный")