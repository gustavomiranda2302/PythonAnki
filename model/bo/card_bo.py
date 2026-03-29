from model.repository.entity.card import Card
from datetime import date, timedelta
class CardBO:
    def revisar_card(self, card : Card, nota: int) -> Card:
        
        card.fator_d = card.fator_d + (0.1 -(5- nota) * (0.08 + (5 - nota) * 0.02))
        card.fator_d = max(card.fator_d, 1.3)
        
        if (nota < 3):
            card.intervalo = 1
        else:
            if(card.intervalo == 0):
                card.intervalo = 1
            elif( card.intervalo == 1):
                card.intervalo = 6
            else:
                card.intervalo = int(card.intervalo * card.fator_d)
        card.proxima_review = date.today() + timedelta(days= card.intervalo)
        
        return card
    
            