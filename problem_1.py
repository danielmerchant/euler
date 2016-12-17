"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""

sum = 0


def isDivisibleBy3or5(num):
    if (num % 3 == 0 or num % 5 == 0):
        return True
    else:
        return False


for i in range(1000):
    if isDivisibleBy3or5(i) == True:
        sum += i

print(sum)
