class Cours:
    pass

c = Cours()
c.etudiants = 0
c.duree = 120

print(f"Etudiants : {c.etudiants}")
# identique à print("Etudiants : "+str(c.etudiants))
print(f"Temps : {c.duree}")

# comparé à un dictionnaire :

d = {"etudiants" : 0, "duree" : 120}
print(f"Etudiants : {d['etudiants']}")
print(f"Temps : {d['duree']}")



