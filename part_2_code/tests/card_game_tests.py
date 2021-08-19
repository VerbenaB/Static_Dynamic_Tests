import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Heart", 2)
        self.card2 = Card("Diamond", 8)
        self.cardgame = CardGame()
        self.cards = [self.card1, self.card2]

    def test_check_for_ace(self):
        self.assertEqual(False, self.cardgame.check_for_ace(self.card1))

    def test_highest_card(self):
        self.assertEqual(self.card2, self.cardgame.highest_card(self.card1, self.card2))

    def test_cards_total(self):
        self.assertEqual("You have a total of 10", self.cardgame.cards_total(self.cards))