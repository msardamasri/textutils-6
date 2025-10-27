# textutils-6

Small Python package for text utilities — group assignment.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/msardamasri/textutils-6.git
cd textutils-6
```

2. Create the environment (with micromamba):

```bash
micromamba create -f environment.yml -y
micromamba activate textutils
```

3. Install the package in editable mode:

```bash
pip install -e .
```

## Running Tests

To run all tests and check coverage:

```bash
pytest
```

To see detailed coverage information:

```bash
pytest --cov=src/textutils --cov-report=term-missing
```

## Features

- `word_count(text)` — case-insensitive counts.
- `top_n(counts, n)` — top-N by frequency, ties alphabetical.
- `normalize_whitespace(text)` — collapse runs of whitespace, trim ends.
- `remove_punctuation(text)` — strip punctuation while keeping spaces and letters.
- `is_palindrome(text)` — check if text reads the same backwards (ignore case and spaces).
- `unique_words(text)` — return a sorted list of distinct words (case-insensitive).
- `reverse_words(text)` — reverse the order of words, not characters.
- `capitalize_sentences(text)` — ensure each sentence starts with a capital letter.
- `word_lengths(text)` — return a dict mapping words to their lengths.
- `strip_accents(text)` — remove accents from characters (e.g., café → cafe).
- `slugify(text)` — convert text to lowercase, hyphen-separated safe string.
- `count_vowels(text)` — count vowels in the given text.
- `camel_to_snake(text)` — convert CamelCase identifiers to snake_case.
- `truncate(text, n)` — shorten text to n characters, adding “...” if needed.
- `collapse_duplicates(text, char)` — replace runs of the same char with one.
- `is_anagram(a, b)` — check if two texts are anagrams (ignore case and spaces).
- `compare_texts(text1, text2)` — compute similarity based on common word ratio.
- `replace_numbers(text)` — replace digits with their word equivalents (2 → two).
- `sentence_count(text)` — count number of sentences in text.
- `average_word_length(text)` — compute mean length of words in text.

## Team

**Team 6** - Python for Data Science, Term 1, Group 6

- Marc Sardà
- Vera Kannewischer
- Yiben Nicolò Fruncillo
- Omar Trabelsi

**Delivery Date:** October 31, 2026

## Project Description

This package was developed as a group assignment for Python for Data Science. We initially handled different features separately, resolving merge conflicts individually with each commit to the master branch. Afterward, we transitioned to working collaboratively on the `average_word_length` feature, contributing to both its testing and core functionality.

---
