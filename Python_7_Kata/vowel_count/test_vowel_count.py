from vowel_count import vowel_count

def test_counts_string_of_5_vowels():
    solution = vowel_count("aeiou")

    assert solution == 5

def test_returns_0_for_empty_string():
    solution = vowel_count("")

    assert solution == 0

def test_can_acount_for_mixed_string():
    solution = vowel_count("o a kak ushakov lil vo kashu kakao")

    assert solution == 13