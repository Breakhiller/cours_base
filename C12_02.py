vE1 = {
    "constructeur":"Pinninfarina",
    "modele":"Battista",
    "vitesse":350
    }
vE2 = {
    "constructeur":"Toyota",
    "modele":"Previa",
    "vitesse":200
    }

print(vE1)
print(vE2)

listeV = []
print(type(listeV))
listeV.append(vE1)
listeV.append(vE2)
print(listeV)
print(listeV[1])
print(listeV[1]["modele"])

for i in listeV:
    print(i)
    




