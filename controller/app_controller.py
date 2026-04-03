from model.bo.card_bo import CardBO
from model.service.deck_service import DeckService



class AppController:
    def __init__(self, cardbo : CardBO, deckservice: DeckService):
        self.cardbo = cardbo
        self.deckservice = deckservice
        
    
    def revisar_card(self, card_id, nota, deck_id):
        deck_escolhido =self.deckservice.get_id_deck(deck_id)
        for i in deck_escolhido.cards:
            if i.id == card_id:
                card_escolhido = i
                self.cardbo.revisar_card(card_escolhido, nota)
                
        return self.deckservice.atualizar_deck(deck_escolhido)
    
    def criar_card(self,deck_id,card):
        deck_escolhido =self.deckservice.get_id_deck(deck_id)
        deck_escolhido.cards.append(card)
        return self.deckservice.atualizar_deck(deck_escolhido)
    
    def deletar_card(self,deck_id,card_id):
        deck_escolhido = self.deckservice.get_id_deck(deck_id)
        for i in deck_escolhido.cards:
            if i.id == card_id:
                card_escolhido = i
                deck_escolhido.cards.remove(card_escolhido)
        return self.deckservice.atualizar_deck(deck_escolhido)
    
    def editar_card(self,deck_id,card_id,card):
        deck_escolhido = self.deckservice.get_id_deck(deck_id)
        for i in deck_escolhido.cards:
            if i.id == card_id:
                card_escolhido = i
                card_escolhido.name = card.name
                card_escolhido.description = card.description
        return self.deckservice.atualizar_deck(deck_escolhido)
            
               
    


    
    