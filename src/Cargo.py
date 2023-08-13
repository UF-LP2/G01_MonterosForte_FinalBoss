import Ship

class Cargo(Ship):
   def __init__(self, cargo, quality, draft, crew):
       Ship.__init__(self, draft, crew)
       self.cargo = cargo
       self.quality = quality

   def is_worth_it(self) ->float:
       self.draft - (self.crew*1.5)

       if self.draft <= 0:
           raise ValueError
       elif self.quality == 1:
           self.draft - self.cargo*3.5
       elif self.quality == 0.5:
           self.draft - self.cargo*2
       elif self.quality == 0.25:
           self - self.cargo*0.5
       else:
           raise ValueError


       return self.draft