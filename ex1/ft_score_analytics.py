#!/usr/bin/env python3
"""
This module reads numeric command-line arguments representing player scores.
It outputs descriptive statistics and ignores invalid inputs.

Authorized modules: sys
"""
import sys


def ft_score_analytics() -> None:
    """
    Process player scores from command-line arguments.

    Validates input, calculates statistics including:
    - Total players
    - Total and average score
    - High and low scores
    - Score range
    """
    print("=== Player Score Analytics ===")
    scores: list[int] = []
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"This doesn't look like a number: {arg}")
    if not scores:
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
            )
        return
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores):.1f}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    ft_score_analytics()
