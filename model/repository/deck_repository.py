from abc import ABC, abstractmethod
from model.repository.entity.deck import deck
class DeckRepository(ABC):
    
    @abstractmethod
    def create_deck(self, deck: deck):
        pass
    
    @abstractmethod
    def get_deck_by_id(self, id) -> deck:
        pass
    
    @abstractmethod
    def update_deck(self, deck: deck):
        pass
    
    @abstractmethod
    def delete_deck(self, id):
        pass
    @abstractmethod
    def list_all(self) -> list[deck]:
        pass