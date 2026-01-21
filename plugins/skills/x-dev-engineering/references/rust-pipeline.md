# Reference: The Rust Candidate Pipeline

The core logic of the "For You" feed is implemented in Rust using a staged execution model.

### Execution Stages
The `CandidatePipeline` trait executes components in a precise sequence:
1.  **QueryHydrators (Parallel):** Fetches user context (e.g., user embeddings, blocked list).
2.  **Sources (Parallel):** Fetches Tweet IDs from services like Thunder or Earlybird.
3.  **Hydrators (Parallel):** Enriches IDs with full tweet and author metadata.
4.  **Filters (Sequential):** Prunes the list (e.g., `MutedKeywordFilter`).
5.  **Scorers (Sequential):** Assigns ML scores to each remaining candidate.
6.  **Selector (Single):** Sorts and picks the Top-K.

### Implementation Pattern
Every component follows this standard pattern:
```rust
#[async_trait]
impl Filter<MyQuery, MyCandidate> for VisibilityFilter {
    async fn filter(&self, query: &MyQuery, candidates: Vec<MyCandidate>) -> Result<FilterResult<MyCandidate>, String> {
        // Logic to partition candidates based on visibility labels
    }
}
```
