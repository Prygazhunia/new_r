#Если в функцию передается кортеж, то посчитать длину всех его слов
#Eсли список - посчитать количество букв и чисел в нем
#Число - количество нечетных цифр
#Строка -количество букв

# def function(a):
#     t = 0
#     d = 0
#
#     if type(a) == list:
#         return len(a)
#
#     elif type(a) == tuple:
#         for i in a:
#             h = len(i)
#             t+=h
#         return t
#
#     elif type(a) == int:
#         for i in str(a):
#             i = int(i)
#             if i % 2 != 0:
#                 d+=i
#             return d
#
#     elif type(a) == str:
#         return len(a)
#
# print('Количество символов в списке: ', function([1,4,6,8]))
# print('Количество букв в кортеже: ', function(('Hello', 'World')))
# print('Количество нечетных цифр в числе 34567: ', function(34567))
# print('Количество букв в строке "Californication": ', function('Californication'))


#Задачка про то, как Николай удалял первое появленние
#элемента из кортежа по значению

def del_from_tuple(tuple_N, element):
    l = list(tuple_N)
    if element in tuple_N:
        l.remove(element)
    return tuple_N
print(del_from_tuple((1,2,43,6),2))
print(del_from_tuple((9, 7, 14, 26, 15), 26))


















