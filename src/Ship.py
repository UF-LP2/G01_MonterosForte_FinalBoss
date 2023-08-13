class Ship:
  max_ = 200
  def __init__(self, draft, crew):
         self.draft = draft
         self.crew = crew

  def get_draft(self):
         return self.draft
  def get_crew(self):
        return self.crew
  def is_worth_it(self)->float:
        return (self.draft-(self.crew*1.5))