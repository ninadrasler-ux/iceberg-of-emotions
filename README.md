
# *Titanic Emoji & Sentiment Exploration*

---

## 🎬 Why study emojis on Titanic comments?
Because if there’s any film that turns the internet into a puddle of feelings, it’s Titanic.
So I wanted to see what happens when you take a famously emotional movie, mix it with Reddit, and then zoom in on the tiny symbols people use to express big feelings.

This mini‑project is basically a dive into the emotional debris field:
Which emojis float to the surface?
Do people cry more than they laugh?
And are emoji‑users actually more dramatic — or just more honest?

It’s a light, playful exploration of how people talk about a story everyone already knows… and still somehow cries about.

---

## ❓ What was I trying to understand?

### 💬 **Do people use emojis when talking about Titanic — and which ones?**

### ❤️ **Are comments with emojis more emotionally charged than those without?**

### 😭 **Which emotional tones dominate the discussion?**

---

## 🧪 Method: How the data was collected and processed

- Pulled ~100 top-level Reddit comments about *Titanic* using a JSON export.
- Cleaned the text (removed placeholders, ignored nested replies).
- Ran **emoji extraction** using the `emoji` library.
- Performed **sentiment analysis** using NLTK’s `SentimentIntensityAnalyzer`.
- Split comments into two groups:
  - comments **with emojis**
  - comments **without emojis**
- Calculated:
  - average **compound** sentiment
  - average **absolute compound** sentiment (emotional intensity)
  - frequency of each emoji

---

## 📊 Emoji frequency table

| Emoji | Count |
|------|------:|
| 😭 | 4 |
| 💔 | 4 |
| ❤️ | 3 |
| 😊 | 2 |
| 🙏 | 2 |
| 🥹 | 2 |
| 😂 | 1 |
| 🙄 | 1 |
| 🤡 | 1 |
| 💀 | 1 |

---

## 📈 Key findings

### 😢 **1. The most common emojis were 😭 and 💔**  
Not surprising for *Titanic* — grief and heartbreak dominate.

### 📉 **2. Only 11 out of 98 comments contained emojis**  
This is important: the sample of emoji-using comments is small.

### 💡 **3. Emoji comments were slightly more emotional**  
- **Average compound (emoji comments): 0.41**  
- **Average compound (non-emoji): 0.31**

- **Average absolute compound (emoji): 0.54**  
- **Average absolute compound (non-emoji): 0.49**

> *Comments containing emojis showed slightly higher average compound and absolute compound scores than comments without emojis.  
> However, only 11 of the 98 comments contained emojis, so the difference should be interpreted cautiously.*

### 😀 **4. Overall sentiment skewed positive**  
- **58 positive**  
- **17 negative**  
- **23 neutral**

---

## 🌊 Final thoughts

This was a small but revealing exploration of how emotional symbols appear in discussions about a famously emotional film.  
Even with a small sample, emojis tended to accompany **more emotionally intense** comments — especially those expressing sadness or heartbreak.

---

🧠 **Full script**  
If you're curious about the exact steps, the full code lives in `titanic_comments.py`.

