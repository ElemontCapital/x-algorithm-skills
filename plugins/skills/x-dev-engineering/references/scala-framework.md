# Reference: Scala ProductMixer Framework

While the heavy lifting is in Rust, the high-level orchestration uses **ProductMixer**, a Scala framework developed at Twitter.



### Core Abstractions
* **ProductPipeline:** The entry point for a specific product surface (e.g., `HomeTimeline`).
* **MixerPipeline:** Combines results from multiple `CandidatePipelines` (e.g., mixing Tweets, Ads, and User Recommendations).
* **CandidatePipelineConfig:** Defines where to fetch candidates and which filters/scorers to apply.

### Why Scala?
Scala is used for its powerful type system and **Finagle** integration, making it ideal for managing complex request routing and "mixing" different types of content (Ads vs. Organic) that may come from entirely different microservices.

### Interop Logic
Scala services call Rust services via **gRPC/Thrift**. A typical request flow starts in a Scala `ProductPipeline`, which makes a remote call to the Rust-based `HomeMixer` to perform the heavy-duty ranking.
