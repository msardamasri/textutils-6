import textutils.core as c

def test_word_count_basic():
       text = "Red red BLUE"
       assert c.word_count(text) == {"red": 2, "blue": 1}

def test_top_n_order_and_ties():
    counts = {"a": 2, "b": 2, "c": 1}
    assert c.top_n(counts, 2) == [("a", 2), ("b", 2)]

def test_normalize_whitespace_removes_extra_spaces():
    text = "  a   b \n  c  "
    assert c.normalize_whitespace(text) == "a b c"

def test_unique_words_handles_punctuation_and_case():
    text = "Hello, hello! World."
    assert c.unique_words(text) == ["hello", "world"]

def test_remove_punctuation_removes_all_punctuation():
    text = "Hello, world! This is a test."
    assert c.remove_punctuation(text) == "Hello world This is a test"

def test_is_palindrome():
    assert c.is_palindrome("Racecar")
    assert c.is_palindrome("nurses run")
    assert c.is_palindrome("Was it a car or a cat I saw")
    assert not c.is_palindrome("Hello")
    assert not c.is_palindrome("Python")

def test_reverse_words():
    from textutils.core import reverse_words
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("a b c") == "c b a"
    assert reverse_words("single") == "single"
    assert reverse_words("") == ""

def test_average_word_length():
    text = "Hello world"
    words = text.split()
    avg_length = sum(len(word) for word in words) / len(words)
    assert avg_length == 5.0

def test_capitalize_sentences():
    text = "hello world. this is a test! is it working?"
    expected = "Hello world. This is a test! Is it working?"
    assert c.capitalize_sentences(text) == expected

def test_word_lengths():
    text = "hello world python"
    assert c.word_lengths(text) == {"hello": 5, "world": 5, "python": 6}

def test_strip_accents():
    text = "café naïve façade"
    assert c.strip_accents(text) == "cafe naive facade"

def test_slugify():
    assert c.slugify("Hello World!") == "hello-world"
    assert c.slugify("Café & Château") == "cafe-and-chateau"
    assert c.slugify("  spaces  here  ") == "spaces-here"

def test_count_vowels():
    assert c.count_vowels("Hello World") == 3
    assert c.count_vowels("Python Programming") == 4
    assert c.count_vowels("BCDFG") == 0
    assert c.count_vowels("AEIOUaeiou") == 10

def test_camel_to_snake():
    assert c.camel_to_snake("CamelCase") == "camel_case"
    assert c.camel_to_snake("HTTPRequest") == "http_request"
    assert c.camel_to_snake("SimpleText") == "simple_text"
    assert c.camel_to_snake("helloWorld") == "hello_world"

def test_truncate():
    text = "This is a long text that needs truncation"
    assert c.truncate(text, 10) == "This is..."
    assert c.truncate(text, 5) == "Th..."
    assert c.truncate(text, 3) == "Thi"

def test_collapse_duplicates():
    text = "hello!!! world??? yes..."
    assert c.collapse_duplicates(text, '!') == "hello! world??? yes..."
    assert c.collapse_duplicates(text, '.') == "hello!!! world??? yes."
    assert c.collapse_duplicates("aaabbbccc", 'a') == "abbbccc"

def test_is_anagram():
    assert c.is_anagram("listen", "silent") == True
    assert c.is_anagram("Hello", "World") == False
    assert c.is_anagram("Dormitory", "Dirty room") == True
    assert c.is_anagram("abc", "abcd") == False