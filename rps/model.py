"""Rules and value objects for rock-paper-scissors."""

from __future__ import annotations

from enum import Enum


class Move(str, Enum):
    ROCK = "rock"
    SCISSORS = "scissors"
    PAPER = "paper"


class Outcome(Enum):
    WIN = 1
    DRAW = 0
    LOSS = -1

    @property
    def opposite(self) -> "Outcome":
        return Outcome(-self.value)


_BEATS = {
    Move.ROCK: Move.SCISSORS,
    Move.SCISSORS: Move.PAPER,
    Move.PAPER: Move.ROCK,
}


def judge(first: Move, second: Move) -> Outcome:
    """Return the outcome from the first player's point of view."""
    if first == second:
        return Outcome.DRAW
    if _BEATS[first] == second:
        return Outcome.WIN
    return Outcome.LOSS

