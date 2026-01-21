# Reference: Filtering Logic & Architecture

`VisibilityLib` is a Rust-based library designed to answer one question: *"Can User A see Tweet B?"*

### The Filtering Pipeline
When a request is made, `VisibilityLib` executes a chain of logic:

1.  **Legal & Compliance:**
    * Is the content geo-blocked in the user's country?
    * Is the author deactivated or suspended?

2.  **User Graph State:**
    * Does User A block User B?
    * Does User B block User A?
    * Has User A muted User B?

3.  **Content Safety (Viewer Context):**
    * Is the content NSFW? (Check viewer's `include_nsfw` setting).
    * Is the content "Trophyless"? (Check viewer's quality filters).

4.  **Ranking Adjustments (Downstream):**
    * If the content survives the hard filters, `VisibilityLib` passes metadata to the **Heavy Ranker** to apply negative weights (e.g., if the user has "Muted this conversation").
