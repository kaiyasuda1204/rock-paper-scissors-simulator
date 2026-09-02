"""Match simulation independent of command-line presentation."""

from __future__ import annotations

from dataclasses import dataclass

from .model import Outcome, judge
from .player import Player


@dataclass(frozen=True)
class MatchResult:
    rounds: int
    first_wins: int
    second_wins: int
    draws: int

    @property
    def first_win_rate(self) -> float:
        return self.first_wins / self.rounds

    @property
    def second_win_rate(self) -> float:
        return self.second_wins / self.rounds


def play_match(first: Player, second: Player, rounds: int) -> MatchResult:
    if rounds <= 0:
        raise ValueError("rounds must be a positive integer")

    first_wins = 0
    second_wins = 0
    draws = 0

    for _ in range(rounds):
        first_move = first.choose_move()
        second_move = second.choose_move()
        outcome = judge(first_move, second_move)

        first.record(first_move, outcome)
        second.record(second_move, outcome.opposite)

        if outcome is Outcome.WIN:
            first_wins += 1
        elif outcome is Outcome.LOSS:
            second_wins += 1
        else:
            draws += 1

    return MatchResult(rounds, first_wins, second_wins, draws)

