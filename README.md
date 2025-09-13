# Popules Landing Page Replica (Assessment)

Installation & Setup
1. Clone this repository
2. Create a Reddit App for API credentials
3. Usage

Run the scraper:
python scraper.py >> This will generate `output.json` with filtered Reddit posts.

---

View Results (  Webpage)

Open `index.html` in your browser.
It will load `output.json` and display posts:

* Title (linked to Reddit post)
* Image (if available)
* Text (if available)

---

## 📂 Project Structure

```
popules-landing-replica/
├── scraper.py         # Python Reddit scraper
├── output.json        # Sample scraped data
├── index.html         # Web page to display JSON
├── requirements.txt   # Dependencies
└── README.md          # Documentation
```


## ✨ Notes

* Fetches \~250 posts from `r/confession`
* Keeps only posts with **images** or **text**
* Example output is included as `output.json`

---
