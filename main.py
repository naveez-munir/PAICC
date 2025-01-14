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

# Sort the frequencies in descending order
sorted_freq = dict(sorted(word_freq.items(), key=lambda x: x[1], reverse=True))

# Print the 20 most common words and their frequencies
print("Top 20 most frequent words:")
count = 0
for word, freq in sorted_freq.items():
    if count >= 20:
        break
    print(f"{word}: {freq}")
    count += 1
