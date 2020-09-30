# import math
#
# 1.1
string = "1996"
print(string.isdigit())

string = "Yulia"
print(string.isdigit())

# # 1.2
q = "My name is Yulia"
count = 0
for a in string:
    if (q.isspace()) == True:
        count += 1
print(count)

# # 1.3
string = "See you soon...."
print(string.count("."))


# # 1.4
a = ('{:^100}'. format("Homework"))
print(a)
print(a.count(' '))

# # 1.5
b = "hello yulia"
print(b.title())

# # 1.6
text = "weekend is coming"
result = text.endswith('ing')
print(result)

# # 1.7
s = 'aaaaSbbb'
s.index('a')
print(a)

# # 1.8
words = "summer is coming"
sentence = " ".join(words)
print(sentence)

# # 1.9
a = "      just like it so much      "
print(a.strip(" "))

# # 2.1
x = int("367")
y = int("127")
q = x**2 + y**2
print(q** .5)

# # 2.2
n = 56
print(n // 10 % 10)

# # 2.3
a = 333
b = str(a)[0]
c = str(a)[1]
d = str(a)[2]
e = (int(b) + int(c) + int (d))
print(e)

# # 2.4
n = 3
print(n+1-(n%1))

# # 2.5
X = 20 % 6
print(X)

# # 2.6
x = float(input())
print(int(x * 10) % 10)

# # 3.1
list = [1, 2, 3, 4, 5, 6, "cat", 8, 9]
print(list[-3])

# # 3.2
l = [1, "cat", 3, 4, 5, 6, "cat", 8, "hello"]
print(l[1][0])

# # 3.3
l = [1, "cat", 3, 4, 5, 6, "cat", 8, "hello"]
print(l[-1][-1])

# # 3.4
list = [1, 2, 3, 4, 5, 6, "cat", 8, "hello"]
list.append('dog')
print(list)

# # 3.5
list = [1, 2, 3, 4, 5, 6, "cat", 8]
list.insert(list[3], "sun")
print(list)

# # 3.6
a = ["dog", "cat", 8]
a.remove("dog")
print(a)

# # 3.7
a = [1, 2, 3, 4, 5, 6, 'world', 8]
while 'world' in a:
    a.remove('world')
print(a)

# 4.1
d = {"title": "a cup of tea", "price": 10, "ingredients": "tea"}
d["description"] = "about tea"
print(d)

# # 4.2
d = {"title": "a cup of tea", "price": 10, "ingredients": "tea"}
d["price"] = 10 * 100
print(d)

# 4.3
d = {"title": "a cup of tea", "price": 10, "ingredients": "tea"}
d["ingredients"] = "tea", "water"
print(d)

# # 4.4
d = {"title": "a cup of tea", "price": 10, "ingredients": "tea"}
d["ingredients"] = "tea", "water"
print(len(d['ingredients']))

# 4.5
d = {"title": "a cup of tea", "price": 10, "ingredients": "tea", "description": "about tea"}
d.pop("description")
print(d)

# 5
while True:
    year = int(input("Write year:"))
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print('YES')
    else:
        print('NO')

# 6
a = int(1)
b = int(8)
c = int(9)
if (c >= (a + b)) or (b >= (a + c)) or (a >= (b + c)):
    print("NO")
else:
    print("YES")

# 7
n = [10, 7, 3, 12, 24]
n.sort()
print(n)
# second
a = int(6)
b = int(7)
c = int(2)
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a, b, c)

# 8
a = int(2)
b = int(2)
c = int(2)
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)
