items = ['a', 'b', 'c']


def bad_technique():
    for i, value in enumerate(items, start=1):
        print(f'{i}: {value}')


def good_technique():
    for i, value in enumerate(items):
        print(f'{i + 1}: {value}')


if __name__ == '__main__':
    # bad_technique()
    good_technique()
