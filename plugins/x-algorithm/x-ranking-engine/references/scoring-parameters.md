# Reference: Scoring Parameters & Weights

The "Score" of a tweet determines its position. This is the logic used by the `ScoringService`.

### Current Interaction Weights (Approximate)
The weights are frequently tuned via A/B testing, but the relative hierarchy is generally:

| Interaction Type | Relative Weight | Strategic Notes |
| :--- | :--- | :--- |
| **Author Reply** | 75.0x | Highest value; rewards "conversation" creators. |
| **Retweet** | 20.0x | High value for virality and distribution. |
| **Reply** | 13.5x | Rewards engagement; lower than author replies. |
| **Like** | 1.0x | The baseline "unit" of engagement. |
| **Negative Signal** | -50.0x | "Show less often" or "Mute" is highly punitive. |



### The Weighted Formula Logic
The final rank is calculated by multiplying the probability of an action by its assigned weight:
$$TotalScore = (P_{like} \cdot W_{like}) + (P_{reply} \cdot W_{reply}) + (P_{rt} \cdot W_{rt}) ...$$

### Safety & Health Adjustments
Before the final sort, "Integrity" multipliers are applied:
- **Toxicity Filter:** If $P(\text{Toxicity}) > \text{threshold}$, the score is multiplied by 0.1 (90% reduction).
- **Misinformation:** If flagged by community notes or internal labels, a heavy decay is applied.
- **Blue Checkmark:** Verified users may receive a multiplier in specific sourcing stages, though this is often a retrieval boost rather than a pure ranking multiplier.
