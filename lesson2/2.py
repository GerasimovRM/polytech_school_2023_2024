a = int(input())
# print(3 > 5, 5 > 3, 5 >= 3, 3 < 5, 3 <= 5, 3 == 4, 3 != 4, 5 == 5)

if a >= 0 and a % 2 == 0:
    print("Положительное!")
    print("Четное!")
elif a >= 0:
    print("Положительное!")
    print("Нечетное!")
else:
    print("Отрицательное!")


print('Конец программы!')