class AnimalShelter:

    def __init__(self):
        self.selfdict = {}

    def addAnimal(self, animal):
            species = animal.species
            if species in self.selfdict:
                self.selfdict[species].append(animal)
            else:
                self.selfdict[species] = [animal]

    def removeAnimal(self, animal):
        if animal.species is not None: 
            species = animal.species
            if species in self.selfdict:
                for oldanimal in self.selfdict[species]:
                    if oldanimal.name == animal.name and oldanimal.weight == animal.weight and oldanimal.age == animal.age:
                        self.selfdict[species].remove(oldanimal)
                        return True
                    else:
                        return False
            else:
                return False
        else:
            return False
    
    
    def removeSpecies(self, species):
            if species.upper() in self.selfdict:
                del self.selfdict[species.upper()]
                return ''
            else:
                return ''

    def getAnimalsBySpecies(self, species):
        species = species.upper()  # Convert to uppercase
        if species in self.selfdict:
            string = ""
            for animal in self.selfdict[species][:-1]:
                string += animal.toString() + "\n"
            string += self.selfdict[species][-1].toString()
            return string
        else:
            return ""

    def doesAnimalExist(self, animal):
            species = animal.species
            if species in self.selfdict:
                for oldanimal in self.selfdict[species]:
                    if oldanimal.name == animal.name and oldanimal.weight == animal.weight and oldanimal.age == animal.age:
                       return True
                    else:
                        return False
            else:
                return False
