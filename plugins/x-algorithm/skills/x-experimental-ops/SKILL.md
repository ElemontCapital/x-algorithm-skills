---
name: x-experimental-ops
description: Use this skill when reasoning about how the algorithm is tuned, why different users see different behaviors, or how "Success" is defined by X's engineering team.
version: 1.0.0
license: MIT
---

# X Experimental Ops

Knowledge of X's A/B testing infrastructure (DuckDuckGoose) and the metrics used to measure algorithmic success.

## Context
The algorithm is never "finished." It is a living system managed by **DuckDuckGoose (DDG)**, X's internal experimentation platform. Every change to a weight or a filter is first tested on a small percentage of the user base.

- [DuckDuckGoose (A/B Testing)](./references/ab-testing-framework.md)
- [Metrics & Alignment](./references/metrics-alignment.md)

## What it does
* **Explains Bucketing:** How users are assigned to "Control" and "Treatment" groups.
* **Decodes Success Metrics:** Breaks down the "North Star" metrics like Unregretted User Minutes.
* **Analyzes Feature Flags:** Identifies how logic can be toggled on/off for specific cohorts without a full code deploy.
