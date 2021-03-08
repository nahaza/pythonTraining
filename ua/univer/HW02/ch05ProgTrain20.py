# 20. Будущая стоимость. Предположим, что на вашем сберегательном счете есть определенная сумма денег,
# и счет приносит составной ежемесячный процентный доход. Вы хотите вычислить сумму, которую будете иметь
# после определенного количества месяцев.
# Формула приведена ниже:
# F = Р х ( 1 + i)2,
# 300 Глава 5. Функции
# где F - будущая сумма на счете после указанного периода времени; Р - текущая сумма на счете;
# i - ежемесячная процентная ставка; t - количество месяцев.
# Напишите программу, которая предлагает пользователю ввести текущую сумму на счете, ежемесячную процентную ставку
# и количество месяцев, в течение которых деньги
# будут находиться на счете. Программа должна передать эти значения в функцию, которая возвращает
# будущую сумму на счете после заданного количества месяцев. Программа должна показать будущую сумму на счете.


def main():
    p = float(input("Enter the account’s present value, UAH: "))
    i = int(input("Enter monthly interest rate, percentage: "))
    t = int(input("Enter the number of months that the money will be left in the account: "))
    f = getFutureValue(p, i, t)
    print("Future value, UAH:", format(f, '.2f'))


def getFutureValue(p, i, t):
    i /= 100
    futureValue = p * (1 + i) ** t
    return futureValue


main()