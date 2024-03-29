import random

SCORE_PASSIVE_INCREMENT = 5

SCORE_INCREASE_CHANCE = 25
SCORE_INCREMENT_BASE = 5
SCORE_DECREMENT_BASE = 5

INCOME_INCREASE_CHANCE = 65
INCOME_INCREMENT_BASE = 5
INCOME_DECREMENT_BASE = 5


class Player:

    def __init__(self, settings: dict):
        self.color = settings.get('color')
        self.name = settings.get('name')
        self.score = settings.get('init_score')
        self.income = settings.get('init_income')

        self.score_incr_chance = \
            settings.get('score_incr_chance', SCORE_INCREASE_CHANCE)
        self.income_incr_chance = \
            settings.get('income_incr_chance', INCOME_INCREASE_CHANCE)

        self.score_passive_increment = \
            settings.get('score_passive_increment', SCORE_PASSIVE_INCREMENT)

        self.score_increment_base = \
            settings.get('score_increment_base', SCORE_INCREMENT_BASE)
        self.score_decrement_base = \
            settings.get('score_decrement_base', SCORE_DECREMENT_BASE)

        self.income_increment_base = \
            settings.get('income_increment_base', INCOME_INCREMENT_BASE)
        self.income_decrement_base = \
            settings.get('income_decrement_base', INCOME_DECREMENT_BASE)

        self.__random = random.Random()

    def try_inc_score(self) -> bool:
        if self.__random.randint(1, 100) <= self.score_incr_chance:
            self.score = self.score + self.score_increment_base
            return True
        else:
            self.score = self.score - self.score_decrement_base
            return False

    def try_inc_income(self) -> bool:
        if self.__random.randint(1, 100) <= self.income_incr_chance:
            self.income = self.income + self.income_increment_base
            return True
        else:
            self.income = self.income - self.income_decrement_base
            return False

    def pass_turn(self):
        self.score += self.score_passive_increment

    def get_status(self):
        return {
            'color': self.color,
            'name': self.name,
            'score': self.score,
            'income': self.income
        }
