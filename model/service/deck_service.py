from model.repository.deck_repository import DeckRepository
from model.repository.entity.deck import Deck

class DeckService:
    def __init__(self, deckrepo: DeckRepository):
        self.deckrepo = deckrepo
       

    def listar_decks(self):
        return self.deckrepo.list_all()

    def get_id_deck(self, deck_id):
        return self.deckrepo.get_deck_by_id(deck_id)

    def atualizar_deck(self, deckobj : Deck):
        return self.deckrepo.update_deck(deckobj)
    def criar_deck(self, deckobj: Deck):
        return self.deckrepo.create_deck(deckobj)
    def deletar_deck(self, deck_id):
            return self.deckrepo.delete_deck(deck_id)

   