from likes import likes

def test_returns_a_single_name_likes():
    solution = likes(["Peter"])

    assert solution == "Peter likes this"

def test_returns_a_different_single_name():
    solution = likes(["Bob"])
    assert solution == "Bob likes this"