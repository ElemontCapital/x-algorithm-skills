---
name: x-architecture
description: Deep knowledge of the X (Twitter) recommendation engine architecture, focusing on HomeMixer orchestration, ProductMixer framework components, and the candidate pipeline lifecycle.
version: 1.0.0
license: MIT
---

# X Algorithm Architecture

Use this skill when you need to reason about the system design, service orchestration, or data flow of the X recommendation engine. It is particularly useful for understanding how the "For You" timeline is constructed using the `HomeMixer` and `ProductMixer` frameworks.

## Context

The X recommendation engine is a large-scale distributed system designed to deliver high-relevance content with sub-second latency. The primary entry point is **HomeMixer**, which is built using the **ProductMixer** Scala framework. The heavy lifting of candidate processing is offloaded to a modular Rust-based **Candidate Pipeline**.



For detailed breakdowns of the execution flow and service roles, see:
- [Pipeline Lifecycle](./references/pipeline-lifecycle.md)
- [Service Map](./references/service-map.md)

## What it does

* **Explains Orchestration:** Details how `HomeMixer` coordinates multiple candidate sources and scoring stages.
* **Defines Framework Components:** Breaks down `ProductMixer` abstractions such as `CandidateSource`, `Scorer`, `Filter`, and `Hydrator`.
* **Maps Data Flow:** Traces a tweet from sourcing (In-Network/Out-of-Network) through to final timeline mixing.
* **Identifies Logic Boundaries:** Differentiates between Scala-based orchestration logic and Rust-based performance logic.

## Guidelines

* **Component-Based Architecture:** All feed features are implemented as discrete components within the `ProductMixer` lifecycle. If the user wants to add a new ranking signal, it must be integrated as a `Scorer`.
* **ProductMixer Lifecycle:** Familiarize yourself with the sequence:
    1.  **Candidate Sourcing:** Fetching ~1,500 candidates from multiple sources.
    2.  **Candidate Hydration:** Fetching metadata (author info, tweet text) for the IDs retrieved.
    3.  **Scoring:** Applying ML models (like the Heavy Ranker) to assign a score.
    4.  **Filtering:** Applying `VisibilityLib` to prune content (blocked users, NSFW).
    5.  **Mixing:** Combining sources and applying diversity rules.
* **Candidate Isolation:** During scoring, candidates are treated as independent units. They can attend to user context (the "Query") but cannot attend to other candidates in the same batch, allowing for massive parallelization.
* **Rust/Scala Interop:** High-level orchestration (routing and mixing) happens in Scala. Low-level, CPU-intensive tasks (Scoring and Filtering) are implemented in Rust for maximum throughput.
* **Thrift Contracts:** All inter-service communication (e.g., between HomeMixer and the Heavy Ranker) is governed by Thrift IDL files. Changes to data structures must be reflected in these schemas.

## Example Trigger Prompts

* "How does HomeMixer use ProductMixer to build the For You timeline?"
* "Explain the stages of the X recommendation pipeline."
* "What is the role of a CandidateSource in this architecture?"
* "How does the system handle In-Network vs. Out-of-Network content sourcing?"
* "Where does the transition from Scala orchestration to Rust execution happen?"
