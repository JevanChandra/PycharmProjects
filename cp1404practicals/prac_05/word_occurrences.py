"""
Word Occurrences

Estimate: 25 minutes
Actual:   40 minutes
"""

text = input("Text: ")
words = text.split()
word_count = {}
longest_word_length = len(words[0])

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
        if len(word) > longest_word_length:
            longest_word_length = len(word)
print()
word_count = sorted(word_count.items())
print(word_count)
for word in word_count:
    print(f"{word[0]:{longest_word_length}} : {word[1]}")