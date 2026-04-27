class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def affiche_infos(self):
        print(f"Nom : {self.name}")
        print(f"Age : {self.age}")

# TODO: créer deux objets différents et afficher leurs infos
p1 = Person("Carlo", 65)
p2 = Person("Rosemarie", 57)

p1.affiche_infos()
p2.affiche_infos()
