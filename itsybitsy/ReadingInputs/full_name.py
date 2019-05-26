def minimalOperations(words):
    result = []
    for word in words:
        word_len = len(word)
        start = 0
        new_word =""
        count = 0
        while word[start] and start < word_len-1:
            if word[start] == word[start+1]:
                start = start + 1
                count = count + 1
                continue
            else:
                new_word = new_word + word[start]
            start = start + 1
        if count:
            new_word_len = len(new_word)-2 + count
        else:
            new_word_len = len(new_word) - 2
        result.append(word_len - new_word_len)

    print(result)


n = int(input())
words = [input().strip() for i in range(n)]

minimalOperations(words)
