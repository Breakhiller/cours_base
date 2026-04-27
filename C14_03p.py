def addition(x,y):
    pile["X"] = pile["Y"] + pile["X"]
    tourner()

def soustraction(x,y):
    pile["X"] = pile["Y"] - pile["X"]
    tourner()

def multiplication(x,y):
    pile["X"] = pile["Y"] * pile["X"]
    tourner()

def division(x,y):
    pile["X"] = pile["Y"] / pile["X"]
    tourner()

def carre():
    pile["X"] = pile["X"] ** 2

def pi():
    enter()
    pile["X"] = 3.1416
    
def enter():
    pile["T"] = pile["Z"]
    pile["Z"] = pile["Y"]
    pile["Y"] = pile["X"]

def tourner():
    pile["Y"] = pile["Z"]
    pile["Z"] = pile["T"]

def afficher():
    print("T = "+str(pile["T"]))
    print("Z = "+str(pile["Z"]))
    print("Y = "+str(pile["Y"]))
    print("X = "+str(pile["X"]))

pile = {
    "X": 0.0,
    "Y": 0.0,
    "Z": 0.0,
    "T": 0.0
    }

action = {
    "+": addition,
    "-": soustraction,
    "*": multiplication,
    "/": division,
    "x2": carre,
    "pi": pi,
    "enter": enter
    }

calc=False

while(True):
    appel=input("saisie : ")

    if appel == "end":
        break

    if appel in action:
        if  appel in ["+", "-", "*", "/"]:
            resultat=action[appel](pile["X"],pile["Y"])
            calc=True
            afficher()
#            print("X="+str(pile["X"]))
        else:
            resultat=action[appel]()
            afficher()
        print(str(pile["X"]))
    else:
        try:
            if  calc:
                pile["Y"]=pile["X"]
            pile["X"]=float(appel)
#            calc=True
            afficher()
#            print("x = "+str(pile["X"]))
#            print("y = "+str(pile["Y"]))
        except ValueError:
            print("saisie non numérique")

print("à bientôt")
