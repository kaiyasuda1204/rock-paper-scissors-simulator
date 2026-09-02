"""Player state kept independently from move-selection strategies."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field

from .model import Move, Outcome
from .strategies import MoveStats, Strategy


@dataclass
class Player:
    name: str
    strategy: Strategy
    _history: dict[Move, MoveStats] = field(
        default_factory=lambda: {move: MoveStats() for move in Move},
        init=False,
        repr=False,
    )

    @property
    def history(self) -> Mapping[Move, MoveStats]:
        return self._history

    def choose_move(self) -> Move:
        return self.strategy.choose(self.history)

    def record(self, move: Move, outcome: Outcome) -> None:
        self._history[move].record(outcome)

