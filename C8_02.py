temp = float(input("Temp ? "))
sous = float(input("Sous ? "))
if  (sous > 5):
    print("sous")
    if  (temp > 27):
        print("Glace")
    elif(temp < 15):
        print("pain")
    else:
        print("macaron")
print("fin")
