# Найти самое длинное слово в строке
# способ 1
# str = "I see there's something burning inside you"
# print(str)
# list = str.split()
# max_str = max(list, key=len)   # key=len - сортировка по длине
# print('Самое длинное слово: ', max_str)

# способ 2
#str = "I see there's something burning inside you"
#str_sort = str.split() #из строки в список
#list_sort = sorted(str_sort, key=len) # key=len сортируется по длине
#print(list_sort[-1])

# С помощью метода sorted() сортируем наш список и выводим
# -1 элемент. Он сортирует от наименьшего слова к
# наибольшему. По логике самое длинное слово будет стоять
#  в конце.



# Преобразовать текст в список слов с удалением знаков препинания
#a = input("Введите текст: ")
#import string
#string.punctuation    # все знаки препинания
#for i in string.punctuation:   # в цикле проходимся по всем символам пунктуации
  # if i in a:
  #     a = a.replace(i, '')  #замена знака препинания на пробел
#print(a.strip())              # strip возвращает копию строки с удаленными элементами

# У вас есть словарь, где ключ - название продукта. Значение - список содержит
# цену и количество товара.
# Выведите название_цену_количество
# C клавиатуры вводите название товара и его количество, n - выход из программы
# Посчитать цену выбранных товаров, и сколько товаров осталось в изначальном списке
# foodstuff = {'milk': [2, 10],
#              'eggs': [4, 12],
#              'bread': [1.5, 11],
#              'sousages': [8.5, 16],
#              'flour': [3.7, 15]}
# for key, value in foodstuff.items():
#     print(key, '-', value[0], '-', value[1])
# s = 0
# while True:
#     a = input('Produkt (no prodakt - "n"): ')
#     if a == 'n' or a not in foodstuff.keys():
#         print('Bye')
#         break
#     b = int (input('Quantity: '))
#     if b > foodstuff[a][1]:
#         print('Out of stock.')
#         continue
#     s += foodstuff[a][0] * b
#     foodstuff[a][1] -= b
# print('Price: ', s)
# for key, value in foodstuff.items():
#     print(key, '_', value[0], '_', value[1])



