def addition(a, b):
    return a + b

def bonjour():
    print("Bonjour !")

actions = {
    "addition": (addition, 2),
    "bonjour": (bonjour, 0)
}

while True:
    nom = input("Fonction (ou q) : ")

    if nom == "q":
        break

    if nom in actions:
        fonction, nb_args = actions[nom]

        args = []
        print(args)
        print(type(args))
        for i in range(nb_args):
            val = float(input(f"paramètre {i+1} = "))
            args.append(val)
            
        print(args)
        resultat = fonction(*args)

        if resultat is not None:
            print("Résultat :", resultat)
    else:
        print("Fonction inconnue")
