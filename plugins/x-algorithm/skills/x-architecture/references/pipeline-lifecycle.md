# Reference: Pipeline Lifecycle

The X Recommendation Pipeline follows a strictly defined lifecycle. Understanding these stages is critical for modifying the feed behavior.

### 1. Candidate Sourcing
Retrieval of potential tweets from multiple indices.
- **In-Network:** Content from the user's following graph (Thunder).
- **Out-of-Network:** Discovery content based on embeddings (Phoenix/CR-Mixer).
- **Search Index:** Real-time keyword matches (Earlybird).

### 2. Hydration
The sourcing stage returns only Tweet IDs. Hydrators are responsible for "filling in" the data:
- **Tweet Hydrator:** Fetches text, media, and timestamps.
- **User Hydrator:** Fetches author reputation (TweepCred) and relationship status.

### 3. Scoring
The **Heavy Ranker** (MaskNet/Transformer) assigns a score.
- **Inputs:** User Features + Tweet Features + Interaction History.
- **Output:** A multi-task probability score (e.g., `P(Like) * W_like + P(Retweet) * W_rt`).

### 4. Filtering
Sequential removal of candidates.
- **Safety:** VisibilityLib prunes content based on blocks, mutes, and safety labels.
- **Deduplication:** Removing multiple versions of the same media or retweets.

### 5. Mixing & Selection
The final stage where the candidate pool is pruned to the top ~100 items.
- **Diversity Rules:** Ensuring a single author doesn't dominate the feed.
- **Content Ratios:** Maintaining a balance between In-Network and Out-of-Network content.
