# 🤖 Agent Integration Guide

This repository complies with the **Agent Skills Standard**. While it is optimized for **Claude Code**, these skills can be manually integrated into other AI coding environments like Cursor, Windsurf, or Roo Code.

## 🛠 Manual Installation
If you are not using the Claude Code CLI, you can point your agent to the local skill definitions.

### For Cursor / Windsurf
1.  Clone this repository:
    ```bash
    git clone [https://github.com/ElemontCapital/x-algorithm-skills.git](https://github.com/ElemontCapital/x-algorithm-skills.git)
    ```
2.  In your Agent's settings (or `.cursor/rules`), add a reference to the specific skill folder you need.
    * **Strategy:** `./plugins/x-algorithm/skills/x-post-optimizer/SKILL.md`
    * **Engineering:** `./plugins/x-algorithm/skills/x-dev-engineering/SKILL.md`

## 🧠 Skill Triggers & Capabilities

| Skill Name | Trigger Phrases | Best For |
| :--- | :--- | :--- |
| **x-post-optimizer** | "Optimize this tweet", "Check for shadowban", "Increase reach" | **Creators** looking to maximize engagement weights (Replies ~75x). |
| **x-architecture** | "Explain HomeMixer", "How does sourcing work?", "Trace the pipeline" | **Architects** needing a high-level map of the Thunder/Phoenix services. |
| **x-ranking-engine** | "Explain Heavy Ranker", "What is MaskNet?", "Scoring formula" | **ML Engineers** analyzing the probability scoring logic. |
| **x-dev-engineering** | "Refactor this Rust trait", "Write a Thrift schema", "Fix async deadlock" | **Developers** writing code for the `product-mixer` or `candidate-pipeline`. |
| **x-data-signals** | "Explain SimClusters", "Calculate TweepCred", "Graph analysis" | **Data Scientists** interpreting user reputation and community clusters. |
| **x-safety-filtering** | "Check safety labels", "Explain VisibilityLib", "NSFW filtering" | **Trust & Safety** analysts auditing content suppression logic. |

## 📦 Compatibility Note
This repository uses the **Expo-style** structure ("Single Plugin, Multi-Skill").
- **Claude Code:** Automatically detects all 6 skills via `plugin.json`.
- **Other Agents:** May require you to manually open the `SKILL.md` file you want the agent to "read" into its context window.
