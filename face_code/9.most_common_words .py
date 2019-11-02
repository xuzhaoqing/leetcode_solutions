# Amazon is partnering with the linguistics department at a local university to analyze important works of English literature and identify patterns in word usage across different eras. To ensure a cleaner output, the linguistics department has provided a list of commonly used words (e.g., "an", "the", etc.) to exclude from the analysis. In the context of this search, a word is an alphabetic sequence of characters having no whitespace or punctuation. Write an algorithm to ﬁnd the most frequently used word in the text excluding the commonly used words.

# Input
# The input to the function/method consists of two arguments -
# literatureText, a string representing the block of text;
# wordsToExclude , a list of strings representing the commonly used words to be excluded while analyzing the word frequency.
# Output
# Return a list of strings representing the most frequently used word in the text or in case of a tie, all of the most frequently used words in the text.
# Note
# Words that have a different case are counted as the same word. The order of words does not matter in the output list. All words in the wordsToExclude list are unique.
# Any character other than letters from the English alphabet should be treated as white space.
# Example
# Input:
# literatureText = “Jack and Jill went to the market to buy bread and cheese. Cheese is Jack's and Jill’s favorite food.”
# wordsToExclude = ["and", "he", "the", "to", "is", "Jack", "Jill"]
# Output:
# ["cheese", “s”]
# Explanation:
# The word “and” has a maximum of three frequency but this word should be excluded while analyzing the word frequency.
# The words “Jack”, “Jill”, “s”, "to" and "cheese” have the next maximum frequency(two) in the given text but the words “Jack”, "to" and “Jill” should be excluded as these are commonly used words which you are not interested to include.
# So the output is ["cheese", “s”] or [“s”, "cheese"] as the order of words does not matter.
from collections import Counter
def maxCommonWord(literatureText, wordsToExclude):
    wordsToExclude = set([w.lower() for w in wordsToExclude])
    words = ''.join([x.lower() if x.isalpha() else ' ' for x in literatureText ])
    words = [word for word in words.split() if word and word not in wordsToExclude]
    counter = Counter(words)
    ret = []
    mostCommon = 0
    for w in counter:
        if counter[w] > mostCommon:
            ret = [w]
            mostCommon = counter[w]
        elif counter[w] == mostCommon:
            ret.append(w)
    return ret

if __name__ == "__main__":
    text = "    "
    words = ["and", "he", "the", "to", "is", "Jack", "Jill"]
    print(maxCommonWord(text,words))