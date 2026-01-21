# Reference: Service Map

Key services involved in the X algorithm architecture:

| Service | Language | Primary Responsibility |
| :--- | :--- | :--- |
| **HomeMixer** | Scala/Rust | Main orchestrator; defines the "For You" pipeline. |
| **Thunder** | Rust | High-speed In-Network candidate sourcing. |
| **Phoenix** | Python/Rust | Out-of-Network ML discovery and embedding-based retrieval. |
| **Earlybird** | Java | The Search index; provides real-time retrieval for keyword and topic matches. |
| **VisibilityLib** | Rust | Health and Safety engine; handles de-amplification and legal compliance. |
| **Navi** | Rust | ML Model serving; provides the infrastructure to run Heavy Ranker models. |
| **Manhattan** | C++ | Core distributed key-value store for user and tweet data. |

### Technical Interaction
Most services communicate via **Finagle (Thrift)**. The architecture favors "Thin Clients"—where the client (HomeMixer) manages the logic of what to call, and the service simply returns computed values (like scores or IDs).
