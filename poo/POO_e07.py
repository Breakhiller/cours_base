class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self, years=1):
        self.age += years

    # TODO: ajouter celebrate_birthday()

p=Person("Carlo", 65)
print(p.age)

p.celebrate_birthday(2)
print(p.age)

