def no_of_primes(number):
    if number == 2:
        return True
    else:
        bool = False
        #this formula will check if a number is prime or not.
        if (math.pow(2, number) - 2) % number == 0:
            bool = True
        if bool == False:
            return False
        else:
            return True

def primeCount(n):
    prime_multiples = 1
    count = 0
    i = 2
    while prime_multiples <= n and i <= n:
        bool_if_prime = no_of_primes(i)
        if bool_if_prime == True:
            prime_multiples = prime_multiples * i
        if bool_if_prime == True:
            count = count + 1
        i = i + 1
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return count - 1

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = primeCount(n)
        print(result)
