from middle_letter import middle_letter

def test_returns_the_letter_of_a_single_word():
    solution = middle_letter("i")

    assert solution == "i"

def test_returns_the_letters_of_a_two_letter_word():
    solution = middle_letter("it")

    assert solution == "it"