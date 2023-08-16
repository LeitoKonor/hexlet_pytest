def reverse(string):
    return string[::-1]


def sum(x, y):
    return x + y


def get_range(num):
    if num > 0:
        return list(range(num))
    else:
        return []
print(get_range(5))
