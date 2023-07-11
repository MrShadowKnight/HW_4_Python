# TASK №1

number1 = int(input("Vvedit pochatkove chyslo: "))
number2 = int(input("Vvedit kinceve chyslo: "))

for i in range(number1, number2 + 1):
    if i % 7 == 0:
        print(i)

# TASK №2

number3 = int(input("Vvedit pochatkove chyslo: "))
number4 = int(input("Vvedit kinceve chyslo: "))
count = 0
kratni = []
min_max = []
max_min = []

for a in range(number4, number3 - 1, -1):
    max_min.append(a)

for i in range(number3, number4 + 1):
    min_max.append(i)
    if i % 7 == 0:
        kratni.append(i)
    elif i % 5 == 0:
        count += 1

print("chysla diapasonu vid menshogo: ", min_max)
print("chysla diapasonu vid bilshogo: ", max_min)
print("Vsi kratni 7: ", kratni)
print("Kilkist kratnyh 5: ", count)

# TASK №3

number5 = int(input("Vvedit pochatkove chyslo: "))
number6 = int(input("Vvedit kinceve chyslo: "))
diapason = []

for i in range(number5, number6 + 1):
    if i % 3 == 0 and i % 5 == 0:
        i = "Fizz Buzz"
        diapason.append(i)
    elif i % 3 == 0:
        i = "Fizz"
        diapason.append(i)
    elif i % 5 == 0:
        i = "Buzz"
        diapason.append(i)
    else:
        diapason.append(i)

print(diapason)