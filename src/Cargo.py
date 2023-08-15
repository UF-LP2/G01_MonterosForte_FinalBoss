from src.Ship import Ship

class Cargo(Ship):
   def __init__(self, cargo, quality, draft, crew):
       Ship.__init__(self, draft, crew)
       self.cargo = cargo
       self.quality = quality


   def is_worth_it(self) ->float:
       borradorFinal = self.draft - self.crew*1.5

       if self.quality == 1:
           borradorFinal -= self.cargo*3.5
       elif self.quality == 0.5:
           borradorFinal -= self.cargo*2
       elif self.quality == 0.25:
           borradorFinal -= self.cargo*0.5
       else:
           raise ValueError # Por si en quality hay un valor incorrecto
       
       if borradorFinal < 20:
           raise Exception("No merece ser saqueado.")

       return borradorFinal