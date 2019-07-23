from player import Player

class GameStatus:
  def __init__(self, settings: dict):
    self.round_amount = settings.get('round_amount', 10)
    self.players = []
    for player in settings.get('players', []):
      self.players.append(Player({
        'name': player.get('name'),
        'color': player.get('color'),
        'init_score': settings.get('init_score'),
        'init_income': settings.get('init_income')
      }))
    self.current_player_index = 0
    self.current_round = 1
    self.finishers = []
    self.is_game_finished = False