from model.repository.mapper.deck_mapper import DeckMapper
from model.repository.deck_repository import DeckRepository
from model.repository.json.json_handler import JsonHandler
class DeckRepositoryImpl(DeckRepository):
    def __init__(self, json_handler):
        self.json_handler = json_handler
    
    def list_all(self):
        data = self.json_handler.load_json()
        return [DeckMapper.deck_to_entity(deck) for deck in data]
    
    def get_deck_by_id(self, id):
        data = self.json_handler.load_json()
        for i in data:
            if i["id"] == id:
                return DeckMapper.deck_to_entity(i)
        return None
    
    def create_deck(self, deck):
        data = self.json_handler.load_json()
        data.append(DeckMapper.deck_to_dict(deck))
        self.json_handler.save_json(data)
        
    def delete_deck(self, id):
        data = self.json_handler.load_json()
        for i in data:
            if i["id"] == id:
                 data.remove(i)
                 self.json_handler.save_json(data)
        return None
    
    
    def update_deck(self, deck):
        data = self.json_handler.load_json()
        for i, item in enumerate(data):
                if item["id"] == deck.id:
                    data[i] = DeckMapper.deck_to_dict(deck)
                    self.json_handler.save_json(data)
