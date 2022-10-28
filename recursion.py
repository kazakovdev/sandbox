# show all numbers from 100 to 0
import random


def countdown(number):
    print(number)
    if number > 0:
        countdown(number - 1)
    else:
        return None


# calc fibo numbers
def fibo(prev, curr, max=1000):
    if prev == 0:
        print(prev)
        print(curr)
    if prev + curr >= 1000:
        return None
    print(prev + curr)
    fibo(prev=curr, curr=curr + prev)


# is power of 2
def is_power_of_two(number):
    def devide(num, m=2):
        new = num / m
        if new == 1:
            print('OK')
            return None
        elif int(new) == new:
            devide(new, m)
            return None
        print('NO')

    devide(number, 2)


# sum of digits in long number
def sum_digits(num, sum=0):
    x = num % 10
    # print(num, sum, x)
    if num < 10:
        sum = sum + num
        return sum
    elif x == 0 and num >= 10:
        sum = sum_digits(num=num / 10, sum=sum)
    else:
        sum = sum_digits(num=num - x, sum=sum + x)
    return sum


def quicksort(list_):
    def partial_sort(l):
        if len(l) < 2:
            return l

        r = random.randint(0, len(l) - 1)
        left = [x for x in l[:r] + l[r + 1:] if x <= l[r]]
        right = [x for x in l[:r] + l[r + 1:] if x > l[r]]

        return partial_sort(left) + [l[r]] + partial_sort(right)

    sorted = partial_sort(list_)
    return sorted


if __name__ == "__main__":
    # print(quicksort([random.randint(-5000, 5000) for x in range(0, 20)]))

    class i():
        def __init__(x, y, z):
            print(y)
            print(z)


    a = i(2, 4)
