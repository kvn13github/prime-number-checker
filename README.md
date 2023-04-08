# prime-number-checker
First it asks for a number, then says if it is a prime number and then what kind of special prime if so, and gives a quick description and field of use.

Output example:

*Enter a number greater than 0 to check for primes: 997
997 is a prime number.
997 is a Chen prime. A Chen prime is a prime number p such that p+2 is either a prime or a semiprime (the product of two primes). These primes have applications in number theory and cryptography.
Enter a number greater than 0 to check for primes: 89
89 is a prime number.
89 is a Sophie Germain prime. A Sophie Germain prime is a prime number p such that 2p + 1 is also a prime number. These primes are important in public-key cryptography, particularly in the generation of strong primes for use in RSA encryption.
89 is a Chen prime. A Chen prime is a prime number p such that p+2 is either a prime or a semiprime (the product of two primes). These primes have applications in number theory and cryptography.*


It works but not for very large numbers like this, it is a cullen prime, but my code doesnt recognize it as a prime: 

*Enter a number greater than 0 to check for primes: 4327026808213905342050800768897834255749702825971335854561344097468641739066470995883039328368346550230795011865072231993321873354682343477009643549350458900923391931374096250530395845111512030677507715986523126342188406582213595682945594166273
4327026808213905342050800768897834255749702825971335854561344097468641739066470995883039328368346550230795011865072231993321873354682343477009643549350458900923391931374096250530395845111512030677507715986523126342188406582213595682945594166273 is not a prime number. Try another?*

I can use different libraries for greater numbers, and I can still add more special prime number checks.
This code has lots of growth potential.
