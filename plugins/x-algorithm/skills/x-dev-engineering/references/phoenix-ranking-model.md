# Reference: Phoenix Ranking Model
The Phoenix ranking layer scores hydrated candidates with learned engagement models rather than hand-coded relevance rules.

- **Transformer context:** The user query and recent behavior provide context for candidate scoring.
- **Multi-action heads:** Separate heads estimate Like, Reply, Repost, Quote, VideoView, negative feedback, and dwell-time outcomes.
- **Point-wise scoring:** Each candidate is scored independently against the user context, so batch members do not attend to each other.
- **Learned interactions:** Dense feature and embedding interactions replace manual feature crosses wherever possible.
- Keep candidate features available before scoring, but avoid adding heuristic boosts in the pipeline.
- Preserve candidate isolation when batching scorer calls.
- Treat downstream diversity and safety stages as separate from raw relevance prediction.
