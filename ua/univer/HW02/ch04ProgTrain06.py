# 6. Таблица соответствия между градусами Цельсия и градусами Фаренгейта. Напишите программу, которая выводит таблицу
# температур по шкале Цельсия от О до 20 и их
# эквиваленты по Фаренгейту. Формула преобразования температуры из шкалы Цельсия
# в шкалу Фаренгейта:
# 9 F=-C+32,
# 5
# где F - это температура по шкале Фаренгейта; С - температура по шкале Цельсия. Для
# вывода этой таблицы ваша программа должна применить цикл.


print('------------------------------')
print('Celsius        Fahrenheit')
print('------------------------------')
for temperatureCelsius in range(21):
    temperatureFahrenheit = (9 / 5) * temperatureCelsius + 32
    print(temperatureCelsius + 1, "\t\t\t\t", format(temperatureFahrenheit, '.1f'))
