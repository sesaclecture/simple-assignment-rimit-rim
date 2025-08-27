import test

def test_name_type():
    assert isinstance(test.name, str)

def test_age_type():
    assert isinstance(test.age, int)

def test_numbers_type():
    assert 2 in test.numbers
    assert len(test.numbers) == 3

def test_is_student_type():
    assert test.is_student is True