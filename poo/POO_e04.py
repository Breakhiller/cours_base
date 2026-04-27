class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # TODO: ajouter show_age()
    def show_age(self):
        print(f"{self.name}, j'ai {self.age} ans")

p1 = Person("Carlo", 65)
p2 = Person("Rosemarie", 57)

p1.show_age()
p2.show_age()
