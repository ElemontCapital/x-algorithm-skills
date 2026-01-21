# Reference: SimClusters & Communities

SimClusters is a collaborative filtering framework used to move beyond simple "Topic" tags and into "Community" interest groups.



### How it Works
1.  **Matrix Factorization:** The system analyzes the User-to-User follow graph.
2.  **Cluster Identification:** It identifies ~145,000 distinct clusters (e.g., "NY Tech," "K-Pop Fans," "Rust Developers").
3.  **User Membership:** Each user is assigned a "Score" for various clusters based on who they follow and interact with.
4.  **Tweet Anchoring:** If multiple members of "Cluster A" interact with a tweet, that tweet is "anchored" to Cluster A.

### Significance in Ranking
In the **Heavy Ranker**, a feature known as `sim_cluster_score` is computed by calculating the dot product between the User's cluster vector and the Tweet's anchor vector. A high match is one of the strongest predictors of a "Like" or "Retweet."
