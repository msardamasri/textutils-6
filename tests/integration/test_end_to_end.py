import textutils.core as c

def test_ultimate_mega_pipeline():
    text = "  Héllo   Wórld!!! Café costs $123.   CamelCaseExample is COOL. A man a plan a canal Panama! Listen vs Silent.   "
    final_result = c.truncate(
        c.slugify(
            c.collapse_duplicates(
                c.capitalize_sentences(
                    c.replace_numbers(
                        c.camel_to_snake(
                            c.remove_punctuation(
                                c.strip_accents(
                                    c.normalize_whitespace(text)
                                )
                            )
                        )
                    )
                ), '-'
            )
        ), 120
    )
    assert "hello-world" in final_result
    assert "cafe-costs" in final_result
    assert "one-two-three" in final_result
    assert "camel-case-example" in final_result
    assert "cool" in final_result.lower()
    
    word_counts = c.word_count(text)
    top_words = c.top_n(word_counts, 5)
    assert len(top_words) > 0
    
    assert c.is_palindrome("A man a plan a canal Panama")
    assert c.is_anagram("Listen", "Silent")
    
    reversed_text = c.reverse_words("Hello World")
    assert reversed_text == "World Hello"
    
    assert c.count_vowels("Hello") > 0
    
    similarity = c.compare_texts("hello world", "world hello")
    assert similarity > 0.5
    
    assert c.average_word_length("test words") > 0
    
    unique = c.unique_words("hello hello world")
    assert "hello" in unique and "world" in unique
    
    lengths = c.word_lengths("test")
    assert "test" in lengths
    
    assert c.sentence_count("First. Second! Third?") == 3