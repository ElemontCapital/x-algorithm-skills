# Reference: RealGraph (User Interaction Affinity)

RealGraph models the directed relationship between two users to predict the probability of a future interaction.



### The Edge Scoring Model
RealGraph looks at historical interactions between User A and User B:
- **Reciprocal Follow:** Strongest signal.
- **Direct Messages:** Very strong signal.
- **Replies/Mentions:** Strong signal.
- **Likes/Retweets:** Moderate signal.
- **Profile Views:** Weak but positive signal.

### Implementation
RealGraph features are typically stored as a set of weights in a directed graph. When User A opens their feed, the system pulls the RealGraph weights for everyone they follow. These weights are then passed as "Personalization Features" to the **Heavy Ranker** to ensure that content from "Close Friends" (high RealGraph weight) is ranked above content from "Acquaintances" (low RealGraph weight).
