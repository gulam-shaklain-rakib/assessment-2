""" owner.py
Contains the Owner class
"""
from pet import Pet
import utils

class Owner:
    """ Owners have a name and a list of pets  """
    def __init__(self, name):
        """ Owner's __init__    
        Initializes an empty list of pets.    
        :param self
        :param name: Name of the owner 
        """
        self.name = name
        self.pets = []

    def add_pet(self, name, species):
        """
        Creates a new pet for this owner.
        
        :param self
        :param name: name of pet
        :param species: species of pet
        """
        self.pets.append(Pet(name, self, species))

    
    def find_pet(self, name):
        return utils.find_by_name(name, self.pets)