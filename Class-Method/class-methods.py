# # class

# class Person:
#     # class attriibutes
#     address = 'no information'

#     # constructor (yapici metod)
#     def __init__(self, name, year):
        
#         # object attributes
#         self.name = name
#         self.year = year
        
#     # instance methods
#     def intro(self):
#         print('Hello There. I am '+ self.name)

#     def calculateAge(self):
#         return 2019 - self.year

# # object, instance
# p1 = Person(name= 'Ali', year= 1990)
# p2 = Person(name= 'Yagmur', year= 1995)

# p1.intro()
# p2.intro()

# print(f'adim: {p1.name} ve yasim: {p1.calculateAge()}')
# print(f'adim: {p2.name} ve yasim: {p2.calculateAge()}')


class Circle:
    # Class object attribute
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    # Methods
    def cevre_hesapla(self):
        return 2 * self.pi + self.yaricap

    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)

c1 = Circle()   #yaricap = 1
c2 = Circle(5)  

print(f'c1 : alan = {c1.alan_hesapla()} cevre = {c1.cevre_hesapla()}')
print(f'c2 : alan = {c2.alan_hesapla()} cevre = {c2.cevre_hesapla()}')

