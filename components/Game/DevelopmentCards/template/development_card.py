from abc import ABC, abstractmethod

class DevelopmentCard(ABC):
    """
    This is the template for the development cards.
    """
    def __init__(self, name: str):
        self.name: str = name

    @abstractmethod
    def use_card(self):
        """
        This is where the logic for the development card will go.
        """