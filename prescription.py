
"""
prescription.py
Contains the Prescription class and the PrescriptionStatus enum.
"""

from enum import Enum


class PrescriptionStatus(Enum):
    """ Used to track the status of the prescription  """
    preparing_order = 1  # if the medication is in stock, prepare medication before collection
    ready_for_collection = 2  # after preparation, ready for collection
    out_of_stock = 3  # if not enough stock available
    collected = 4  # final state: medication collected


class Prescription:
    """
    When the prescription is created:
        If enough medication is in stock, status is preparing_order.
        If not enough medication is in stock, status is out_of_stock.

        YOUR TASK: Automatically update status when medication stock changes.
    """

    def __init__(self, pet, medication, dosage):
        """
        :param pet: Pet the prescription is for
        :param medication: Medication object
        :param dosage: required dosage
        """
        self.pet = pet
        self.medication = medication
        self.dosage = dosage

        # Observer pattern registration
        self.medication.attach(self)

        self._prepareOrWaitForStock()

    # =========================
    # OBSERVER METHOD (ADDED)
    # =========================
    def update(self, medication):
        """
        Called automatically when medication stock changes
        """
        if self.status == PrescriptionStatus.collected:
            return
        self._prepareOrWaitForStock()

    # =========================
    # ORIGINAL LOGIC (UNCHANGED)
    # =========================
    def _prepareOrWaitForStock(self):
        """
        Checks medication stock and updates status
        """
        if self.medication.has_enough_stock(self.dosage):
            self.status = PrescriptionStatus.preparing_order
        else:
            self.status = PrescriptionStatus.out_of_stock

    def prepareForCollection(self):
        """
        Moves prescription to ready_for_collection if possible
        """
        if self.status == PrescriptionStatus.preparing_order:
            self.medication.reduce_stock(self.dosage)
            self.status = PrescriptionStatus.ready_for_collection
            return True
        return False

    def collect(self):
        """
        Marks prescription as collected
        """
        if self.status == PrescriptionStatus.ready_for_collection:
            self.status = PrescriptionStatus.collected

            # stop observing after completion
            self.medication.detach(self)

            return True
        return False


# EOF
