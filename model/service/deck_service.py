from model.repository.deck_repository import DeckRepository

class DeckService:
    def __init__(self, deckrepo: DeckRepository):
        self.deckrepo = deckrepo

    def listar_decks(self):
        return self.deckrepo.list_all()

    def get_id_deck(self, deck_id):
        return self.deckrepo.get_by_id(deck_id)

    def atualizar_deck(self, deck_id):
        return self.deckrepo.update(deck_id)