a = int(input())
# print(3 > 5, 5 > 3, 5 >= 3, 3 < 5, 3 <= 5, 3 == 4, 3 != 4, 5 == 5)

if a >= 0:
    print("Положительное!")
    if a % 2 == 0:
        print("Четное!")
    else:
        print("Нечетное")
else:
    print("Отрицательное!")

print('Конец программы!')