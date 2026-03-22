class Deck:
    
    def __init__(self, id, name, description, cards: list[Card] = None):
        self.id = id
        self.name = name
        self.description = description
        self.cards = cards if cards is not None else []
