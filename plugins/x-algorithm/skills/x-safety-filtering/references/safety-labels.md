# Reference: Safety Labels & Shadowbans

"Shadowbanning" is the colloquial term for specific visibility states defined in the codebase.



### Critical Labels
* **`DoNotAmplify`:** The content is visible on the profile but removed from discovery surfaces (For You, Search, Trends).
* **`SearchBlacklist`:** The user's account and tweets are completely hidden from Search results. This is often triggered by excessive hashtag spam or bot-like behavior.
* **`TrendsBlacklist`:** The user cannot appear in the "Trending" tab.
* **`NsfwUser` / `NsfwHighPrecision`:** Labels the account as strictly 18+. If a user has not opted-in to view sensitive content, they will never see tweets from these accounts.

### Trigger Conditions
These labels are often applied by:
1.  **Bot Detection:** Rapid-fire posting or following.
2.  **Network Analysis:** Being "graph-blocked" by a large cluster of users.
3.  **Toxicity Models:** Consistently posting content that NLP models flag as abusive.
