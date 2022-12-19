# 1. Добавьте на свой рабочий стол папку. В ней создайте три текстовых
#    файла: test_1.txt, test_2.txt, test_3.txt. Затем переименуйте файлы
#    на rename_1.txt, rename_2.txt, rename_3.txt
#    После этого удалите созданную папку

import os
#os.mkdir('C:\\Users\\User\\Desktop\\Catalog_p')
# a = open('C:\\Users\\User\\Desktop\\Catalog_p\\test_1.txt', 'w')
# b = open('C:\\Users\\User\\Desktop\\Catalog_p\\test_2.txt', 'w')
# c = open('C:\\Users\\User\\Desktop\\Catalog_p\\test_3.txt', 'w')
# os.rename('C:\\Users\\User\\Desktop\\Catalog_p\\test_1.txt', 'C:\\Users\\User\\Desktop\\Catalog_p\\rename_1.txt')
# os.rename('C:\\Users\\User\\Desktop\\Catalog_p\\test_2.txt', 'C:\\Users\\User\\Desktop\\Catalog_p\\rename_2.txt')
# os.rename('C:\\Users\\User\\Desktop\\Catalog_p\\test_3.txt', 'C:\\Users\\User\\Desktop\\Catalog_p\\rename_3.txt')
#os.remove('C:\\Users\\User\\Desktop\\Catalog_p\\rename_1.txt')
# os.remove('C:\\Users\\User\\Desktop\\Catalog_p\\rename_2.txt')
# os.remove('C:\\Users\\User\\Desktop\\Catalog_p\\rename_3.txt')
#os.removedirs('C:\\Users\\User\\Desktop\\Catalog_p')

# 2. Найти в списке те элементы, значения которых меньше среднего арифметического, взятого
#     от всех элементов списка

# list = []
# while True:
#     list_1 = int(input('Введите элементы списка: '))
#     if list_1 == 15:
#         break
#     list.append(list_1)
# print('Список: ', list)
# import statistics
# average = statistics.mean(list)
# print('Среднее арифметическое списка: ', average)
# elements = []
# for i in list:
#     if i < average:
#         elements.append(i)
# print('Элементы: ', elements)

#3 Создайте два множества:
   # -Если они одинаковые, вывести, что они равны
   # -Если одно множество полностью состоит из второго, вывести сообщение "Множество1 состоит
   #  из множества2"
   # -Если второе множество полностью состоит из первого, вывести сообщение "Множество 2 состоит
   #  из множества1"
   # -Если они пересекаются, вывести элементы, в которых они пересекаются
   # -Если не пересекаются, вывести сообщение об этом

# set_1 = {1, 6, 8, 0, 4}
# set_2 = {1, 6, 8, 0, 4, 12, 34}
# set = set_2 == set_1
# if set == True:
#     print('Множества равны')
# if set_1.issubset(set_2):
#     print('Множество1 состоит из Множества2')
# if set_2.issubset(set_1):
#     print('Множество2 состоит из Mножества1')
# list_1 = list(set_1)
# list_2 = list(set_2)
# if len(set_1.union(set_2)) < len(list_1+list_2):
#     print('Множества пересекаются', set_1&set_2)
# if len(set_1.union(set_2)) == len(list_1+list_2):
#     print('Множества не пересекаются')

# 4. Создайте словарь из строки 'An apple a day keeps the doctor away' следующим образом:
#     в качестве ключей возьмите символы строки, а значениями пусть будут числа, соответствующие количеству
#     вхождений данной буквы в строку

# import collections
# d = collections.Counter('An apple a day keeps the doctor away')
# dictionary =  dict(d)
# print(dictionary)

# 5. Ввести 10 чисел. Данные числа добавить во множество

# a = 0
# m = set([])
# while a < 10:
#     n = int(input('Введите число: '))
#     a += 1
#     m.add(n)
# print(m)

# 6. Есть словарь песен группы Depeche Mode violator songsdict = {'World in My Eyes': 4,76,
# 'Sweetest Perfection': 5,43, 'Personal Jesus': 4,56, 'Halo': 4,30, 'Waiting for the Night':
# 6,07, 'Enjoy the Silence': 4,6, 'Policy of Truth': 4,88, 'Blue Dress': 4,18,
# 'Clean': 5,68}
# Вычислите общее время звучания всех песен. Создайте список песен, время звучания которых
# больше 5 минут. Создайте новый словарь тех песен, название которых состоит из одного слова

# songsdict = {'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56,
#                       'Halo': 4.30, 'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6,
#                       'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68}
# v = songsdict.values()
# t = list(v)
# l = len(t)
# s = 0
# for i in range(l):  # создаем последовательность чисел от 0 до l(9)
#     s += t[i]       # добавляем элементы списка в s и суммируем их
# print("Общее время звучания песен: ", s, 'мин')
# s = []
# for a in songsdict:
#     if songsdict.get(a) > 5:  # get - возвращает значение ключа
#         s.append(a)
#     if len(a) < 2:
#         print(a)
# print('Песни, время звучания которых больше 5 минут: ', s)
# d = {}
# for f in songsdict:
#     f_1 = f.split()
#     if len(f_1) < 2:
#         d[f] = songsdict.get(f)
# print('Менее одного слова в названии песни', d)

# 7. Дана строка. Сохранить в ней только первые вхождения символов,
#     удалить все остальные. Результат вывести в виде кортежа.

# a = input('Введите строку: ')
# b = a[0:7]
# t = tuple(b)
# print(t)
# print(type(t))

# 8. Сжать массив, удалив из него все элементы, величина которых
#      находится в интервале [a,b]. освободившиеся в конце массива
#      элементы заполнить нулями.

# m = []
# while True:
#     m_1 = int(input('Введите элементы массива: '))
#     if m_1 == 45:
#         break
#     m.append(m_1)
# mas = []
# print('Массив: ', m)
# a = int(input('Введите a: '))
# b = int(input('Введите b: '))
# for i in m:
#     if i < a or i > b:
#         mas.append(i)
# for i in range(len(m) - len(mas)):
#     mas.append(0)
# print('Преобразованный массив: ', mas)

# 9. Вычислить количество отрицательных элементов под главной
#    диаганалью матрицы

# import random
# n = int(input('Введите количество строк матрицы: '))
# m = int(input('Введите количество столбцов матрицы: '))
#
# Matrix = [[random.randint(-20,20) for j in range(n)] for i in range(m)]
# h = 0
# print('Matrix: ')
# for i in range (m):
#     print(Matrix[i])
#     for j in range(i+1, n):
#         if Matrix[i][j] < 0:
#             h += 1
# print('Количество отрицательных элементов под главной диаганалью матрицы: ', h)

# 10. Найти сумму элементов, находящихся между минимальным и максимальным
#    элементами. Минимальный и максимальный элементы в сумму не включать

# import random
# a = [random.randint(1, 87) for i in range(8)]
# max = max(a)
# min = min(a)
# print("Список: ", a)
# print("Минимальный элемент: ", min)
# print("Максимальный элемент: ", max)
# s = 0
# for i in a:
#     if i > min:
#         s += i
#     if i == max-1:
#         break
# print(s)

# 10. Найти сумму элементов, находящихся между минимальным и максимальным
#    элементами. Минимальный и максимальный элементы в сумму не включать

# import random
# a = [random.randint(1, 87) for i in range(8)]
# max = max(a)
# min = min(a)
# print("Список: ", a)
# print("Минимальный элемент: ", min)
# print("Максимальный элемент: ", max)
# s = 0
# for i in a:
#     if a.index(i) > a.index(min) and a.index(i) >= a.index(max):
#         s+=i
#
# print(s)










