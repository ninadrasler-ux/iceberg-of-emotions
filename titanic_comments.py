import json

import emoji

from collections import Counter

from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

# Load Reddit comments
with open("titanic_comments.json", "r", encoding="utf-8") as f:
    reddit_json = json.load(f)

# Extract comment text
comments = []

for comment in reddit_json[1]["data"]["children"]:
    body = comment["data"].get("body")
    
    if body:
        comments.append(body)

# Sentiment and emoji counters
positive_comments = 0
negative_comments = 0
neutral_comments = 0

emoji_counter = Counter()

comments_with_emojis = 0

emoji_compound_sum = 0
emoji_abs_compound_sum = 0
emoji_comment_count = 0

non_emoji_compound_sum = 0
non_emoji_abs_compound_sum = 0
non_emoji_comment_count = 0

# Analyze comments
for comment in comments:

    # Emoji analysis
    emojis = emoji.emoji_list(comment)

    for e in emojis:
        emoji_counter[e["emoji"]] += 1

    
    if emojis:
        comments_with_emojis += 1

        
    # Sentiment analysis
    scores = sia.polarity_scores(comment)

    compound = scores["compound"]

    # Compare comments with and without emojis
    if emojis:

        emoji_compound_sum += compound
        emoji_abs_compound_sum += abs(compound)
        emoji_comment_count += 1

    else:

        non_emoji_compound_sum += compound
        non_emoji_abs_compound_sum += abs(compound)
        non_emoji_comment_count += 1

    # Classify comments
    if compound > 0.05:
        positive_comments += 1

    elif compound < -0.05:
        negative_comments += 1

    else:
        neutral_comments += 1
        
    
# Calculate averages
avg_emoji_compound = (
    emoji_compound_sum / emoji_comment_count
)

avg_non_emoji_compound = (
    non_emoji_compound_sum / non_emoji_comment_count
)

avg_emoji_abs = (
    emoji_abs_compound_sum / emoji_comment_count
)

avg_non_emoji_abs = (
    non_emoji_abs_compound_sum / non_emoji_comment_count
)


# Results
print(f"Total comments: {len(comments)}")
print(f"Comments with emojis: {comments_with_emojis}")

print()

print(f"Positive comments: {positive_comments}")
print(f"Negative comments: {negative_comments}")
print(f"Neutral comments: {neutral_comments}")

print()

print("Most common emojis:")

for emoji_symbol, count in emoji_counter.most_common(10):
    print(f"{emoji_symbol}: {count}")
    
print()
print("Average compound")

print(f"Emoji comments: {avg_emoji_compound:.2f}")
print(f"Non-emoji comments: {avg_non_emoji_compound:.2f}")

print()
print("Average absolute compound")

print(f"Emoji comments: {avg_emoji_abs:.2f}")
print(f"Non-emoji comments: {avg_non_emoji_abs:.2f}")

