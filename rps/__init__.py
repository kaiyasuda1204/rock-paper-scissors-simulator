"""Rock-paper-scissors simulation package."""

from .game import MatchResult, play_match
from .model import Move, Outcome
from .player import Player
from .strategies import BestWinRateStrategy, UniformRandomStrategy

__all__ = [
    "BestWinRateStrategy",
    "MatchResult",
    "Move",
    "Outcome",
    "Player",
    "UniformRandomStrategy",
    "play_match",
]

