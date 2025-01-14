from collections import Counter
import re

# Read transcript file and store contents
with open('./transcript.txt', 'r') as file:
    transcript_content = file.read()

# Convert to lowercase and split into words
# Remove punctuation and filter out empty strings
words = re.findall(r'\w+', transcript_content.lower())

# Count word frequencies
word_freq = Counter(words)

# Print the 20 most common words and their frequencies
print("Top 20 most frequent words:")
for word, count in word_freq.most_common(20):
    print(f"{word}: {count}")
