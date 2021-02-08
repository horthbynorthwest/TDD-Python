from middle_letter import middle_letter

def test_returns_the_letter_of_a_single_word():
    solution = middle_letter("i")

    assert solution == "i"