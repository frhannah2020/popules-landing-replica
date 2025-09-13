Popules Landing Page Replica (Assessment)

Task >> Replicate a simple version of [Popules.com](https://popules.com) landing page using Reddit data.

Requirements:

* Scrape Reddit posts from a chosen subreddit (used in this assessment - /confession`)
* Collect \~10 “pages” of posts (≈ 250 posts)
* Keep only posts that contain either **images** or **text**
* Save results into a JSON file (`output.json`) with fields:

  * `post_title`
  * `post_url`
  * `image_url` (if available)
  * `text` (if available)

Optional >> Display JSON data in a simple web page

Installation & Setup

1. Clone this repository
2. Create a Reddit App for API credentials

   * Log in to [Reddit Apps](https://www.reddit.com/prefs/apps)
   * Create a new app → choose script type
   * Copy  client\_id and client\_secret
3. Install dependencies >> requirements.txt

**Usage**

Run the scraper: python scraper.py >> This will generate `output.json` with filtered Reddit posts.

View Results (Webpage)

>> Open `index.html` in your browser.
It will load `output.json` and display posts:

* Title (linked to Reddit post)
* Image (if available)
* Text (if available)
