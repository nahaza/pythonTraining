# 1. Информация об учебных курсах. Напишите программу, которая создает словарь,
# содержащий номера курсов и номера аудиторий, где проводятся курсы. Словарь должен
# иметь приведенные в табл. 9 .2 пары ключ/значение.
# Таблица 9.2
# Номер курса (ключ) Номер аудитории (значение)
# CSlOl 3004
# CS102 4501
# CS103 6755
# CS104 1244
# CS105 1411 508 Глава 9. Словари и множества
# Программа должна также создать словарь, содержащий номера курсов и имена преподавателей, которые ведут каждый курс. Словарь должен иметь приведенные в табл. 9.3
# пары ключ/значение.
# Таблица 9.3
# Номер курса (ключ) Преподаватель (значение)
# CS101 Хайнс
# CS102 Альварадо
# CS103 Рич
# NТ110 Берк -- --- - ·-
# СМ241 Ли
# Программа должна также создать словарь, содержащий номера курсов и время проведения каждого курса. Словарь должен иметь приведенные в табл. 9.4 пары ключ/значение.
# Таблица 9.4
# Номер курса (ключ) Время (значение)
# CS101 8:00
# -
# CS102 9:00
# CS103 10:00
# NП 10 11:00
# СМ241 13:00
# Программа должна позволить пользователю ввести номер курса, а затем показать номер
# аудитории, имя преподавателя и время проведения курса.


dict1 = {'CSlOl': 3004,
         'CS102': 4501,
         'CS103': 6755,
         'CS104': 1244,
         'CS105': 1411}

dict2 = {'CSlOl': 'Хайнс',
         'CS102': 'Альварадо',
         'CS103': 'Рич',
         'CS104': 'Берк',
         'CS105': 'Ли'}

dict3 = {'CSlOl': '8:00',
         'CS102': '9:00',
         'CS103': '10:00',
         'CS104': '11:00',
         'CS105': '13:00'}

courseNum = input("Enter course number: ")

if courseNum in dict1.keys():
    print("Room:", str(dict1[courseNum]))
    print("Teacher:", dict2[courseNum])
    print("Time:", dict3[courseNum])
else:
    print("Not found")