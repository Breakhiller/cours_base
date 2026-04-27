class Person:
    # TODO: définir __init__ avec name et age
    def __init__(self, name, age):
        self.name = name
        self.age = age

# TODO: créer un objet et afficher ses attributs
p = Person("Alice", 25)

print(f"nom : {p.name}")
print(f"age : {p.age}")
