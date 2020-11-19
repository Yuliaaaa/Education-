import math
# Список строк, посчитать сколько в этом списке строк с нечетной длиной
# l = ["spam", "tampa", "world", "piu"]
# i = 0
# for el in l:
#     if len(el) % 2 == 1:
#         i += 1
# print(i)

# Ecть словарь. Вывести на экран все пары - ключ.значения, каждую в новой строке. Вывести на экран тип значений
# d = {"name": "Yulia", "age": 24, "pos": "QA"}
# for key in d:
#     print(key, ":", d[key])
#     print(type(d[key]))

# 2 вариант решения
# d = {"name": "Yulia", "age": 24, "pos": "QA"}
# print(d.items())
# for key, value in d.items():
#     print(key, value)

#raise "Исключения"
# raise функция, что вызывает исключение
# print(10)
# raise ValueError
# print('Am I executed?')

# Можно с сообщ, которые передается как аргумент
# name = "3lena"
# if name[0].isnumeric():
#     raise NameError('Invalid error')

# assert, вызывает, если инструкция неверная,
#
# a = input_small_str('Input less than 10 symbols: ')
# assert len(a) < 10
# print(a)

# mass = -100
# assert (mass > 0), "Mass cant ve less o"
# print(a)

# mass = int(input("Enter mass: "))
#
# assert mass > 0, "Mass error"
# print(mass)

# def add(x, y):
#     return x + y
# add(1, 10)
# add('abc', 'def')

# def repeat(s, exclaim):
#     result = s * 3
#     if exclaim:
#         return result + '!!!'
#     return result
# r = repeat ('wow', True)
# print(r)

# функция гипотенузы
# def repeat(kat1, kat2):
#     result = kat1**2
#     if kat2:
#         return result+ (kat2**2)
#     return result
# r = repeat(3, 4)
# r = math.sqrt(r)
# print(r)

# функция, которая удаляет все небуквенныесимволи внутри строки
# def remove_punctuations(s):
#     for sym in s:
#         if not sym.isalpha():
#             s = s.replace(sym, ' ')
#     assert s.isalpha()
#     return s
#
# some = input()
# word = remove_punctuations(some)
# assert word.isalpha()

#pass заглушка

# def word_printer (word, count=1, wow=0):
#     if wow == 1:
#         return (word * count).upper
#     else:
#         return word * count
# print(word_printer('Bob'))

# def repeat (word, count=1, wow=0):
#     if wow == 1:
#         return (word*count).upper()
#     else:
#         return word*count
# # так делать нельзя
# z = repeat("wow2345", wow=1, "skss")
# print(z)

# функция может принимать произвольные количество аргументов
# def func(*args):
#     l = list(args)
#     l.sort()
#     return l[1]
#
# print(func(3, 6, 7,9))

    #
    # def f(a, b, *ll):
    #     print(a + b)
    #     print(sum(ll))

#     def func(*args, **kwargs):
#
#         return args, kwargs
#
# z,y = func(1, 2, 10, a=3, name="Bod")
# print(z)
# print(y)

import math
print(math.sqrt(10))



# Классы
# class Person:
#     # common_attr = []
#     def __init__(self, n, x, v):
#         self.name = n
#         self.age = x
#         self.value = v

    # def say_hello(self):
    #     print("Hello")
    #
    # def print_self(self):
    #     print(self)
    #
    # def set_name(self, n, x, v):

# if __name__ == '__main__':
#     p1 = Person(n=1, x=30, v=100)
#     print(p1.name)
#     p2 = Person(n=1, x=30, v=100)
#     print(p2.name)
# p2 = Person()
# p1.say_hello()
# p2.say_hello()
# p1.common_attr.appenf("Earth")
# print(p2.common_attr)
# p1.print_self()
# p2.print_self()
# print(p1)
# print(p2)
# p1.print_self()
# p2.print_self()
# p1.set_name(n='Bob')
# p2.set_name(n='Den')
# print(p1.name)
# print(p2.name)


# class Person:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#     def full_name(self):
#         return self.name + " " + self.surname
#
#     def get_older(self, years=1):
#         self.age += years
#
#
# p1 = Person(name="Yulia", surname="N", age=20)
# print(p1.full_name())
# p2 = Person(name="Yulia", surname="N", age=20)
# print(p2.get_older(5))
# print(p2.age)



 #
 #
 #
 #
 #
