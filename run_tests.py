import tests


def run_all_tests():
    for i in dir(tests):
        item = getattr(tests, i)
        if callable(item):
            item()


if __name__ == '__main__':
    run_all_tests()
    print("All tests ran successfully")
