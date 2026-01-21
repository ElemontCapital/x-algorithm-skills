# 𝕩 Algorithm Skills

A suite of high-performance agent skills derived from a thorough analysis of the open-source **xAI X Algorithm**. These skills empower an agent to understand, optimize for, and build upon the X recommendation engine.

**Upstream reference:** - https://github.com/xai-org/x-algorithm

---

## 🚀 Installation

### Claude Code

Add the marketplace:

```bash
/plugin marketplace add ElemontCapital/x-algorithm-skills
```
Install the skills:
```bash
/plugin install x-algorithm
```
### Any Other Agent (Cursor, Windsurf, Roo Code, etc.)
You can use the universal installer to pull specific skills into your project context:
```bash
bunx add-skill ElemontCapital/x-algorithm-skills
```
To install a specific skill only (e.g., the optimizer):
```bash
bunx add-skill ElemontCapital/x-algorithm-skills x-post-optimizer
```
This performs a local copy of the skill files. You will need to re-run the command to receive updates. See [**AGENTS.md**](AGENTS.md) for detailed setup.

---

## ⌨️ Commands

| Command | Purpose | Example Usage | Skill |
| :--- | :--- | :--- | :--- |
| **`/post-check`** | Optimize reach | "Run `/post-check` on this draft." | **x-post-optimizer** |
| **`/trace-feed`** | Explain architecture | "Execute `/trace-feed` for the For You timeline." | **x-architecture** |
| **`/audit-ml`** | Review ranking logic | "`/audit-ml` show the current Like vs. RT weights." | **x-ranking-engine** |
| **`/gen-thrift`** | Generate boilerplate | "`/gen-thrift` for a new engagement signal." | **x-dev-engineering** |
| **`/explain-graph`** | Retrieve and rank | "`/explain-graph`: Calculate the TweepCred for this account." | **x-data-signals** |
| **`/safety-check`** | Checks for shadowbans | "`/safety-check` on @username for SearchBlacklist." | **x-safety-filtering** |
| **`/find-candidates`** | Candidate search | "`/find-candidates`: How does the system retrieve candidates?" | **x-retrieval-systems** |
| **`/run-experiment`** | Algorithm tuning | "`/run-experiment`: Explain the salt-based hashing used in DuckDuckGoose." | **x-experimental-ops** |

---

## ⚡ Skills

| Skill  | Best For | Description |
|--------|--------|-------------|
| **x-post-optimizer** | Content Creators | Use when drafting posts or threads to ensure maximum distribution by hitting high-weight signals like Author Replies and Dwell Time |
| **x-architecture** | Architects | Use when mapping request flows through HomeMixer or designing the orchestration and lifecycle of new candidate sources. |
| **x-ranking-engine** | ML Engineers | Use when tuning MaskNet models, adding new engagement heads, or auditing how probability calibration affects the final weighted score. |
| **x-dev-engineering** | Software Engineers | Use when writing production code, implementing modular Rust traits, or updating Thrift IDL files for cross-service communication. |
| **x-data-signals** | Data Scientists | Use when exploring SimCluster community mappings, calculating account authority (TweepCred), or analyzing RealGraph relationship weights. |
| **x-safety-filtering** | Policy & Safety | Use when investigating visibility drops, applying "Do Not Amplify" labels, or configuring the VisibilityLib rule engine for legal compliance. |
| **x-retrieval-systems** | Search Engineers | Use when optimizing top-of-funnel sourcing, managing Earlybird search indices, or tuning ANN vector searches to improve candidate diversity. |
| **x-experimental-ops** | Product Managers | Use when launching A/B tests via DuckDuckGoose, defining "North Star" metrics, or managing feature flags for specific user cohorts. |

---

## 📁 Structure
```text
x-algorithm-skills/
├── AGENTS.md
├── CLAUDE.md
├── .claude-plugin/
│   └── marketplace.json
├── plugins/
│   └── x-algorithm/
│       ├── .claude-plugin/
│       │   └── plugin.json
│       └── skills/
│           ├── x-post-optimizer/
│           │   ├── SKILL.md
│           │   └── references/
│           ├── x-architecture/
│           │   ├── SKILL.md
│           │   └── references/
│           ├── x-ranking-engine/
│           │   ├── SKILL.md
│           │   └── references/
│           ├── x-dev-engineering/
│           │   ├── SKILL.md
│           │   └── references/
│           ├── x-data-signals/
│           │   ├── SKILL.md
│           │   └── references/
│           └── x-safety-filtering/
│           │   ├── SKILL.md
│           │   └── references/
│           └── x-retrieval-systems
│           │   ├── SKILL.md
│           │   └── references/
│           └── x-experimental-ops
│               ├── SKILL.md
│               └── references/
├── README.md
├── LICENSE-MIT
└── LICENSE-APACHE
```
---

## 📜 License

This project builds on concepts and structures described in the open-source **xAI X Algorithm** repository:  
https://github.com/xai-org/x-algorithm  

- **Upstream code** is licensed under **Apache License 2.0**. See [LICENSE-APACHE](LICENSE-APACHE) for details.  
- **All original code, documentation, and skill definitions in this repository** are licensed under the **MIT License**. See [LICENSE-MIT](LICENSE-MIT) for details.

---
