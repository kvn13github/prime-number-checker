import math

""" This script includes functions to check for several types of special primes:

- Safe primes: a prime number of the form p = 2q + 1, where q is also a prime number. Safe primes are important in public-key cryptography, such as Diffie-Hellman key exchange and ElGamal encryption.
- Sophie Germain primes: a prime number p such that 2p + 1 is also a prime number. These primes are important in public-key cryptography, particularly in the generation of strong primes for use in RSA encryption.
- Fermat primes: a prime number of the form 2^(2^k) + 1. These primes are important in number theory and have been used in pseudorandom number generation.
- Cullen primes: a prime number of the form n = k*2^k + 1. These primes have applications in the theory of Fermat numbers and the search for large prime numbers.
- Factorial primes: a prime number that is one more than the factorial of some positive integer. There are only a few known factorial primes, and they become increasingly rare as n increases. They have applications in number theory and combinatorics.
- Mersenne primes: a prime number of the form 2^p - 1, where p is also a prime number. These primes have been used in pseudorandom number generation and in the discovery of large prime numbers.
-  and more ...
The script prompts the user to input a number, checks if it is prime, and then checks if it is any of the special primes listed above. If the number is a special prime, the script outputs an explanation of what makes it special and its practical uses in encryption or other fields. If the number is not prime, the script simply outputs a message stating that the number is not prime.
 """



def input_number():
    n = int(input("Enter a number greater than 0 to check for primes: "));
    return n

#n = input_number()

def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num < 2 or num % 2 == 0:
        return False
    if num < 9:
        return True
    if num % 3 == 0:
        return False
    r = math.floor(math.sqrt(num))
    f = 5
    while f <= r:
        if num % f == 0:
            return False
        if num % (f + 2) == 0:
            return False
        f += 6
    return True

def is_safe_prime(num):
    if not is_prime(num):
        return False
    return is_prime((num-1)//2)

def is_sophie_germain_prime(num):
    if not is_prime(num):
        return False
    return is_prime(2*num + 1)

def is_fermat_prime(num):
    k = 0
    while 2**(2**k) + 1 <= num:
        if num == 2**(2**k) + 1:
            return True
        k += 1
    return False

def is_cullen_prime(num):
    k = 1
    while k < num:
        if num == k * 2**k + 1:
            return True
        k += 1
    return False

def is_factorial_prime(num):
    k = 2
    while math.factorial(k) < num:
        k += 1
    return math.factorial(k) == num

def is_mersenne_prime(num):
    k = 1
    while 2**k - 1 <= num:
        if num == 2**k - 1 and is_prime(k):
            return True
        k += 1
    return False

def is_wieferich_prime(num):
    if not is_prime(num):
        return False
    if num == 2:
        return True
    return pow(2, num-1, num*num) == 1

def is_brocard_prime(num):
    if not is_prime(num):
        return False
    for k in range(1, num):
        if math.factorial(k) + 1 == num:
            return True
        elif math.factorial(k) + 1 > num:
            return False
    return False

def is_chen_prime(num):
    if not is_prime(num):
        return False
    if is_prime(num+2):
        return True
    for i in range(2, num):
        if is_prime(i) and is_prime((num+2)//i):
            return True
    return False

def is_emirp(num):
    if not is_prime(num):
        return False
    n_rev = int(str(num)[::-1])
    if num == n_rev:
        return False
    return is_prime(n_rev)


# keep asking for input until the user enters a non-positive number
while True:
    while True:
        n2 = input_number()
        if n2 <= 0:
            break
        if is_prime(n2):
            print(f"{n2} is a prime number.")
            if is_safe_prime(n2):
                print(f"{n2} is a safe prime. A safe prime is a prime number of the form p = 2q + 1, where q is also a prime number. Safe primes are important in public-key cryptography, such as Diffie-Hellman key exchange and ElGamal encryption.")
            if is_sophie_germain_prime(n2):
                print(f"{n2} is a Sophie Germain prime. A Sophie Germain prime is a prime number p such that 2p + 1 is also a prime number. These primes are important in public-key cryptography, particularly in the generation of strong primes for use in RSA encryption.")
            if is_fermat_prime(n2):
                print(f"{n2} is a Fermat prime. A Fermat prime is a prime number of the form 2^(2^k) + 1. These primes are important in number theory and have been used in pseudorandom number generation.")
            if is_cullen_prime(n2):
                print(f"{n2} is a Cullen prime. A Cullen prime is a prime number of the form n = k*2^k + 1. These primes have applications in the theory of Fermat numbers and the search for large prime numbers.")
            if is_factorial_prime(n2):
                print(f"{n2} is a factorial prime. A factorial prime is a prime number that is one more than the factorial of some positive integer. There are only a few known factorial primes, and they become increasingly rare as n increases. They have applications in number theory and combinatorics.")
            if is_mersenne_prime(n2):
                print(f"{n2} is a Mersenne prime. A Mersenne prime is a prime number of the form 2^p - 1, where p is also a prime number. These primes have been used in pseudorandom number generation and in the discovery of large prime numbers.")
            if is_wieferich_prime(n2):
                print(f"{n2} is a Wieferich prime. A Wieferich prime is a prime number p such that 2^(p-1) mod p^2 = 1. These primes are extremely rare, with only two known examples, and have applications in number theory and cryptography.")
            if is_brocard_prime(n2):
                print(f"{n2} is a Brocard prime. A Brocard prime is a prime number p such that there exists an integer k satisfying the equation k! + 1 = p. These primes are rare and have applications in number theory and combinatorics.")
            if is_chen_prime(n2):
                print(f"{n2} is a Chen prime. A Chen prime is a prime number p such that p+2 is either a prime or a semiprime (the product of two primes). These primes have applications in number theory and cryptography.")
            if is_emirp(n2):
                print(f"{n2} is an emirp. An emirp is a prime number that, when its digits are reversed, forms a different prime number. These primes have applications in recreational mathematics and number theory.")
            break
        else:
            print(f"{n2} is not a prime number. Try another?")
    else:
        print("Want to try another?")
        #continue
   