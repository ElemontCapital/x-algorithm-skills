# Reference: Model Architecture (MaskNet & Phoenix)

The X ranking system has evolved into a sophisticated deep learning pipeline.



### MaskNet
The core of the Heavy Ranker often utilizes **MaskNet**, a deep learning architecture specifically designed for CTR (Click-Through Rate) prediction in recommendation systems.
* **Instance-wise Masking:** Dynamically masks unimportant features for specific user-item pairs.
* **High-order Interactions:** Captures complex relationships between features that linear models miss.

### Multi-Task Learning (MTL)
Instead of one model per action, X uses a shared backbone with multiple "heads":
1.  **Binary Classifiers:** Predict $P(\text{Like})$, $P(\text{Reply})$, $P(\text{Retweet})$, $P(\text{Quote})$.
2.  **Continuous Regression:** Predicts **Dwell Time** (how many seconds a user will look at the tweet).
3.  **Negative Heads:** Predicts $P(\text{Report})$ or $P(\text{Negative Feedback})$.

### Candidate Isolation Design
A specific architectural constraint in the X repo is that candidates are scored in isolation. Unlike "List-wise" rankers (which compare tweets against each other during the scoring phase), X uses "Point-wise" ranking.
- **Benefit:** Allows for $O(N)$ parallel scoring.
- **Trade-off:** The model cannot naturally "know" it is showing too many similar tweets; this must be handled later in the **Mixing/Diversity** stage of HomeMixer.
