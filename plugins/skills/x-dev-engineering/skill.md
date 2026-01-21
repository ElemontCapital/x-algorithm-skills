---
name: x-dev-engineering
description: Technical expertise for developing and extending the X recommendation engine, focusing on Rust traits, Scala ProductMixer configurations, and Thrift-based RPC communication.
version: 1.0.0
license: MIT
---

# X Development Engineering

Use this skill when you are writing code, debugging service interactions, or extending the recommendation framework. It provides the low-level implementation details for the **ProductMixer** (Scala) and **Candidate Pipeline** (Rust) frameworks used to build X's feeds.

## Context

The engineering philosophy behind X's algorithm has shifted toward a high-performance **Rust-first** approach for core logic, while maintaining **Scala** for high-level orchestration. Services like `HomeMixer` act as the glue, using **Thrift** schemas to communicate across service boundaries. Development involves implementing modular traits (Filters, Scorers, Hydrators) that fit into a strictly ordered pipeline execution model.



For implementation specs and best practices, see:
- [The Rust Candidate Pipeline](./references/rust-pipeline.md)
- [Scala ProductMixer Framework](./references/scala-framework.md)
- [Communication & Thrift Guidelines](./references/thrift-guidelines.md)

## What it does

* **Scaffolds Pipeline Components:** Provides boilerplate and logic for implementing new `Filters`, `Scorers`, or `CandidateSources` in Rust.
* **Debugs Cross-Language Logic:** Assists in tracing data as it moves from Scala orchestration to Rust execution layers.
* **Implements Thrift Interfaces:** Generates and validates service-to-service communication contracts.
* **Optimizes Async Execution:** Applies best practices for `tokio` and `async-trait` to ensure non-blocking performance in the pipeline.

## Guidelines

* **Trait-Based Development:** Everything in the Rust core is a trait.
    * `Filter<Q, C>`: Receives a vector of candidates and returns a filtered vector.
    * `Scorer<Q, C>`: Must preserve the count and order of candidates, assigning scores in-place.
    * `Hydrator<Q, C>`: Performs I/O to enrich candidates with metadata.
* **Async/Await Patterns:** Use `#[async_trait]` for all pipeline components. Ensure that `Hydrators` and `Sources` execute in parallel where possible using `futures::join_all`.
* **Memory Management:** Leverage `Arc<T>` for shared read-only state across the pipeline (e.g., config parameters or pre-loaded ML model weights).
* **Error Handling:** Components should return `Result<T, String>`. Avoid panics within the pipeline to ensure that a failure in one candidate source doesn't crash the entire user request.
* **Scala-Rust Interop:** Understand that Scala (`ProductMixer`) handles the "Which pipeline do I run?" logic, while Rust (`HomeMixer`) handles the "How do I run this pipeline?" logic.
* **Observability:** Use the `#[xai_stats_macro]` to wrap key functions. This ensures that latency and success rates for your new components are automatically tracked in internal dashboards.

## Example Trigger Prompts

* "How do I implement a new Filter in the Rust candidate-pipeline?"
* "Show me the Thrift definition for adding a new engagement signal to the Scorer."
* "Explain the execution order of Hydrators vs. Scorers in HomeMixer."
* "Write a Scala ProductMixer config for a new 'Trending' candidate source."
* "Help me debug an async deadlock in the Thunder service logic."
