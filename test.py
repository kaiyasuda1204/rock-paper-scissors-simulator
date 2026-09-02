"""Check that Nobita's three moves are uniformly distributed."""

from __future__ import annotations

import random
from collections import Counter

from rps import Move, Player, UniformRandomStrategy

TRIALS = 10_000
TOLERANCE_PERCENTAGE_POINTS = 1.0
SEED = 42


def check_uniformity() -> tuple[dict[Move, float], bool]:
    nobita = Player("N", UniformRandomStrategy(random.Random(SEED)))
    counts = Counter(nobita.choose_move() for _ in range(TRIALS))
    rates = {move: counts[move] / TRIALS * 100 for move in Move}
    expected_rate = 100 / len(Move)
    is_uniform = all(
        abs(rate - expected_rate) <= TOLERANCE_PERCENTAGE_POINTS
        for rate in rates.values()
    )
    return rates, is_uniform


def main() -> None:
    rates, is_uniform = check_uniformity()
    print(f"{rates[Move.ROCK]:.2f}% {is_uniform}")
    if not is_uniform:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

