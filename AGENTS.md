# 🤖 Agent Integration Guide
This repository follows the Agent Skills Standard, a specification for providing AI agents with domain-specific "expertise" through structured documentation and reference material.

While optimized for Claude Code via its native plugin system, this repository is designed to be "Agent Agnostic"—working seamlessly with Cursor, GitHub Copilot, Windsurf, Roo Code, and custom LLM implementations.

---

## 🧠 Core Agent Personas
Following the Vercel Agent Skills model, we categorize our skills into specialized personas.

You can "summon" these personas by providing the corresponding SKILL.md files to your agent.

### 📈 The Growth Architect (`x-post-optimizer`)
- **Best for:** Viral content strategy and reach optimization.
- **Key Files:** `.../x-post-optimizer/SKILL.md`, `references/engagement-multipliers.md`

### 🏗️ The System Designer (`x-architecture` & `x-retrieval-systems`)
- **Best for:** Understanding the macro-flow from retrieval to timeline delivery.
- **Key Files:** `.../x-architecture/SKILL.md`, `.../x-retrieval-systems/SKILL.md`

### 🧠 The ML Specialist (`x-ranking-engine` & `x-experimental-ops`)
- **Best for:** Deep-dives into MaskNet scoring and A/B test analysis.
- **Key Files:** `.../x-ranking-engine/SKILL.md`, `.../x-experimental-ops/SKILL.md`

### 🛠️ The Algorithm Engineer (`x-dev-engineering`)
- **Best for:** Writing Rust/Scala code and modifying Thrift schemas.
- **Key Files:** `.../x-dev-engineering/SKILL.md`, `references/rust-pipeline.md`

### ⚖️ The Trust & Safety Auditor (`x-data-signals` & `x-safety-filtering`)
- **Best for:** Investigating shadowbans, reputation, and toxicity filtering.
- **Key Files:** `.../x-data-signals/SKILL.md`, `.../x-safety-filtering/SKILL.md`

---

## 📋 Skill Discovery Dashboard

| Skill | Role | Core Capability |
|--------|--------|-------------|
| x-post-optimizer | Content Strategist | Optimizes reach via HeavyRanker weight alignment. |
| x-architecture | System Architect | Maps HomeMixer and candidate generation flows. |
| x-ranking-engine | ML Engineer | Audits MaskNet scoring and MTL probability heads. |
| x-dev-engineering | Software Engineer | Assists with Rust/Scala interop and Thrift definitions. |
| x-data-signals | Data Scientist | Explains SimClusters, TweepCred, and RealGraph. |
| x-safety-filtering | Safety Analyst | Decodes VisibilityLib labels and shadowban logic. |
| x-retrieval-systems | Search Engineer | Manages Earlybird indices and ANN vector search. |
| x-experimental-ops | Product Manager | Tracks DuckDuckGoose tests and "North Star" metrics. |

---

## 🛠 Third-Party Integration
To ensure third-party agents (Cursor, Copilot, Roo Code) utilize these skills effectively, follow the instructions below.
### 1. Cursor & Windsurf
These agents do not have a "plugin" discovery layer. They rely on local file indexing.
- **Recommended Action:** Create a `.cursorrules` (or `.windsurfrules`) file in your project root with the following content:
```
Maintain awareness of the X Algorithm Skills located in ./plugins/x-algorithm/skills/. 
If a query relates to Twitter/X distribution, ranking, or engineering, reference the 
corresponding SKILL.md and its associated /references/ folder before answering.
```
### 2. GitHub Copilot / VS Code Chat
Use the **@workspace** participant.
Trigger: `"@workspace Use the x-post-optimizer skill to review this tweet draft."`

### 3. Roo Code / Custom Agents
Attach the specific `SKILL.md` file to the context window to "ground" the LLM in the algorithm's logic.

### 4. Other Agents
May require you to manually open the `SKILL.md` file you want the agent to "read" into its context window.
