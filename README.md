# X Algorithm Skills 𝕩

A suite of high-performance agent skills derived from the open-source **xAI X Algorithm**. These skills empower an agent to understand, optimize for, and build upon the X recommendation engine.

**Upstream reference:**  
- https://github.com/xai-org/x-algorithm

---

## 🚀 Installation

### Claude Code

Add the marketplace:

```bash
/plugin marketplace add xai-org/x-algorithm-skills
```
Install the skills:
```bash
/plugin install x-post-optimizer
/plugin install x-algo-blueprint
/plugin install x-dev-pro
/plugin install x-data-signals
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
| **x-post-optimizer** | Content Creators | Writes content optimized for "Heavy Ranker" weights while passing safety and visibility filters. |
| **x-algo-blueprint** | Researchers | Maps the full pipeline: **Candidate Sources → Scoring → Filtering → Mixing**. |
| **x-dev-pro** | Software Engineers | Coding assistant for the Rust/Scala product-mixer and Thrift definitions. |
| **x-data-signals** | Data Scientists | Deep dive into SimClusters, User Reputation (TweepCred), and Graph Analytics. |

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

### 2) `x-algo-blueprint`

**Context**  
Contains the system architecture diagrams and data flow for `HomeMixer`.

**Typical Triggers**  
- How does the feed work?  
- Explain candidate generation.  
- What is Phoenix?

**What it does**  
- Explains the end-to-end feed pipeline.  
- Breaks down each stage: sourcing, scoring, filtering, mixing.  
- Helps reason about where ranking changes have the biggest impact.

---

### 3) `x-dev-pro`

**Context**  
Contains patterns for Rust/Scala interop, Thrift schemas, and the product-mixer framework.

**Typical Triggers**  
- Refactor this pipeline.  
- Create a new Candidate Source.  
- Fix this Rust error.

**What it does**  
- Assists with extending the product-mixer architecture.  
- Generates and reviews Thrift and service boundaries.  
- Helps debug cross-language pipeline issues.

---

### 4) `x-data-signals`

**Context**  
Contains logic for SimClusters (Communities), RealGraph (User Interactions), and TweepCred (Reputation).

**Typical Triggers**  
- Explain user clustering.  
- How is reputation calculated?  
- Analyze graph embeddings.

**What it does**  
- Explains how users and content are embedded into clusters.  
- Breaks down interaction graphs and authority signals.  
- Helps interpret ranking and trust features from a data perspective.

---

## 🎯 Who This Is For

- Creators who want to optimize reach and visibility on X.
- Researchers who want a clear, inspectable model of a large-scale recommender.
- Engineers who want to extend or reason about a production-grade ranking pipeline.
- Data scientists who want to understand how graphs, clusters, and reputation signals interact.

---

## 📜 License & Attribution

This project builds on concepts and structures described in the open-source **xAI X Algorithm** repository:  
https://github.com/xai-org/x-algorithm  

- **Upstream code** is licensed under **Apache License 2.0**. See [LICENSE-APACHE](LICENSE-APACHE) for details.  
- **All original code, documentation, and skill definitions in this repository** are licensed under the **MIT License**. See [LICENSE-MIT](LICENSE-MIT) for details.

---
