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

def camel_to_snake(text):
    import re
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()

def truncate(text, n):
    if len(text) <= n:
        return text
    return text[:n-3] + '...' if n > 3 else text[:n]

def collapse_duplicates(text, char):
    import re
    return re.sub(f'{re.escape(char)}+', char, text)

def is_anagram(a, b):
    a_clean = ''.join(c for c in a.lower() if c.isalpha())
    b_clean = ''.join(c for c in b.lower() if c.isalpha())
    return sorted(a_clean) == sorted(b_clean)

def compare_texts(text1, text2):
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    if not words1 and not words2:
        return 1.0
    return len(words1 & words2) / len(words1 | words2)

def replace_numbers(text):
    words = {'0':'zero','1':'one','2':'two','3':'three','4':'four',
             '5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
    return ''.join(words[c] if c in words else c for c in text)

def sentence_count(text):
    import re
    sentences = re.split(r'[.!?]+', text.strip())
    return len([s for s in sentences if s.strip()])