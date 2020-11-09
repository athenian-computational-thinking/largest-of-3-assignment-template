from my_code import largest_num


def test_inc():
    assert 12 == largest_num(2, 12, 6)
    assert 17 == largest_num(17, 5, 17)
    assert 0 == largest_num(-3, -1, 0)
    assert 5 == largest_num(5, 2, 2)
    assert 7 == largest_num(2, 6, 7)
