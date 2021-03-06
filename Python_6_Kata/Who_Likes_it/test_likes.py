from likes import likes

def test_returns_a_single_name_likes():
    solution = likes(["Peter"])

    assert solution == "Peter likes this"

def test_returns_a_different_single_name():
    solution = likes(["Bob"])
    assert solution == "Bob likes this"

def test_returns_two_name_likes():
    solution = likes(['Jacob', 'Alex'])
    assert solution == 'Jacob and Alex like this'

def test_returns_three_name_likes():
    solution = likes(['Max', 'John', 'Mark'])
    assert solution == 'Max, John and Mark like this'

def test_returns_4_names_likes():
    solution = likes(['Alex', 'Jacob', 'Mark', 'Max'])
    assert solution == 'Alex, Jacob and 2 others like this'

def test_can_handle_an_empty_list():
    solution = likes([])
    assert solution == "no one likes this"