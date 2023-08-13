import Ship

class Cruise(Ship):
   def __init__(self, passengers, draft, crew):
      Ship.__init__(self, draft, crew)
      self.passengers = passengers

   def is_worth_it(self) ->float:
      self.draft - self.passengers*2.25
      self.draft - self.crew*1.5
      
      return self.draft 

