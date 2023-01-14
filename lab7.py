def isPrime(n):
    i = 2
    while n % i != 0:
        if i >= n ** 0.5:
            return True
        i += 1
    return False


n = int(input())

if isPrime(n) or n == 2:
    print('liczba jest liczbą pierwszą')
else:
    print('liczba nie jest liczbą pierwszą')
