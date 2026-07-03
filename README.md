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
### Other Agents

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

## Validation

Run the local packaging gate before publishing or editing skills:

```bash
python scripts/validate-skills.py
```

It checks plugin skill paths, exact `SKILL.md` casing, required frontmatter, and local reference links.

---

## ⚡ Skills

| Skill  | Best For | Description |
|--------|--------|-------------|
| **x-post-optimizer** | Content Creators | Optimize posts to hit high-weight signals like Author Replies and Dwell Time—get the algorithm to see you. |
| **x-architecture** | Architects | Map feed flows and candidate sources—design content that naturally aligns with the system. |
| **x-ranking-engine** | ML Engineers | Tune MaskNet and engagement heads—understand why content rises or disappears. |
| **x-dev-engineering** | Software Engineers | Build code that interacts with the ranking system—control cross-service logic behind posts. |
| **x-data-signals** | Data Scientists | Decode hidden account signals, map communities, and predict algorithm behavior. |
| **x-safety-filtering** | Policy & Safety | Audit VisibilityLib rules—stop silent suppression and keep content visible. |
| **x-retrieval-systems** | Search Engineers | Optimize sourcing, vector searches, and candidate diversity for maximum reach. |
| **x-experimental-ops** | Product Managers | Run A/B tests, track metrics, and manipulate flags—treat the feed like a lab. |

---

## ⌨️ Commands

| Command | Purpose | Example Usage | Skill |
| :--- | :--- | :--- | :--- |
| **/post-check** | Boost visibility | "/post-check draft" | **x-post-optimizer** |
| **/trace-feed** | Map content flow | "/trace-feed ForYou" | **x-architecture** |
| **/audit-ml** | Inspect ranking levers | "/audit-ml Likes vs RT" | **x-ranking-engine** |
| **/gen-thrift** | Build system scaffolding | "/gen-thrift new signal" | **x-dev-engineering** |
| **/explain-graph** | Decode account influence | "/explain-graph @user" | **x-data-signals** |
| **/safety-check** | Ensure content visibility | "/safety-check @user" | **x-safety-filtering** |
| **/find-candidates** | Surface potential posts | "/find-candidates topic" | **x-retrieval-systems** |
| **/run-experiment** | Test algorithm tweaks | "/run-experiment feed-test" | **x-experimental-ops** |

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
