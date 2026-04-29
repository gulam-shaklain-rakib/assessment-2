"""
medication.py
contains the medication class
"""

class Medication:
    def __init__(self, name, amount_in_stock):
        """
        :param name: the name of the medication
        :param amount_in_stock: how much is in stock
        """
        self.name = name
        self.amount_in_stock = amount_in_stock
        self.observers = []  # added for observer pattern

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

    def restock(self, amount):
        """
        Increase stock by given amount
        """
        self.amount_in_stock += amount
        self.notify_observers()

    def reduce_stock(self, amount):
        """
        Decrease stock by given amount
        """
        self.amount_in_stock -= amount
        self.notify_observers()

    def has_enough_stock(self, dosage):
        """
        Check if there is enough stock
        """
        return self.amount_in_stock >= dosage
