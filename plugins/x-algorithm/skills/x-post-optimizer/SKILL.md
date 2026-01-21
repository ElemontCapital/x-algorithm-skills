---
name: x-post-optimizer
description: Strategic knowledge for maximizing content reach on X, based on algorithmic scoring weights, engagement multipliers, and anti-spam penalties.
version: 1.0.0
license: MIT
---

# X Post Optimizer

Use this skill when you need to optimize a specific post or a broader content strategy for maximum distribution. It translates the raw weights of the `HeavyRanker` into actionable "Dos and Don'ts" for creators and brands.

## Context

The X algorithm does not treat all engagement equally. By understanding the specific multipliers assigned to actions like "Author Replies" versus "External Link Clicks," this skill allows an agent to predict and improve the "Engagement Velocity" of a post. It also accounts for the "Shadow Hierarchy" of account reputation (TweepCred) which acts as a global multiplier on all content.

For specific tactical data, refer to:
- [Engagement Multipliers](./references/engagement-multipliers.md)
- [Account Reputation (TweepCred)](./references/account-reputation.md)
- [Content Formatting Guidelines](./references/content-formatting.md)

## What it does

* **Optimizes for High-Value Actions:** Prioritizes strategies that trigger high-weight signals like "Conversations" and "Dwell Time."
* **Identifies Reach Killers:** Detects "Anti-Signals" such as external links, engagement bait, or low-quality media that trigger de-amplification.
* **Advises on Engagement Velocity:** Explains how to maximize the "First Hour" impact to move from In-Network to Out-of-Network distribution.
* **Reputation Repair:** Provides logic for improving an account's `TweepCred` to unlock higher reach tiers.

## Guidelines

* **The Thread Hook:** Start with a high-dwell time hook. The algorithm evaluates the first 3 seconds of attention. If a user "scrolls past" too quickly, it triggers a negative quality signal.
* **The "Author Reply" Hack:** In the `HeavyRanker` logic, an author replying to their own thread or to a comment is weighted at **~75x**. This is the single most effective way to sustain a post's lifespan.
* **External Link Penalty:** Avoid placing links in the main post. External links can reduce reach by up to **8x**. Instead, use the "Link in Bio" or "Link in the Second Tweet" strategy.
* **Native Media Preference:** Always prefer native video (MP4) or images over external links or text-only posts. Native video receives a **~3.4x** reach boost compared to text.
* **Engagement Bait Awareness:** The algorithm's NLP models detect phrases like "Retweet this," "Follow for more," or "Link in bio." These can trigger the `EngagementBait` safety label, which caps distribution.
* **Clustering Strategy:** Reach is easier to obtain within your "SimCluster" (interest group). Straying too far into unrelated topics can lead to lower initial engagement, which the algorithm interprets as low relevance.

## Example Trigger Prompts

* "How should I structure this thread to maximize the algorithm's conversation weight?"
* "Why is my latest post getting zero reach despite high likes?"
* "Analyze this draft for potential link penalties or anti-spam triggers."
* "What is the best time to post based on engagement velocity logic?"
* "How can I improve my account's reputation score (TweepCred)?"
