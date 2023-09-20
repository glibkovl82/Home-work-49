class Person:
    '''class Person виводить імена і рахунки людей'''

    def __init__(self, name = "xxx", money = 0):
        self.name = name
        self.money = money
        print("A new Person is born! = ", self.name)

    def __str__(self):
        return self.name + str(self.money)
    def giveMoney(self, delta):
        self.money += delta
        print(f'Рахунок {self.name} поповнено на суму {delta}, всього = {self.money}')

A = Person()
B = Person()
C = Person("Petro", 10)
D = Person("ira", 30)
print(f"Tom: Name = {A.name}, money = {A.money:.2f}")
print(f"Tom: Name = {B.name}, money = {B.money:.2f}")

A.name = "Ivan"
B.name = "Anna"
B.money = 100.2852

A.giveMoney(50.127)
B.giveMoney(40)

print(f"Tom: Name = {A.name}, money = {A.money:.2f}")
print(f"Tom: Name = {B.name}, money = {B.money:.2f}")
def info(person):
    i = person.name + str(person.money)
    return i
people = [A, B, C, D]
for p in people:
   print(p)
# help(Person)
print(Person.__doc__)
