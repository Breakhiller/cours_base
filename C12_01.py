vE = {
    "constructeur":"Pinninfarina",
    "modele":"Battista",
    "vitesse":350
    }
print(vE)
print(type(vE))
print(len(vE))
print(vE.get("vitesse"))
print(type(vE.get("vitesse")))
print(vE["modele"])

vE["vitesse"] = 320
print(vE)

vE["Cylindrée"] = "8.0 L"
print(vE)

      

