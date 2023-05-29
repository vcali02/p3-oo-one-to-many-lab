class Pet:

    #STEP 3
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    #STEP 4
    all = []

    #STEP 2
    def __init__(self, name, pet_type, owner = None):
        #STEP 3
        #if pet_type not in self.PET_TYPES:
         #   raise ValueError("Invalid pet type!")
            #raise Exception("Please enter a valid pet type.")
        #STEP 2
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        #IN PARAMETER owner = "Unknown"
        #self._owner = None

        #STEP 4
        #Class_name + list we want to add to + append(self)
        Pet.all.append(self)

    #STEP 5
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in self.PET_TYPES:
            raise Exception("Please enter a valid pet type.")
        self._pet_type = pet_type

    





class Owner:
    
    #STEP 1
    def __init__(self, name):
        self.name = name

    #STEP 5 method that returns a full list of the owner's pets
    def pets(self):
        #STEP 5 go through all list and check if owner for each pet is equal to self
        return [pet for pet in Pet.all if pet.owner ==self]

    #STEP 6
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Invalid pet type!")
        
        pet.owner = self
       
    

    #STEP 7
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)

DJ = Owner("DJ")
val = Owner("Val")
mom = Owner("Mom")

zeus = Pet("Zeus", "reptile")
melvin = Pet("Melvin", "dog")

winnie = Pet("Winnie", "dog")

mason = Pet("Mason", "dog")


DJ.add_pet(zeus)
DJ.add_pet(melvin)

val.add_pet(winnie)

mom.add_pet(mason)

sorted_pets = val.get_sorted_pets()
for pet in sorted_pets:
    print(pet.name)

print(DJ.pets())

#print(DJ.name)
#print(zeus.name)
#print(zeus.pet_type)

#print(val.name)
#print(winnie.name)
#print(winnie.pet_type)