# Reference: Visibility Filtering
`VisibilityLib` is the Rust safety gate that decides whether a viewer may see a candidate before it reaches ranking or final delivery.

- Author and viewer relationship state, including blocks, mutes, and suspensions.
- Safety labels from text, media, abuse, toxicity, and legal classifiers.
- Viewer settings, country rules, and request-specific safety level.
- **Drop:** Remove content completely when policy or user graph rules require it.
- **Interstitial:** Keep content available only behind a warning.
- **Ranking clue:** Pass safety metadata to ranking so unsafe or low-quality content can be down-ranked without hard removal.

Run safety filtering before final candidate selection, and keep policy decisions outside scorer-specific relevance logic.
