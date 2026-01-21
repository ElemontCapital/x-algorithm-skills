# X Algorithm Skills 𝕩

A suite of high-performance agent skills derived from a thorough analysis of the open-source **xAI X Algorithm**. These skills empower an agent to understand, optimize for, and build upon the X recommendation engine.

**Upstream reference:** - https://github.com/xai-org/x-algorithm

---
## 📁 Project Structure
```text
x-algorithm-skills/
├── README.md
├── AGENTS.md
├── .claude-plugin/
│   └── marketplace.json
└── plugins/
    └── x-algorithm/
        ├── .claude-plugin/
        │   └── plugin.json
        └── skills/
            ├── x-post-optimizer.md    # Content strategy & reach
            ├── x-architecture.md      # System design & HomeMixer
            ├── x-ranking-engine.md    # HeavyRanker & ML models
            ├── x-dev-engineering.md   # Rust/Scala/Thrift implementation
            ├── x-data-signals.md      # SimClusters & Reputation
            └── x-safety-filtering.md  # VisibilityLib & Shadowbans
```
---

## 🚀 Installation

### Claude Code

Add the marketplace:

```bash
/plugin marketplace add xai-org/x-algorithm-skills
```
Install the skills:
```bash
/plugin install x-algorithm
```
### Any Agent
For other agents, you can extract and add the skills manually:
```bash
bunx add-skill xai-org/x-algorithm-skills
```
This will install the skills individually, so you will need to manually upgrade them when updates are available.
See **AGENTS.md** for manual installation instructions.

## ⚡ The Skill Suite

| Skill  | Best For | Description |
|--------|--------|-------------|
| **x-post-optimizer** | Content Creators | Maximizes reach by optimizing for **HeavyRanker** weights. |
| **x-architecture** | Architects | Maps the **HomeMixer** pipeline and candidate generation. |
| **x-ranking-engine** | ML Engineers | Deep dive into **HeavyRanker (MaskNet)** and scoring logic. |
| **x-dev-engineering** | Software Engineers | Coding assistant for Rust/Scala and Thrift definitions. |
| **x-data-signals** | Data Scientists | Logic for **SimClusters**, **TweepCred**, and Graph Analytics. |
| **x-safety-filtering** | Trust & Safety | Managing **VisibilityLib**, safety labels, and shadowbans. |

---

## 📖 Skill Definitions & Capabilities

### 1) `x-post-optimizer`

**Context**  
Contains the weighting parameters from `ScoringService` and filtering logic from `VisibilityLib`.

**Typical Triggers**  
- Draft a post…  
- Why is my reach low?  
- Check for shadowban.

**What it does**  
- Rewrites or scores posts against known ranking features.  
- Flags likely visibility or safety issues before publishing.  
- Suggests structural changes (hook, media, timing, engagement bait).

---

### 2) `x-architecture`

**Context**  
Orchestration logic within the `HomeMixer` and `ProductMixer` frameworks.

**Typical Triggers**  
- How does the feed work?  
- Explain candidate generation.  
- What is Phoenix?

**What it does**  
- Explains the end-to-end feed pipeline.  
- Breaks down each stage: sourcing, scoring, filtering, mixing.  
- Helps reason about where ranking changes have the biggest impact.

---

### 3) `x-ranking-engine`

**Context**  
ML model implementation in the `heavy-ranker` module.

**Typical Triggers**  
- How is scoring calculated?
- Explain the Transformer model.  
- What is MaskNet?

**What it does**  
- Provides technical details on the neural network architecture.
- Explains candidate isolation.
- Breaks down multi-task probability scoring.

---

### 4) `x-dev-engineering`

**Context**  
Contains patterns for Rust/Scala interop, Thrift schemas, and the `product-mixer` framework.

**Typical Triggers**  
- Refactor this mixer pipeline.
- Create a new Candidate Source.  
- "Generate a Thrift schema.

**What it does**  
- Assists with navigating the `ProductMixer` architecture.  
- Generates and reviews Thrift and service boundaries.  
- Helps debug cross-language pipeline issues.
- Assists in writing high-performance async Rust.

---

### 5) `x-data-signals`

**Context**  
Contains logic for `SimClusters` (Communities), `RealGraph` (User Interactions), and `TweepCred` (Reputation).

**Typical Triggers**  
- Explain user clustering.  
- How is reputation calculated?
- What is TweepCred? 
- Analyze graph embeddings.

**What it does**  
- Explains how users and content are embedded into clusters.  
- Breaks down interaction graphs and authority signals.  
- Explains how `PageRank-style reputation scores influence content priority.

---

### 6) `x-safety-filtering`

**Context**  
Compliance and health logic in `visibility-lib`.

**Typical Triggers**  
- Am I shadowbanned?
- Check for toxicity filters.
- What are safety labels?

**What it does**  
- Identifies triggers for `DoNotAmplify` or `SearchBlacklist` labels
- Explains the "Linear Decay" applied to reported content.

---

## 📜 License & Attribution

This project builds on concepts and structures described in the open-source **xAI X Algorithm** repository:  
https://github.com/xai-org/x-algorithm  

- **Upstream code** is licensed under **Apache License 2.0**. See [LICENSE-APACHE](LICENSE-APACHE) for details.  
- **All original code, documentation, and skill definitions in this repository** are licensed under the **MIT License**. See [LICENSE-MIT](LICENSE-MIT) for details.

---
