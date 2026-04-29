""" test_application.py
A few basic tests for the veterinary practice application.
(Many more tests should be used -- no need to add tests for the provided code but you may wish to add test to help you develop/test the code you add.)
"""
import appointment
from appointment import Appointment
from prescription import PrescriptionStatus
from veterinary_practice import veterinary_practice

vp = veterinary_practice()

def setup():
    """ Create a pet to be used by the different tests """
    global vp
    vp = veterinary_practice()    
    vp.register_pet("Kitty", "Tim", "cat") 
    return vp.find_owner("Tim").find_pet("Kitty")

def test_register_pet():    
    setup() # creates a pet

    # find the owner to they have been registered
    owner = vp.find_owner("Tim")
    assert owner.name == "Tim"
    # find the  pet to confirm they have been registered
    pet = owner.find_pet("Kitty")
    assert pet.name == "Kitty"

def test_appointments():
    """NOTE: You could add a similar test for checking your decorated appointment works"""
    pet = setup() # creates a pet    
    appointment.input = lambda: "input" # overrides the input() function within the appointment.py file.

    a = Appointment(pet, "Today") #<-- change this line to test your appointment code
    vp.create_appointment(a)

    notes = vp.attend_appointment(0)
    
    assert notes == ['weight= input', 'input']
    # to test your appointment code:
    #assert notes == ['weight= input', 'input', 'vaccination = input', 'vaccination = input', 'surgery= input']


def test_prescription_too_little_stock():
    """NOTE: You could extend this test to test your observer pattern works"""
    pet = setup() # creates a pet 

    # create medication
    vp.stock_medication("med1", 3)
    med = vp.find_medication("med1")
    assert med.name == "med1"

    # create a prescription that there isn't enough stock for
    id = vp.create_prescription(pet, med, 5)
    prescription = vp.find_prescription(id)
    assert prescription.status == PrescriptionStatus.out_of_stock

def test_prescription_with_stock():
    pet = setup() # creates a pet 

    # create medication
    vp.stock_medication("med1", 3)
    med = vp.find_medication("med1")

    # create a prescription that there is enough stock for
    id = vp.create_prescription(pet, med, 2)
    prescription = vp.find_prescription(id)
    assert prescription.status == PrescriptionStatus.preparing_order

    # prepare the prescription
    vp.prepare_prescription_for_collection(id)
    assert prescription.status == PrescriptionStatus.ready_for_collection

    # collect the prescription
    vp.collect_prescription(id)
    assert prescription.status == PrescriptionStatus.collected