import json 

class DuplicateNameError(Exception):
    pass 

class NeighborhoodPets: 
    def __init__(self):
        self._pets = {}
        self._pets_json_file = None
    
    def add_pet(self, pet_name, pet_species, pet_owner_name):
        if pet_name in self._pets:
            raise DuplicateNameError('A neighborhood pet already has that name.')
        else: 
            self._pets[pet_name] = {'species': pet_species, 'owner': pet_owner_name}

    def delete_pet(self, pet_name):
        if pet_name in self._pets:
            del self._pets[pet_name]
    
    def get_owner(self, pet_name): 
        if pet_name in self._pets:
            return self._pets[pet_name]['owner']

    def save_as_json(self,file_name):
        with open(file_name, 'w') as outfile:
            json.dump(self._pets, outfile)

    def read_json(self, file_name):
        with open(file_name, 'r') as infile:
            self._pets = json.load(infile)

    def get_all_species(self):
        species = set() 
        for pet in self._pets:
            if pet not in species:
                species_name = self._pets[pet]['species']
                species.add(species_name)
        print(species) 

    #get all species 

np = NeighborhoodPets()
try:
    np.add_pet("Fluffy", "gila monster", "Oksana")
    np.add_pet("Tiny", "stegasaurus", "Rachel")
    np.add_pet("Spot", "zebra", "Farrokh")
except DuplicateNameError:
    print('You tried to enter a pet with the same name as another pet.')
np.save_as_json("pets.json")
np.delete_pet("Tiny")
spot_owner = np.get_owner("Spot")
np.read_json("other_pets.json")
species_set = np.get_all_species()