#   4. Напишите цикл, который просит пользователя ввести число. Цикл должен выполнить
# 1 О итераций и вести учет нарастающего итога введенных чисел.

total = 0
for i in range(10):
    num = int(input("Enter a number: "))
    total += num
    print(total)