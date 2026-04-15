# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeMixer 1.0**

---

## 2. Intended Use  

This system suggests top songs from a small CSV catalog.
It is made for classroom learning and experimentation.
It assumes users can describe taste with genre, mood, and energy.

### Non-Intended Use
It should not be used for real music product decisions.
It should not be used to profile people or make high-stakes decisions.
It is not designed for fairness, personalization at scale, or commercial use.

---

## 3. How the Model Works  

The model compares each song to a user profile.
It uses genre, mood, energy, and optional acoustic preference.
Songs get points for matching genre and mood.
Songs also get points when energy is close to the target energy.
For an experiment, I reduced genre weight and increased energy weight.
Then songs are sorted by score and the top `k` are returned.

---

## 4. Data  

The dataset is `data/songs.csv` with 18 songs.
I expanded it from the starter 10 songs by adding 8 songs.
Features include genre, mood, energy, tempo, valence, danceability, and acousticness.
Genres include pop, lofi, rock, ambient, jazz, synthwave, classical, hip hop, metal, reggae, country, edm, blues, and latin.
The data is still small and misses lyrics, language, culture, and listening context.

---

## 5. Strengths  

It works well for clear profiles like High-Energy Pop and Chill Lofi.
The top songs usually match the intended vibe.
The explanation reasons make rankings easy to understand.
It is simple to debug because each score component is visible.

---

## 6. Limitations and Bias 

The model can create a filter bubble around one feature.
In my weight-shift test, energy became too strong and dominated rankings.
Some profiles then got “closest energy” songs even without genre/mood alignment.
The small catalog also causes repetition in top results.
Exact text matching for genre/mood can miss near-equivalent labels like `k-pop` vs `pop`.

---

## 7. Evaluation  

I tested with these profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, Conflicting Preferences, Unknown Genre Tag, and Very Low Energy Intense.
I ran `python -m src.main` and reviewed top 5 recommendations and reason strings.
I compared outputs before and after the weight-shift experiment.
The biggest surprise was how quickly rankings changed when energy weight increased.
This showed the model is very sensitive to weight choices.

---

## 8. Future Work  

Add soft matching between related genres and moods instead of exact text only.
Add diversity rules so top results are not too repetitive.
Add more user preferences (tempo range, valence target, danceability target).
Use a larger and more balanced dataset.

---

## 9. Personal Reflection  

My biggest learning moment was seeing how one weight change can reshape all rankings.
AI tools helped me draft scoring logic, prompts, and documentation faster.
I still had to double-check generated code and outputs, especially around imports and score math.
What surprised me is that a simple weighted formula can still feel like a real recommender when the profile matches the data.
If I extend this project, I want to add better diversity and better handling of mixed tastes.
