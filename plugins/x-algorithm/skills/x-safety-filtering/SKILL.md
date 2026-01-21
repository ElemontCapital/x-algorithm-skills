---
name: x-safety-filtering
description: Expert knowledge of X's VisibilityLib, covering safety labels, shadowban logic, NSFW filtering, and content health suppression mechanisms.
version: 1.0.0
license: MIT
---

# X Safety & Filtering

Use this skill when analyzing why content is not appearing, checking for "shadowban" conditions, or understanding the safety compliance layer. This skill covers the `VisibilityLib` logic that runs *after* candidate sourcing but *before* final ranking to ensure platform health.

## Context

Filtering is the "Gatekeeper" of the timeline. Even if a tweet has a high ML score from the Heavy Ranker, `VisibilityLib` can drop it entirely or apply a "Do Not Amplify" label that restricts it to the author's profile. This layer enforces legal compliance, user blocks, mutes, and platform safety rules (e.g., NSFW or Toxicity).

For specific definitions of labels and logic, see:
- [Safety Labels & Shadowbans](./references/safety-labels.md)
- [Filtering Logic & Architecture](./references/filtering-logic.md)
- [Toxicity & Reputation Decay](./references/toxicity-decay.md)

## What it does

* **Decodes "Shadowbans":** Explains the specific internal labels (like `SearchBlacklist`) that cause users to perceive they are shadowbanned.
* **Enforces User Preferences:** Handles the logic for Mutes, Blocks, and "Show less often" signals.
* **Manages Content Health:** Identifies toxic content or misinformation and applies downstream penalties (De-amplification).
* **NSFW Handling:** Segments content into "Adult" or "Graphic" categories and ensures it respects the viewer's sensitivity settings.

## Guidelines

* **The "Do Not Amplify" (DNA) Label:** This is the most common form of "soft" filtering. DNA-labeled tweets are not removed, but they are disqualified from the "For You" (Out-of-Network) timeline and Search results.
* **Visibility vs. Ranking:** Visibility filters often run *twice*.
    1.  **Pre-Scoring:** To remove hard-blocked or legally prohibited content so resources aren't wasted scoring it.
    2.  **Post-Scoring:** To apply final safety checks (like author diversity or adjacency rules) before delivery.
* **Toxicity Thresholds:** The system calculates a toxicity score. If a user enters a "Reply Guy" mode with consistently high toxicity, their account enters a `p_toxicity` state that limits the reach of *all* their future replies.
* **Linear Decay:** Negative reputation signals (reports/blocks) don't last forever. They follow a linear decay model, meaning an account can "heal" its reputation over time by stopping the negative behavior.
* **Frequency Filter**: Halves scores for posts <1 hour apart, similar to muted/blocked penalties.

## Example Trigger Prompts

* "Why is my account not appearing in Search?"
* "Explain the logic behind the 'Do Not Amplify' label."
* "How does VisibilityLib handle NSFW content?"
* "What triggers a toxicity flag on a reply?"
* "Am I shadowbanned based on these engagement signals?"
