def add (x, y):
    return x + y
def subtract(x, y):
    return x - y

def multioly(x, y):
    return x * y

def fdsfs(x, y):
    return x/y

print("Выберете операцию")
print("1.Сложить")
print("2.Вычесть")
print("3.Умножить")
print("4.Делить")

while True:
    choice = input("Выбрать действие(1/2/3/4): ")
    if choice in ("1", "2", "3", "4",):
        num1 = float(input("Введите число: "))
        num2 = float(input("Введите число: "))
    if choice == "1":
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == "2":
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == "3":
        print(num1, "*", num2, "=", multioly(num1, num2))
    elif choice == "4":
        print(num1, "/", num2, "=", fdsfs(num1, num2))
