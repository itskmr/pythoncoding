class Dog():
    species = 'mamals'

    def __init__(self , breed , name):
        self.breed = breed
        self.name = name

dog1 = Dog ('Lab' , "Ruhil")

print(dog1.breed)
print(dog1.name)
print(dog1.species)