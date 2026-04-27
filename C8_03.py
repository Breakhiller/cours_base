print("1 : Montagnes russes")
print("2 : Carrousels")
choix = int(input("Choix ? "))
if  (choix == 1):
    taille = float(input("Votre taille en cm ? "))
    print(taille)
    if  (taille >= 121.5):
        print("OK pour les montagnes russes")
    else:
        print("Taille trop petite")
elif(choix == 2):
        print("Bon caroussels")
print("fin")
