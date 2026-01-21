---
name: x-data-signals
description: Expert knowledge of X's social graph signals, including SimClusters community mapping, TweepCred reputation scoring, and RealGraph interaction modeling.
version: 1.0.0
license: MIT
---

# X Data Signals

Use this skill when you need to understand how the algorithm identifies user interests, calculates account authority, or predicts specific user-to-user affinities. This skill covers the underlying data "DNA" that feeds into both the Candidate Sourcing and Ranking stages.

## Context

The X recommendation engine doesn't just look at tweets; it looks at the relationship between entities. **SimClusters** provide a way to group users and content into ~145,000 community-based interest groups. **TweepCred** calculates a PageRank-style reputation for every user, and **RealGraph** models the likelihood of interaction between any two specific users. These signals are the primary inputs for personalized discovery.

For deep dives into specific signal logic, see:
- [SimClusters & Communities](./references/simclusters.md)
- [TweepCred (Reputation)](./references/tweepcred.md)
- [RealGraph (Interaction Affinity)](./references/realgraph.md)

## What it does

* **Decodes Community Mapping:** Explains how users are assigned to interest clusters and how tweets are "anchored" to those clusters.
* **Analyzes Account Authority:** Details the factors that increase or decrease a user's global reputation score (TweepCred).
* **Maps Personalized Affinity:** Explains how the system predicts the strength of a relationship between two users to prioritize "In-Network" content.
* **Troubleshoots "Echo Chambers":** Provides insight into how SimCluster isolation can limit content distribution to specific silos.

## Guidelines

* **SimCluster Anchoring:** A tweet is anchored to a cluster if a high-reputation member of that cluster likes it. This is how the "Out-of-Network" (Phoenix) source finds content for you—by looking at what your clusters are currently engaging with.
* **TweepCred as a Gatekeeper:** In the `Thunder` (In-Network) source, users with low TweepCred may have their tweets omitted from their followers' feeds during high-traffic periods to save compute. 
* **RealGraph Edge Weights:** Interaction isn't binary. RealGraph assigns a weight to every "edge" (connection) between users. A direct DM or a reciprocal "Follow" creates a much stronger weight than a single "Like."
* **Embedding Logic:** Content and Users are mapped into a shared 145k-dimensional space. The closer a tweet's embedding is to a user's embedding, the higher the "Relevance Score" in the early stages of the pipeline.
* **Signal Freshness:** TweepCred is typically calculated in batches (daily/weekly), whereas RealGraph and SimCluster anchors are updated in near real-time via Kafka streams to capture trending community shifts.

## Example Trigger Prompts

* "Explain the SimClusters algorithm and how it groups users."
* "How does TweepCred influence a user's initial reach in the Thunder service?"
* "What data signals are used to calculate the 'RealGraph' score between two users?"
* "How do SimCluster 'Anchors' help in out-of-network content discovery?"
* "Why would an account have a high follower count but low TweepCred?"
