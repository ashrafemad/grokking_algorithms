from algorithms.binary_search import binary_search


def test_binary_search_high_success():
    assert binary_search([1, 2, 3, 4, 5], 4) == 3, "Should be index 3"


def test_binary_search_low_success():
    assert binary_search([1, 2, 3, 4, 5], 1) == 0, "Should be index 0"


def test_binary_search_failed_to_find():
    assert binary_search([1, 2, 3, 4, 5], 6) is None, "Should be None"
