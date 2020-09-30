# # 1
a = input("Please write a text:")
print(a[2], a[-2], a[:5], a[:-2], a[0::2], a[1::2], a[::-1], a[::-2], a[-1:0:-2], a[-2:0:-2], a[-2:0:-1], len(a), sep='\n')
#
# # 2
s = input("Please write a text:")
print(s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])

# 3.1
i = 0
while i < 10:
    print(i, end="")
    i = i + 1
print(i)

# 3.2
a = 20
while a > 0:
    print(a, "",  end="")
    a -= 1

# 3.3?
n = 10
i = int(input("Write numbers:"))
while n != 10:
    n = n // 2
print(n)

#3.4?

# 4.1
list = ['1', '2', '3', '4', '5', '6']
while len(list) != 0:
print(list.pop(0))

# 4.2
a = "H e l l o w o r l d!"
a = a.split(" ")
while len(a) != 0:
   print(a.pop(0))
   print(a)

# 4.3
l = ["90", "31", "20", "22", "25", "30", "1", "40"]
l.sort()
while len(l) != 0:
    print(l.pop(0))
    print(l)

# 4.4
prev = -1
a = 0
b = 0
element = int(input())
while element != 0:
   if prev == element:
       a += 1
   else:
       prev = element
       b = max(b, a)
       a = 1
   element = int(input())
b = max(b, a)
print(b)

# 5
while True:
    a = (input("Plese put some text or number:"))
    b = (input("Please put some text or number for value B:"))
    try:
        a = int(a)
        b = int(b)
        a += b
    except (TypeError, ValueError):
        print(str(a) + str(b))
        break
    else:
        print(a)
# 7.1 Посчитайте сколько слов в тексте
a = "We are not what we should be!\n We are not what we need to be.\n" \
    " But at least we are not what we used to be \n (Football Coach)"
print(len(a.split()))

# 7.2 Удалите знаки препинания в списке слов ?
a = "We are not what we should be! \n We are not what we need to be. \n" \
    "But at least we are not what we used to be \n (Football Coach)"\
for:
    a.strip(" . ")
    print(a)
# 7.3
a = "We are not what we should be!\n We are not what we need to be.\n" \
    " But at least we are not what we used to be \n (Football Coach)"