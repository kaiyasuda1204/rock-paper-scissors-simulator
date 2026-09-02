from __future__ import annotations

import random
import unittest

from rps import BestWinRateStrategy, Move, Outcome, Player, UniformRandomStrategy
from rps.model import judge
from rps.strategies import MoveStats
from test import check_uniformity


class RulesTest(unittest.TestCase):
    def test_each_move_beats_the_expected_move(self) -> None:
        self.assertIs(judge(Move.ROCK, Move.SCISSORS), Outcome.WIN)
        self.assertIs(judge(Move.SCISSORS, Move.PAPER), Outcome.WIN)
        self.assertIs(judge(Move.PAPER, Move.ROCK), Outcome.WIN)

    def test_same_moves_draw(self) -> None:
        for move in Move:
            with self.subTest(move=move):
                self.assertIs(judge(move, move), Outcome.DRAW)


class StrategiesTest(unittest.TestCase):
    def test_nobita_is_uniform_within_one_percentage_point(self) -> None:
        rates, is_uniform = check_uniformity()
        self.assertTrue(is_uniform, rates)

    def test_suneo_chooses_the_move_with_the_best_win_rate(self) -> None:
        history = {move: MoveStats(plays=10, wins=1) for move in Move}
        history[Move.PAPER] = MoveStats(plays=10, wins=8)
        strategy = BestWinRateStrategy(random.Random(0))

        self.assertIs(strategy.choose(history), Move.PAPER)

    def test_suneo_randomly_breaks_a_tie(self) -> None:
        history = {move: MoveStats() for move in Move}
        strategy = BestWinRateStrategy(random.Random(0))

        selected = {strategy.choose(history) for _ in range(100)}

        self.assertEqual(selected, set(Move))


if __name__ == "__main__":
    unittest.main()

