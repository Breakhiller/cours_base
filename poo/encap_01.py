class Cours:
    def __init__(self, titre, etudiants, duree):
        self.titre = titre
        self.duree = duree
        self.__etudiants = etudiants

    def get_etudiants(self):
        return self.__etudiants

    def set_etudiants(self, valeur):
        if  valeur >= 0:
            self.__etudiants = valeur
        else:
            print("Erreur : nombre doit être positif")
        
c = Cours("100+ Exercices en POO", 100, 30)
print(c.get_etudiants())
c.set_etudiants(-50)
print(c.get_etudiants())






