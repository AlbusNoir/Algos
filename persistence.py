'''The function takes a positive integer and returns its multiplicative persistence
Multiplicative persistence is the number of times you have to multiply  the digits in an integer until you reach a
single digit
Example: n = 39, 3*9 = 27, 2*7 = 14, 1*4 = 4, the count is 3
'''

def find_persistence(n):
    count  = 0

    while not n < 10:
        product = 1
        for i in list(str(n)):
            product *= int(i)
        count += 1
        n = product

    return count

num = int(input('Enter an integer: '))
count = find_persistence(num)

print(f'The persistence of {num} is {count}')