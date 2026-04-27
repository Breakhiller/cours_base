class Cours:
    def __init__(self, titre, etudiants, duree):
        self.titre = titre
        self.etudiants = etudiants
        self.duree = duree

    def afficher_infos(self):
        print("Cours : "+self.titre)
        print(f"Etudiants : {self.etudiants}")
        print(f"Temps : {self.duree} min")

    def ajouter_etudiant(self):
        self.etudiants += 1
        
c1 = Cours(titre="250+ Exercices en Python", etudiants=1000, duree=60)
c2 = Cours("100+ Exercices en POO", 0, 30)

c1.afficher_infos()
c2.afficher_infos()



