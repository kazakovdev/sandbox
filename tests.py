import recursion

def recurison_test():
    assert recursion.sum_digits(100) == 1
    assert recursion.sum_digits(5) == 5
    assert recursion.sum_digits(40001) == 5
    assert recursion.sum_digits(367) == 16
    assert recursion.sum_digits(999) == 9*3
    print('SUCCESS')
    return True

def main():
    recurison_test()
    return None



if __name__ == '__main__':
    main()