from positive_sum import positive_sum

def test_one():
    solution = positive_sum([1,2,3,4,5])

    assert solution == 15

def test_two():
    solution = positive_sum([1,2,3,4])

    assert solution == 10