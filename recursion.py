#show all numbers from 100 to 0
def countdown(number):
    print(number)
    if number > 0:
        countdown(number-1)
    else:
        return None

#calc fibo numbers
def fibo(prev, curr, max = 1000):
    if prev == 0:
        print(prev)
        print(curr)
    if prev + curr >= 1000:
        return None
    print(prev + curr)
    fibo(prev = curr, curr = curr + prev)

#is power of 2
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


#sum of digits in long number
def sum_digits(num, sum=0):
    x = num % 10
    #print(num, sum, x)
    if num < 10:
        sum = sum + num
        return sum
    elif x == 0 and num >= 10:
        sum = sum_digits(num = num / 10, sum = sum)
    else:
        sum = sum_digits(num = num - x, sum = sum + x)
    return sum

if __name__ == "__main__":
    print(sum_digits(925))