def accueil():
    print("Bonjour")

def surface(rayon):
    print("La surface est de "+str(rayon*3.1415926535))

def surf2(rayon):
    surface=rayon*3.1415926535
    return surface
    
accueil()
print("")

r = float(input("rayon ? "))
surface(r)
print("")

print("Surface : "+str(surf2(r)))
print("fin")

