def word_count(text):
    from collections import Counter
    words = text.lower().split()
    return dict(Counter(words))

def top_n(word_counts, n):
    return sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))[:n]

def normalize_whitespace(text):
    import re
    return re.sub(r'\s+', ' ', text).strip()

def unique_words(text):
    words = text.lower().split()
    words = [word.strip(".,!?;:'\"()[]{}") for word in words]
    return sorted(set(words))

def remove_punctuation(text):
    import string
    return text.translate(str.maketrans('', '', string.punctuation))
