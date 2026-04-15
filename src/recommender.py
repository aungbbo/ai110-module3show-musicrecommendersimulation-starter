from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from CSV into typed dictionaries."""
    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": int(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )

    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Compute a weighted song score and explanation reasons."""
    score = 0.0
    reasons: List[str] = []

    # Support both starter keys (genre/mood/energy) and profile-style keys.
    favorite_genre = user_prefs.get("favorite_genre", user_prefs.get("genre"))
    favorite_mood = user_prefs.get("favorite_mood", user_prefs.get("mood"))
    target_energy = float(user_prefs.get("target_energy", user_prefs.get("energy", 0.5)))
    likes_acoustic = user_prefs.get("likes_acoustic")

    if favorite_genre and song["genre"].lower() == str(favorite_genre).lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    if favorite_mood and song["mood"].lower() == str(favorite_mood).lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    # Reward closeness to target energy (max 1.0 points).
    energy_similarity = max(0.0, 1.0 - abs(float(song["energy"]) - target_energy))
    energy_points = energy_similarity
    score += energy_points
    reasons.append(f"energy closeness (+{energy_points:.2f})")

    # Optional acoustic preference component.
    if likes_acoustic is not None:
        if likes_acoustic:
            acoustic_points = 0.5 * float(song.get("acousticness", 0.0))
            score += acoustic_points
            reasons.append(f"acoustic preference (+{acoustic_points:.2f})")
        else:
            non_acoustic_points = 0.5 * (1.0 - float(song.get("acousticness", 0.0)))
            score += non_acoustic_points
            reasons.append(f"low-acoustic preference (+{non_acoustic_points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank songs by score and return the top-k recommendations."""
    scored_songs: List[Tuple[Dict, float, str]] = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda rec: rec[1], reverse=True)
    return scored_songs[:k]
