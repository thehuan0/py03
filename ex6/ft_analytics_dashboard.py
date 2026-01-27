#!/usr/bin/env python3
"""
Exercise 6: Data Alchemist
Demonstrates mastery of Python comprehensions.
"""


def ft_analytics_dashboard() -> None:
    """
    Demonstrates list, dictionary, and set comprehensions.
    """
    print("=== Data Alchemist Dashboard ===")

    scores = [1500, 2300, 1800, 2100, 1950]
    players = ["alice", "bob", "charlie", "diana", "evan"]
    achievements = ["first_kill", "level_10", "boss_slayer", "first_kill", "treasure_hunter"]

    print("\n=== List Comprehensions ===")

    high_scores = [score for score in scores if score > 2000]
    print(f"High scores (>2000): {high_scores}")

    boosted_scores = [score + 100 for score in scores]
    print(f"Boosted scores (+100): {boosted_scores}")

    print("\n=== Dictionary Comprehensions ===")

    player_scores = {players[i]: scores[i] for i in range(len(players))}
    print(f"Player scores: {player_scores}")

    achievement_counts = {ach: achievements.count(ach) for ach in achievements}
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehensions ===")

    unique_achievements = {ach for ach in achievements}
    print(f"Unique achievements: {unique_achievements}")

    score_ranges = {"High" if score > 2000 else "Medium" if score > 1800 else "Low" for score in scores}
    print(f"Score ranges present: {score_ranges}")

    print("\n--- Analytics with Comprehensions ---")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores):.1f}")
    print(f"Highest score: {max(scores)}")
    print(f"Lowest score: {min(scores)}")
    print(f"Sorted scores: {sorted(scores)}")


if __name__ == "__main__":
    ft_analytics_dashboard()