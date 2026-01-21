# Reference: TweepCred (Reputation)

TweepCred is the internal authority score that dictates an account's "trustworthiness" in the eyes of the algorithm.



### The PageRank Logic
TweepCred is not based on the *number* of followers, but the *quality* of those followers.
- If a user with a TweepCred of 90 follows you, your score increases significantly.
- If 1,000 users with a TweepCred of 10 follow you, your score barely moves.

### Factors that Lower TweepCred
- **Negative Feedback:** High ratios of "Report Spam" or "Block" relative to total impressions.
- **Bot-like Behavior:** Rapid following/unfollowing or high-frequency automated posting.
- **Safety Labels:** Being flagged by `VisibilityLib` for toxicity or misinformation triggers a temporary reputation penalty.

### Usage in the Code
In `thunder/`, the candidate retrieval logic often uses a `min_tweepcred` threshold during peak load to prioritize content from authoritative sources, effectively "shadow-throttling" low-reputation accounts.
