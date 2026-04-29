"""
prescription.py
Contains the Prescription class and the PrescriptionStatus enum.
"""

from enum import Enum


class PrescriptionStatus(Enum):
    """ Used to track the status of the prescription  """
    preparing_order = 1  # if the medication is in stock, the pharmacist needs to prepare the medication before it can be collected.
    ready_for_collection = 2  # after the pharmacist has prepared the medication, it becomes ready for collection.
    out_of_stock = 3  # when the medication is restocked, the status should become preparing_order
    collected = 4  # end status: the medication has been collected.


class Prescription:
    """
    When the prescription is created:
        If enough medication is in stock, the prescription status is preparing_order.
        If there isn't enough medication in stock, the status is out_of_stock.
        Currently this state is only set when the prescription is created
        YOUR TASK: Automatically update the status to preparing_order or out_of_stock when the medication stock level changes.
    Once the prescription is prepared, its status becomes ready_for_collection.
    Once the prescription is collected, its status becomes collected (and no further action is needed).
    """

    def __init__(self, pet, medication, dosage):
        """ Prescription  __init__

        :param self
        :param pet (Pet): The pet the prescription is for
        :param medication (Medication): The medication to be given to the pet
        :param dosage (int): The amount of medication to be given to the pet
        """
        self.pet = pet
        self.medication = medication
        self.dosage = dosage

        # Observer pattern: register prescription to medication
        self.medication.attach(self)

        self._prepareOrWaitForStock()

    # -----------------------------
    # OBSERVER METHOD (NEW)
    # -----------------------------
    def update(self, medication):
        # called automatically when stock changes
        if self.status == PrescriptionStatus.collected:
            return
        self._prepareOrWaitForStock()

    def _prepareOrWaitForStock(self):
        """ Checks if there is enough medication in stock for this prescription.
        :param self
        """
        if self.medication.has_enough_stock(self.dosage):
            self.status = PrescriptionStatus.preparing_order
        else:
            self.status = PrescriptionStatus.out_of_stock

    def prepareForCollection(self):
        """ If the status is preparing_order, the order becomes ready_for_collection
        :param self
        :return True if the order becomes ready for collection; otherwise, False
        """
        if self.status == PrescriptionStatus.preparing_order:
            self.medication.reduce_stock(self.dosage)
            self.status = PrescriptionStatus.ready_for_collection
            return True
        else:
            return False

    def collect(self):
        """ If the status is ready_for_collection, the order becomes collected
        :param self
        :return True if the order is collected; otherwise, False
        """
        if self.status == PrescriptionStatus.ready_for_collection:
            self.status = PrescriptionStatus.collected

            # stop observing after completion
            self.medication.detach(self)

            return True
        else:
            return False


# EOF
#EOF
#----
