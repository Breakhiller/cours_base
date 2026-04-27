class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)
print("Avant :", p.age)

# TODO: modifier l'âge en 26 ici
p.age = 26
print("Après :", p.age)
