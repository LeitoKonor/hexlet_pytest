from hexlet_pytest.example import reverse, sum, get_range


def test_reverse():
    assert reverse('Hexlet') == 'telxeH'

def test_reverse_for_empty_string():
    assert reverse('') == ''


def test_sum():
    assert sum(5, 4) == 9


def test_get_range():
    assert get_range(5) == [0, 1, 2, 3, 4]
    assert get_range(0) == []
    assert get_range(-5) == []


def test_stack():
    stack = []
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'
    assert stack.pop() == 'one'
