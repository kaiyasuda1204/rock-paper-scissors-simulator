"""Interchangeable move-selection strategies."""

from __future__ import annotations

import random
from abc import ABC, abstractmethod
from collections.abc import Mapping
from dataclasses import dataclass

from .model import Move, Outcome


@dataclass
class MoveStats:
    plays: int = 0
    wins: int = 0

    @property
    def win_rate(self) -> float:
        # An unused move has no wins yet, so it starts at 0%.
        return self.wins / self.plays if self.plays else 0.0

    def record(self, outcome: Outcome) -> None:
        self.plays += 1
        if outcome is Outcome.WIN:
            self.wins += 1


class Strategy(ABC):
    @abstractmethod
    def choose(self, history: Mapping[Move, MoveStats]) -> Move:
        """Choose one move using the player's history."""


class UniformRandomStrategy(Strategy):
    def __init__(self, rng: random.Random | None = None) -> None:
        self._rng = rng or random.Random()
        self._moves = tuple(Move)

    def choose(self, history: Mapping[Move, MoveStats]) -> Move:
        del history
        return self._rng.choice(self._moves)


class BestWinRateStrategy(Strategy):
    def __init__(self, rng: random.Random | None = None) -> None:
        self._rng = rng or random.Random()

    def choose(self, history: Mapping[Move, MoveStats]) -> Move:
        best_rate = max(stats.win_rate for stats in history.values())
        best_moves = [
            move for move, stats in history.items() if stats.win_rate == best_rate
        ]
        return self._rng.choice(best_moves)

