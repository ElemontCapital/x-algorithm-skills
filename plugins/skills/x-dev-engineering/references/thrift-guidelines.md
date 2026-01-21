# Reference: Communication & Thrift Guidelines

X uses **Apache Thrift** as its Interface Definition Language (IDL) to ensure type safety across different languages (Rust, Scala, Java, Python).

### Key Thrift Files
* `request.thrift`: Defines the `MixerRequest` parameters.
* `ranking.thrift`: Defines the features passed to the Heavy Ranker.
* `visibility.thrift`: Defines the safety labels and filtering results.

### Best Practices
1.  **Backward Compatibility:** Never change a field ID in a Thrift file. Always add new fields as `optional` to avoid breaking existing services.
2.  **Naming:** Use CamelCase for types and snake_case for fields.
3.  **Efficiency:** Avoid sending large blobs of text through Thrift. Pass IDs where possible and let the receiving service hydrate the data locally from a cache or database.

### Compilation
Changes to `.thrift` files require re-running the build (e.g., `bazel build` or `cargo build`) to regenerate the language-specific bindings.
