from positive_sum import positive_sum

def test_one():
    solution = positive_sum([1,2,3,4,5])

    assert solution == 15

def test_two():
    solution = positive_sum([1,2,3,4])

    assert solution == 10

def test_three():
    solution = positive_sum([1,-2,3,4,5])

    assert solution == 13

def test_four():
    solution = positive_sum([])

    assert solution == 0

def test_five():
    solution = positive_sum([-1,-2,-3,-4,-5])

    assert solution == 0 