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

def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def reverse_words(text):
    return ' '.join(text.split()[::-1]) if text else ''

def average_word_length(text):
    words = text.split()
    if not words:
        return 0
    return sum(len(word) for word in words) / len(words)

def capitalize_sentences(text):
    import re
    sentences = re.split('([.!?] *)', text)
    capitalized_sentences = [s.capitalize() for s in sentences]
    return ''.join(capitalized_sentences)

def word_lengths(text):
    words = text.split()
    return {word: len(word) for word in words}

def strip_accents(text):
    import unicodedata
    normalized = unicodedata.normalize('NFD', text)
    
    return ''.join(
        char for char in normalized
        if unicodedata.category(char) != 'Mn'
    )

def slugify(text):
    import re
    import unicodedata

    text = unicodedata.normalize('NFKD', text)
    text = ''.join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def count_vowels(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)