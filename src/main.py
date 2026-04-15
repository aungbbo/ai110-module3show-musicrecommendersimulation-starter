"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Core evaluation profiles.
    profiles = {
        "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9},
        "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.35, "likes_acoustic": True},
        "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.95},
        # Adversarial / edge-case profiles to stress test behavior.
        "Conflicting Preferences": {"genre": "ambient", "mood": "sad", "energy": 0.9},
        "Unknown Genre Tag": {"genre": "k-pop", "mood": "focused", "energy": 0.5},
        "Very Low Energy Intense": {"genre": "metal", "mood": "intense", "energy": 0.1},
    }

    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n=== {profile_name} ===")
        print(f"Preferences: {user_prefs}\n")
        print("Top recommendations:\n")

        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
