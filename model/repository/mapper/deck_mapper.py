from datetime import datetime

from model.repository.entity.deck import Deck
from model.repository.entity.card import Card

class DeckMapper:
    @staticmethod    
    def deck_to_dict(deck):
        return{
            "id": deck.id,
            "name": deck.name,
            "description": deck.description,
            "cards": [DeckMapper.card_to_dict(card) for card in deck.cards]
        }
    @staticmethod
    def deck_to_entity(data):
        return Deck(
                id=data["id"],
                name=data["name"],
                description=data["description"],
                cards=[DeckMapper.card_to_entity(card) for card in data.get("cards", [])]
        )
    @staticmethod
    def card_to_dict(card):
        return{
            "id": card.id,
            "name": card.name,
            "description": card.description,
            "intervalo": card.intervalo,
            "proxima_review": card.proxima_review.isoformat(),
            "fator_d": card.fator_d
            
        }
    @staticmethod
    def card_to_entity(data):
        return Card(
                id=data["id"],
                name=data["name"],
                description=data["description"],
                intervalo= data["intervalo"],
                proxima_review= datetime.fromisoformat(data["proxima_review"]),
                fator_d= data["fator_d"]
        )
 