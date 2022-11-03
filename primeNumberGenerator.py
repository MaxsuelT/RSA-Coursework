
import math
from random import randrange, randint
import numpy as np

class primeNumberGen:

    def __init__(self, bitLength=20):
        """Halving the bit-length to avoid overflow error"""
        self.bitLength = bitLength >> 1


    def randomNumber(self):
        """ Returns an odd number between bitLength-1 and bitLength
          Using leftwise operation in Python:This is the same as multiplying by 2**bitLength.
          The bitwise OR operator "|""  returns a 1 in each bit position for which the 
          corresponding bits of either or both operands are 1 s.     
        """   
        
        try: 
            if self.bitLength >= 10 and self.bitLength <=30:
                return randrange(1 << (self.bitLength-1) , 1 <<(self.bitLength+1)) | 1
        except TypeError:
            print (f' bit length {self.bitLength} is either too small or too large and it may break the code') 
            pass


    def isPrime(self,number):
        """
            Handles a few base cases: if number is less than 1 or number is 2 or 3
            If a number is even, in its binary representation it always end in zero
            Using bitwise operator &(and) if the last digit is zero then the number is even 
            and it should be False
            Every composite number has at least one prime factor less than or equal to square 
            root of itself[1]. Iterate in steps of two to ensure only odd numbers are considered.
        
        """

        if number < 1:
            return False
        if number == 2: 
            return True    
        if not number & 1: 
            return False
        
        for divisor in range(3, int(math.sqrt(number))+1, 2):
            if number % divisor == 0:
                return False
        return True


    def generatingPrimeCandidate(self):
        """Returns a number if it is prime"""
        primeCandidate = self.randomNumber()
        while not self.isPrime(primeCandidate):
            primeCandidate = self.randomNumber()
        return primeCandidate
            
            

    def generatePrimeNumbers(self):
        """Returns two prime number that will be used in RSA"""
        prime1 = self.generatingPrimeCandidate()
        prime2 = self.generatingPrimeCandidate()
        return prime1,prime2



number = primeNumberGen(30)
print(number.randomNumber())
print(len(bin(number.randomNumber())))
p,q = number.generatePrimeNumbers()
print(p)
print(len(bin(q)))
