#1
class Person:
   def __init__(self, full_name, age):
       self.full_name = full_name
       self.age = age
   def full_name(self):
       return self.full_name()
   def year(self):
       return self.age

p1 = Person('Yulia Nevm', 24)
print(p1.full_name)
print(p1.age)






