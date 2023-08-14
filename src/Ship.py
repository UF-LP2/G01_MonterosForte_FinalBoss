

class Ship:
  max_ = 200

  def __init__(self, draft, crew):
    self.draft = draft
    self.crew = crew
  def is_worth_it(self) ->float:
    borradorFinal = self.draft - self.crew*1.5
    return borradorFinal

