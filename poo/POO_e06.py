class Person:
    def __init__(self, name, age, city="ville inconnue"):  # Ajouter un attribut avec valeur par défaut après age 
        self.name = name
        self.age = age
        self.city = city

    def age_dans_5_ans(self):
        return self.age + 5

# TODO: créer 2 Person : une avec et une sans préciser la ville
p1 = Person("Carlo", 65, "Frinvillier")
p2 = Person("Romain", 25)

print(f"{p1.name}, {p1.city}")
print(f"{p2.name}, {p2.city}")

print(p2.age_dans_5_ans())

            
