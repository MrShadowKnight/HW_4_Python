# TASK №1

number1 = int(input("Введіть початкове число: "))
number2 = int(input("Введіть кінцеіе число: "))
list_diapasonu = []

for i in range(number1, number2 + 1):
    if i % 7 == 0:          # виконуємо ділення без остачі і виводимо результат читсла які діляться націло
        list_diapasonu.append(i)
print(list_diapasonu)

# TASK №2

number3 = int(input("Введіть пперше число: "))
number4 = int(input("Введіть друге число: "))
count = 0                   # Додаємо лічильник кратних на 5
kratni = []                 # Додаємо список кратних на 7
min_max = []                # Додаємо список діапазону від меншого до більшого
max_min = []                # Додаємо список діапазону від більшого до меншого

for a in range(number4, number3 - 1, -1):
    max_min.append(a)       # Вносимо в список діапазону від більшого до меншого

for i in range(number3, number4 + 1):
    min_max.append(i)       # Вносимо в список діапазону від меншого до більшого
    if i % 7 == 0:
        kratni.append(i)    # Вносимо в список кратних на 7
    elif i % 5 == 0:
        count += 1          # Нараховуємо в лічильник

print("chysla diapasonu vid menshogo: ", min_max)          # І все виводимо
print("chysla diapasonu vid bilshogo: ", max_min)
print("Vsi kratni 7: ", kratni)
print("Kilkist kratnyh 5: ", count)

# TASK №3

number5 = int(input("Введіть початкове число: "))
number6 = int(input("Введіть кінцеіе число: "))
diapason = []               # Додаємо список діапазону

for i in range(number5, number6 + 1):
    if i % 3 == 0 and i % 5 == 0:
        i = "Fizz Buzz"     # Запіняємо елемент який кратний, і 3, і 5, і додаємо в діапазон
        diapason.append(i)
    elif i % 3 == 0:
        i = "Fizz"          # Запіняємо елемент який кратний 3, і додаємо в діапазон
        diapason.append(i)
    elif i % 5 == 0:
        i = "Buzz"          # Запіняємо елемент який кратний 5, і додаємо в діапазон
        diapason.append(i)
    else:
        diapason.append(i)  # Додаємо елемент до діапазону

print(diapason)             # Ввиводимо діапазон