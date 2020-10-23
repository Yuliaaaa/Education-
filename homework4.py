#1Пишем функцию, которая генерирует песню la-la-la. Функция принимает 3 аргумента:
# 1-е число – сколько строк будет в песне. По умолчанию 3
# 2-е число – сколько «la» будет в строке («la» в строке объединяются дефисом). По умолчанию 3
# 3-е число – если 0, то в конце песни (в конце последней строчки) стоит точка, если 1, то в конце
# стоит «!». По умолчанию 0

def word_printer(a=3, b=3, c=0):
    word = "la" + "-"
    words = (word * b)[:-1]
    song = ((words + "\n") * a)[:-1]
    if c == 1:
        return song + "."
    else:
        return song + "!"
print(word_printer(3, 4, 1))

#2 Пишем функцию, которая выводит второе по возрастанию значение из переданных аргументов
# (неопределенное количество). Учитываем, что может быть повторяющиеся значения аргументов.

def func(*args):
    l = list(args)
    l.sort()
    l = list(set(l))
    return l[1]
print(func(45, 60, 2, 1, 0, 0, 34))

# 3.1 Пишем функцию, которая попросит ввести число. Пока он не введёт правильно, просите
# его ввести. Функция возвращает введённое число.
# * Теперь далее для других задач с числами, вы можете пользоваться этой функцией, а не
# простым input!

def add(a):
    return a
while True:
    try:
        a = float(input("Write a number:"))
        print("Thanks you for a number!")
    except ValueError:
        print("Number, please.")
        continue
    break

#3.2 Пишем функцию, которая попросит пользователя ввести слово (строка из буквенных
# символов без пробелов в середине, а вначале и в конце пробелы могут быть). Пока он не
# введёт правильно, просите его ввести. Функция возвращает введённое слово.


def add():
    word = str(input("Write a string:"))
    print(word.isalpha())
    if word.isalpha() and ' ' in word.strip():
        print(f'OK = {word}')
        return
    else:
        print("Incorrect, repeate, plz")
        add()

add()

    while True:
        try:
            word = str(input("Write a string:"))
            if word.isalpha():
                print("Thank you for a word")
            # if(word[0] and word[-1] == ' '):
            if ' ' in word.strip():
                print("Error, delete indents")

        except ValueError:
            print("Word, please.")



# 3.3 Проверка на високосный год
def is_year_leap(year):
    return year % 4 == 0
print(is_year_leap(2020))

#3.4 Функция принимает три числа a, b, c. Функция должна определить, существует ли
# треугольник с такими сторонами. Если треугольник существует, вернёт True, иначе False.
# print("Sides:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b > c and a + c > b and b + c > a:
    print("Exist")
else:
    print("No Exist")

# 3.5 Функция принимает три числа a, b, c. Функция должна определить, существует ли
# треугольник с такими сторонами и если существует, то возвращает тип треугольника
# Equilateral triangle (равносторонний), Isosceles triangle (равнобедренный), Versatile triangle
# (разносторонний) или не треугольник (Not a triangle).

# 3.6 Функция принимает три числа a, b, c. Функция должна определить, существует ли
# треугольник с такими сторонами и если существует, то возвращает тип треугольника
# Equilateral triangle (равносторонний), Isosceles triangle (равнобедренный), Versatile triangle
# (разносторонний) или не треугольник (Not a triangle).










