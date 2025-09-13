import praw
import json

reddit = praw.Reddit(
    client_id="rgSi9cXYcSHJ53iFyoHwqw",
    client_secret="ilEwpDBYxEmFuivKWa6RjGq_e8UG-A",
    user_agent="popules_scraper by u/Calm_Painting_8017"
)

subreddit = reddit.subreddit("confession")  

results = []

# Fetch ~250 posts (≈ 10 pages if 1 page ~ 25 posts)
for post in subreddit.hot(limit=250):
    post_data = {
        "post_title": post.title,
        "post_url": f"https://www.reddit.com{post.permalink}"
    }

    # If the post has an image
    if post.url.endswith(('.jpg', '.png', '.jpeg', '.gif')):
        post_data["image_url"] = post.url

    # If the post is a text/self post
    if post.is_self and post.selftext:
        post_data["text"] = post.selftext

    # Only keep if it has either image or text
    if "image_url" in post_data or "text" in post_data:
        results.append(post_data)

# Save to JSON
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"Saved {len(results)} posts with images or text.")

