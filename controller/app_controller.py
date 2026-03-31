from model.bo.card_bo import CardBO
from model.service.deck_service import DeckService



class AppController:
    def __init__(self, cardbo : CardBO, deckservice: DeckService):
        self.cardbo = cardbo
        self.deckservice = deckservice
        
        