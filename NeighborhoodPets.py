# Author: Zihan Li
# Date: 2020/2/5
# Description: a class named NeighborhoodPets that has methods for adding a pet, deleting a pet, searching for
#              the owner of a pet, saving data to a JSON file, loading data from a JSON file, and getting a
#              list of all pet species.

import json

class NeighborhoodPets:
    def __init__(self):
        super().__init__()
        self.Allpet = {}
        # declare a dict to store all pet species

    def add_pet(self, pet_name, species, owner_name):
        if pet_name not in self.Allpet:
        # if a pet does not have the same name as a pet that has already been added
            self.Allpet[pet_name] = {"pet's name:": pet_name, "pet's species:": species, "owner:": owner_name}

    def delete_pet(self, pet_name):
        if pet_name in self.Allpet:
        # check a pet's name
            self.Allpet.pop(pet_name)
            # removed the pet's name

    def get_owner(self, pet_name):
        if pet_name in self.Allpet:
        # check a pet's name
            return self.Allpet[pet_name]["owner"]

    def save_as_json(self, file_name):
        pet_file = self.Allpet
        with open(file_name, 'w') as outfile:
            json.dump(pet_file, outfile)
            # save the file in json format with a name you want

    def read_json(self, file_name):
        with open(file_name, 'r') as infile:
            self.Allpet = json.load(infile)
            # read and loads that file

    def get_all_species(self):
        Allpet = {pet["pet's species"] for pet in self.Allpet.values()}
        # find all species of pet and save in a set
        return Allpet
        # returns the set
