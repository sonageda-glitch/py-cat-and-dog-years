from app.main import get_human_age


def test_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_cat_before_first_human_year() -> None:
    assert get_human_age(14, 0)[0] == 0


def test_dog_before_first_human_year() -> None:
    assert get_human_age(0, 14)[1] == 0


def test_cat_first_human_year() -> None:
    assert get_human_age(15, 0)[0] == 1


def test_dog_first_human_year() -> None:
    assert get_human_age(0, 15)[1] == 1


def test_cat_before_second_human_year() -> None:
    assert get_human_age(23, 0)[0] == 1


def test_dog_before_second_human_year() -> None:
    assert get_human_age(0, 23)[1] == 1


def test_cat_second_human_year() -> None:
    assert get_human_age(24, 0)[0] == 2


def test_dog_second_human_year() -> None:
    assert get_human_age(0, 24)[1] == 2


def test_cat_third_human_year() -> None:
    assert get_human_age(28, 0)[0] == 3


def test_dog_third_human_year() -> None:
    assert get_human_age(0, 29)[1] == 3


def test_cat_fourth_human_year() -> None:
    assert get_human_age(32, 0)[0] == 4


def test_dog_fourth_human_year() -> None:
    assert get_human_age(0, 34)[1] == 4


def test_cat_and_dog_use_different_intervals() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]
