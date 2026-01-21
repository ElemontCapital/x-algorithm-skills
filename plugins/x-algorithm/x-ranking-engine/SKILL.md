---
name: x-ranking-engine
description: Expert knowledge of the X Heavy Ranker (MaskNet/Transformer), multi-task engagement prediction, and the mathematical scoring formulas used to rank the For You timeline.
version: 1.0.0
license: MIT
---

# X Ranking Engine

Use this skill when you need to understand or modify the machine learning logic that determines which tweets appear at the top of a user's feed. This skill covers model architecture, feature engineering, and the weights assigned to different user interactions.

## Context

The **Heavy Ranker** is the "brain" of X. While the architecture (HomeMixer) fetches candidates, the Ranking Engine scores them. It utilizes a Multi-Task Learning (MTL) approach to predict the probability of various user actions simultaneously. The model has transitioned from legacy Gradient Boosted Decision Trees (GBDT) to deep neural networks (MaskNet) and Grok-influenced Transformers.

For deep technical specifications, refer to:
- [Model Architecture](./references/model-architecture.md)
- [Scoring Parameters](./references/scoring-parameters.md)

## What it does

* **Explains Multi-Task Learning:** Details how the model predicts multiple binary outcomes (Like, Reply, RT) in a single pass.
* **Analyzes Feature Importance:** Identifies the impact of User-Tweet interaction features vs. static Author features (e.g., TweepCred).
* **Calculates Ranking Scores:** Provides the mathematical logic for how individual probability predictions are combined into a final rank.
* **Rationalizes Candidate Isolation:** Explains the design constraint where tweets are scored independently of each other to ensure high-throughput serving via the Navi engine.

## Guidelines

* **The Scoring Equation:** The final score $S$ for a tweet is generally a weighted sum of predicted probabilities $P$:
  $$S = \sum_{i=1}^{n} w_i \cdot P_i$$
  where $w_i$ represents the weight of action $i$ (e.g., Like, Reply, Retweet).
* **Feature Categories:**
    * **User Features:** Logged-in user's interests, embedding ID, and recent engagement history.
    * **Tweet Features:** Content embeddings, media type, and age (recency).
    * **Author Features:** Reputation (TweepCred) and "Social Proof" (current engagement velocity).
* **Navi Serving:** Models are served via **Navi**. When adding a new feature to the model, it must be hydrated in the `HomeMixer` and passed through the Thrift interface to the ranker.
* **Positive vs. Negative Signals:** Ensure you account for negative weights. Signals like "Show less often" or "Block/Mute" have massive negative multipliers that can instantly tank a candidate's score.
* **Recency Bias:** The algorithm applies a time-decay function. A high-scoring old tweet will eventually be outranked by a lower-scoring fresh tweet to maintain timeline "newness."

## Example Trigger Prompts

* "How does the Heavy Ranker calculate the final score for a tweet?"
* "Explain the MaskNet architecture used in the Phoenix model."
* "What are the specific weights for a Like vs. a Retweet in the current scoring service?"
* "How does the algorithm handle negative feedback signals?"
* "Where in the code are the model features defined for the Navi engine?"
