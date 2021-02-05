from vowel_count import vowel_count

def test_counts_string_of_5_vowels():
    solution = vowel_count("aeiou")

    assert solution == 5