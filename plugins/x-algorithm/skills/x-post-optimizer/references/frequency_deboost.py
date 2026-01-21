# Frequency penalty logic
```bash
def apply_frequency_penalty(posts, author_id):
    sorted_posts = sorted(posts, key=lambda p: p.timestamp)
    scores = []
    for i, post in enumerate(sorted_posts):
        if i > 0 and (post.timestamp - sorted_posts[i-1].timestamp).total_seconds() < 3600:
            post.score *= 0.5  # Halve for <1 hour
        scores.append(post.score)
    return scores
```