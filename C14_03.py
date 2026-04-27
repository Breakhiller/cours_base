def addition(x,y):
    print(str(x+y))

def soustraction(x,y):
    print(str(x-y))

def enter():
    y=x

action = {
    "+": addition,
    "-": soustraction,
    "enter": enter
    }

x=0.0
y=0.0

while(True):
    appel=input("saisie : ")

    if appel == "end":
        break

    if appel in action:
        if  appel in ["+", "-"]:
            resultat=action[appel](x,y)
            print("x = "+str(x))
            print("y = "+str(y))
        else:
            resultat=action[appel]()
            print("x = "+str(x))
            print("y = "+str(y))
        print("fait")
    else:
        try:
            x=float(appel)
            print("x = "+str(x))
            print("y = "+str(y))
        except ValueError:
            print("saisie non numérique")

print("à bientôt")
