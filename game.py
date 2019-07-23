from game_status import GameStatus
from player import Player
import random

class Game:
  def __init__(self, settings: dict):
    self.game_status = GameStatus(settings)
  
  def randomize_play_order(self):
    random.shuffle(self.game_status.players)

  def set_turn_order(self, players: list):
    self.game_status.players = players

  def get_current_player(self):
    return self.game_status.players[self.game_status.current_player_index]

  def update_game_status(self):
      # first add current player to finishers if he is done
      if (self.get_current_player().score >= 100 or self.get_current_player().score <= 0):
        self.game_status.finishers.append(self.get_current_player())
      # then update index and maybe round till player that is still in game
      while (self.get_current_player() in self.game_status.finishers):
        self.game_status.current_player_index += 1
        if (self.game_status.current_player_index >= len(self.game_status.players)):
          self.game_status.current_player_index = 0
          self.game_status.current_round += 1
      # then check if it's the end of the game
      if (self.game_status.current_round > self.game_status.round_amount or \
        len(self.game_status.finishers) == len(self.game_status.players)):
        self.game_status.is_game_finished = True

  def perform_action_by_current_player(self, n: int):
    if (n == 1):
      self.get_current_player().try_inc_score()
    if (n == 2):
      self.get_current_player().try_inc_income()
    if (n == 3):
      self.get_current_player().pass_turn()
    self.update_game_status()
