# Word Counter - Day 6
# Lessons learned:
# 1. split() turns a sentence into a list of words - do this before looping
# 2. Store cleaned versions of words as variables before using them as keys
# 3. .lower() and strip(string.punctuation) must happen BEFORE checking the dictionary
# 4. Two loops: one to COUNT, one to PRINT - don't mix them

def main():
    words = {}
    n = input("Sentence: ").lower().strip().split()
    for i in n:
        import string
        w = i.strip(string.punctuation)
        if w in words:
            words[w] = words[w] + 1
        else:
            words[w] = 1
    for i in words:
        print(i, words[i])


if __name__ == "__main__":
    main()