""" veterinary_practice.py
Contains the veterinary_practice class
"""
from medication import Medication
from owner import Owner
import utils

class veterinary_practice:
    """ Holds the data required for the Veterinary Practice application and allows:
        - pets to be registered
        - appointments for pets to be created and attended
        - medications to be stocked
        - prescriptions to be created, prepared and collected.

        Note, in a real systems, use data storage rather than a set of arrays and an MVC architecture.
    """

    def __init__(self):
        """ initialise empty arrays to store the veterinary_practice data """
        self.owners = []
        self.medications = []
        self.prescriptions = []
        self.appointments = []

    def register_pet(self, pet_name, owner_name, species):
        """ Registers a pet with the vets. 
            If the owner does not exist, a new owner is created.
        
        :param self
        :param pet_name (string): The name of the pet
        :param owner_name (string): The name of a new or existing owner
        :param species (string): The pet's species
        """
        owner = self.find_owner(owner_name)
        if not owner:
            owner = Owner(owner_name)
            self.owners.append(owner)

        owner.add_pet(pet_name, species)

    def create_appointment(self, appointment):
        """ Adds the appointment and returns the appointment ID (the ID is list index)"""
        self.appointments.append(appointment)

        return len(self.appointments) - 1

    def attend_appointment(self, appointment_id):
        """  Allows the appointment to be attended.
        :param appointment_id (int): The list index of the appointment

        :returns The notes made during the appointment or an error message.
        """
        appointment = self.find_appointment(appointment_id)
        if appointment:
            appointment.attend_appointment()
            return appointment.get_notes()
        else:
            return "Unrecognized appointment ID"
     

    def stock_medication(self, medication_name, amount):
        """ Find the medication by the given name or, if it does not exist, creates the medication.
            Updates the amount of mediation that is in stock.
            
        :param medication_name: The name of the medication to be created/updated.
        :param amount: The amount to increase the stock by.
        """
        medication = self.find_medication(medication_name)
        if medication: # medication exists
            medication.restock(amount)
        else: # medication does not exist
            medication = Medication(medication_name, amount)
            self.medications.append(medication)

    def create_prescription(self, pet, medication, dosage):
        """ Create a prescription for a pet.
        
        :param pet (Pet): The pet to create the prescription for
        :param medication (Medication): The medication the prescription is for
        :param dosage (int): The amount of medication to be given

        :returns the prescription ID (the ID is list index)
        """
        prescription = pet.create_prescription(medication, dosage)
        self.prescriptions.append(prescription)

        return len(self.prescriptions) - 1    
        
    def prepare_prescription_for_collection(self, prescription_id):
        """ Attempts to change the prescription status from being prepared to ready for collection
        
        :param prescription_id: The ID of the prescription to be prepared
        :returns message (string)
        """
        prescription = self.find_prescription(prescription_id)
        if prescription:
            if prescription.prepareForCollection():     
                return "Prescription prepared"
            return "Prescription is not ready for preparation"
        else:
            return "Unrecognized prescription ID"
        
    
    def collect_prescription(self, prescription_id):
        """ Attempts to change the prescription status from ready for collection to collected.
        
        :param prescription_id: The ID of the prescription to be collected
        :returns message (string)
        """
        prescription = self.find_prescription(prescription_id)
        if prescription:
            if prescription.collect():
                return "Prescription collected"
            return "Prescription is not ready for collection"
        else:
            return "Unrecognized prescription ID"
    

    #===================================
    # Basic access methods

    def has_owners(self):
        return len(self.owners) > 0
    
    def has_medications(self):
        return len(self.medications) > 0
    
    def has_prescriptions(self):
        return len(self.prescriptions) > 0

    def find_owner(self, name):
        return utils.find_by_name(name, self.owners)
        
    def find_medication(self, name):
        return utils.find_by_name(name, self.medications) 
    
    def find_prescription(self, id):
        if id < len(self.prescriptions):
            return self.prescriptions[id]
        return None
    
    def find_appointment(self, id):
        if id < len(self.appointments):
            return self.appointments[id]
        return None
    

# EOF    
#------