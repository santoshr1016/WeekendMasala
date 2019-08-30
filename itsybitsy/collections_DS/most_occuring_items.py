words = [
       'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
       'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
       'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
       'my', 'eyes', "you're", 'under'
]

from collections import Counter

word_counts = Counter(words)
print(word_counts)
top_3 = word_counts.most_common(3)
print(top_3)
morewords = ['why','are','you','not','looking','in','my','eyes']

for word in morewords:
    word_counts[word] += 1
print(word_counts)

# word_counts.update(morewords)
print("using count")
s = "This is the word, which is the most repeated"
print(s.count("is"))