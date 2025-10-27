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

def test_remove_punctuation_removes_all_punctuation():
    text = "Hello, world! This is a test."
    assert c.remove_punctuation(text) == "Hello world This is a test"