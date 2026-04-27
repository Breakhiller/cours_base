class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # TODO: ajouter une méthode say_hello
    def say_hello(self):
        print(f"Bonjour, je m'appelle {self.name}")
        
p = Person("Carlo", 65)

p.say_hello()




