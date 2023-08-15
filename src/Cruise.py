from src.Ship import Ship

class Cruise(Ship):
   def __init__(self, passengers, draft, crew):
      Ship.__init__(self, draft, crew)
      self.passengers = passengers

   def is_worth_it(self) ->float:
      borradorFinal = self.draft - self.passengers*2.25 - self.crew*1.5
      if borradorFinal < 20:
         raise Exception("No merece ser saqueado.")

      return borradorFinal

