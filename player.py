class Player:
  def __init__(self, settings: dict):
    self.color = settings.get('color')
    self.name = settings.get('name')
    self.score = settings.get('score_sum')
    self.income = settings.get('income_sum')
  
  def try_inc_score(self):
    pass
  
  def try_inc_income(self):
    pass
  
  def pass_turn(self):
    pass
  
  def get_status(self):
    return {
      'color': self.color,
      'name': self.name,
      'score': self.score,
      'income': self.income
    }
