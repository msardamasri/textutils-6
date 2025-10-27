def word_count(text):
    from collections import Counter
    words = text.lower().split()
    return dict(Counter(words))

def top_n(word_counts, n):
    return sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))[:n]

def normalize_whitespace(text):
    import re
    return re.sub(r'\s+', ' ', text).strip()
def reverse_words(text):
    return ' '.join(text.split()[::-1]) if text else ''