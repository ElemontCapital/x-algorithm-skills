# Reference: Toxicity & Reputation Decay

The system is designed to be forgiving but firm. It uses a mathematical decay model to handle reputation penalties.

### The Score Accumulator
Negative signals (Reports, Blocks, Mutes) act as "Damage" to an account's reputation score.
* **Spike Detection:** A sudden influx of blocks (e.g., during a "dogpile") triggers immediate protective limiters.

### Linear Decay (Healing)
The codebase implements a linear decay function for these negative scores.
* **Concept:** "Time heals all wounds."
* **Mechanism:** If an account stops generating negative signals, the penalty score decreases linearly over a set period (often days or weeks) until it returns to zero.
* **Strategy:** The only way to remove a "Shadowban" caused by toxicity is to go silent or post strictly positive/neutral content until the decay timer runs out.

### Reply Toxicity
Replies are scrutinized more heavily than original tweets.
* **`p_toxicity` Score:** If a reply scores high on the toxicity model, it is moved to the bottom of the conversation thread (often hidden behind a "Show more replies" click).
