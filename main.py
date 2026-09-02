"""Run a match between Nobita and Suneo."""

from __future__ import annotations

import argparse
import random

from rps import BestWinRateStrategy, Player, UniformRandomStrategy, play_match


def positive_integer(value: str) -> int:
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("rounds must be a positive integer")
    return number


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("rounds", type=positive_integer, help="number of rounds")
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="optional random seed for reproducible output",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rng = random.Random(args.seed)
    nobita = Player("N", UniformRandomStrategy(rng))
    suneo = Player("S", BestWinRateStrategy(rng))
    result = play_match(nobita, suneo, args.rounds)

    print(f"{nobita.name}: {result.first_win_rate:.2%}")
    print(f"{suneo.name}: {result.second_win_rate:.2%}")


if __name__ == "__main__":
    main()

