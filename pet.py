from prescription import Prescription

class Pet:
    def __init__(self, name, owner, species):
        self.name = name
        self.owner = owner
        self.species = species

        self.appointments = []
        self.vaccinations = []
        self.prescriptions = []

    def create_prescription(self, medication, dosage):
        prescription = Prescription(self, medication, dosage)
        self.prescriptions.append( prescription )
        return prescription
    
    def add_vaccination(self, vaccination):
        self.vaccinations.append(vaccination)

    def add_appointment(self, appointment):
        self.appointments.append(appointment)