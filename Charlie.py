import math
from privateKeyGenerator import privateKeyGen



class CharlieTheHacker(privateKeyGen):
    """To avoid code repetions, some methods have been inherited from shared super classes,
       though, to keep it simply and avoid errors, some methods have been copied to this class e.g. isPrime
    """

    def __init__(self, cipherText, publicKey, modulusN):
        super(CharlieTheHacker, self).__init__()
        self.cipherText = cipherText
        self.pubKey = publicKey
        self.modulusN = modulusN
        

    def isPrime(self, number):
        """Charlie's 'version' of isPrime """

        if number <= 1:
            return False
        if number == 2: 
            return True    
        if not number & 1: 
            return False
        
        for divisor in range(3, int(math.sqrt(number))+1, 2):
            if number % divisor == 0:
                return False
        return True


    def generateNPrimes(self, numberPrimes=100000):
        """Generate N prime numbers"""
        return [prime for prime in range(numberPrimes) if self.isPrime(prime)]

    def primeFactorization(self, modulusN):
        """ Naive Prime factorization: Finding the prime factors of a given number. 
            If the number is not prime and it is even: Repeatedly divide  even number until 
            is odd. Once the number is odd: if the number mod the primes is 0
            that means they are factors.
            The code for this section is inspired by this author: 
            https://paulrohan.medium.com/prime-factorization-of-a-number-in-python-and-why-we-check-upto-the-square-root-of-the-number-111de56541f 
        
        """
        primeFactorization = []
        primeNumbersList = self.generateNPrimes()
        
        if not self.isPrime(modulusN):
            while modulusN % 2 == 0:
                modulusN >>= 1
                
            for divisor in primeNumbersList:
                while modulusN % divisor == 0:
                    primeFactorization.append(divisor)
                    modulusN /= divisor

            return primeFactorization
        return f'The number {modulusN} is Prime'

    def eulerTotientCharlie(self):
        p,q = self.primeFactorization(self.modulusN)
        return (p-1) * (q-1)

    def charliePrivateKey(self):
        self.phi = self.eulerTotientCharlie()
        return self.privateKeyGenerator()



    def charlieDecrypt(self):
        """Returns an decrypted message using m = c**d mod n"""
        pk = self.charliePrivateKey()
        
        msg = [int(char) for char in self.cipherText.split(',')]

        decrypted = [pow(char, pk, self.modulusN) for char in msg]
        # return decrypted
        plainText = "".join([(chr(char)) for char in decrypted])
        return plainText



            
# hacker = CharlieTheHacker('914939,1841225,1615633,1615633,411588,2097881,2173800,742322,1841225,953087,1841225,\
#     2097881,742322,411588,767771,2097881,1813893,953087,1841225,2097881,1122267,411588,2253382,2097881,1243396,\
#     411588,1829339,1099163,1096313,1056910',65537, 2436829)

# # print(hacker.generateNPrimes())

# print(hacker.primeFactorization(2436829))
# print(hacker.eulerTotientCharlie())
# print(hacker.charliePrivateKey())
# print(hacker.charlieDecrypt())

    