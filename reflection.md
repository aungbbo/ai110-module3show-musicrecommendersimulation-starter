## Profile comparisons (what changed and why)

- **High-Energy Pop vs Chill Lofi**
  - High-Energy Pop surfaces songs with high energy near the target (and pop/happy matches when available).
  - Chill Lofi shifts toward lower-energy songs and (when `likes_acoustic` is enabled) favors more acoustic tracks; that makes sense because acousticness and energy jointly define a “calm” vibe in this dataset.

- **Deep Intense Rock vs Chill Lofi**
  - Deep Intense Rock pushes “Storm Runner” and other high-energy tracks upward because energy closeness dominates and the mood “intense” appears in multiple songs.
  - Chill Lofi prefers “Library Rain” / “Midnight Coding” because genre+mood align and energy is closer to ~0.35–0.42, which matches the calm profile.

- **Conflicting Preferences vs Unknown Genre Tag**
  - Conflicting Preferences (ambient + sad + high energy) can’t satisfy mood/genre well (no “sad” mood), so the outputs mostly become “highest energy closeness wins.”
  - Unknown Genre Tag (k-pop) also can’t match genre, but it can match mood (“focused”), so “Focus Flow” rises to the top because it earns the mood bonus plus solid energy closeness.

- **Before vs after the weight shift experiment (genre down, energy up)**
  - After the change, more lists become dominated by energy similarity (even when categorical matches are missing), increasing repetition of a few high-energy songs.
  - This makes the system feel more “numerical” (pace/intensity driven) but less faithful to genre labels for users who strongly care about genre.

