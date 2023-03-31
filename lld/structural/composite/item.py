from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def return_price(self):
        pass