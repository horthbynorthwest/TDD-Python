from middle_letter import middle_letter

def test_returns_the_letter_of_a_single_word():
    solution = middle_letter("i")

    assert solution == "i"

def test_returns_the_letters_of_a_two_letter_word():
    solution = middle_letter("it")

    assert solution == "it"

def test_returns_middle_letter_of_a_three_letter_word():
    solution = middle_letter("hit")

    assert solution == "i"

def test_returns_correct_letter_from_odd_string():
    solution = middle_letter("testing")

    assert solution == "t"

def test_returns_middle_two_letters_from_even_string():
    solution = middle_letter("middle")

    assert solution == "dd"