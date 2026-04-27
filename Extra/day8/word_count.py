"""
word_counter
---------------
Counts how many times each word appears in a sentence.

- .lower().strip().split(): normalises input and splits into a list of words
- string.punctuation: contains all punctuation characters
- .strip(string.punctuation): removes punctuation from both ends of each word
- words.get(clean_word, 0) + 1: returns current count or 0 if unseen, then increments
- if __name__ == "__main__": ensures main() only runs when executed directly
"""
import string

def main():
    words = {}
    sentence = input("Sentence: ").lower().strip().split()
    
    for word in sentence:
        clean_word = word.strip(string.punctuation)
        words[clean_word] = words.get(clean_word, 0) + 1
    
    for word in words:
        print(word, words[word])

if __name__ == "__main__":
    main()