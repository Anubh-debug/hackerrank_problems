'''this is the implementation of sieve to find prime numbers in a range in python'''
#take a list of range
range_primes = int(input("Enter the range of the given primes: "))
prime_list = []
for i in range(1, range_primes + 1):
    prime_list.append(1)
prime_list[1] = 0
prime_list[2] = 1
i = 2
while i * i <= range_primes:
    if prime_list[i] == 1:
        j = i * i
        while j <= range_primes - 1:
            prime_list[j] = 0
            j += i
    i += 1
for i in range(2, range_primes):
    if prime_list[i] == 1:
        print(i, end = ' ')
