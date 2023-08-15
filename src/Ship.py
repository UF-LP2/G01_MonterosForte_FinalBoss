

class Ship:
  contador = 0

  def __init__(self, draft, crew):
    self.draft = draft
    self.crew = crew
    Ship.contador += 1
 
  def is_worth_it(self) ->float:
    borradorFinal = self.draft - self.crew*1.5
    if borradorFinal < 20:
      raise ValueError("No merece ser saqueado.")
    
    return borradorFinal

