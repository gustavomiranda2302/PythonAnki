from datetime import datetime
class Card:
    def __init__(self,id, name, description, proxima_review: datetime, intervalo: int, fator_d: float):
        self.id = id
        self.name = name
        self.description = description
        self.intervalo = intervalo
        self.proxima_review = proxima_review
        self.fator_d = fator_d
        