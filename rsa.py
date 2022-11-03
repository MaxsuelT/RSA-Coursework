
from primeNumberGenerator import primeNumberGen
from privateKeyGenerator import privateKeyGen


class RSA(primeNumberGen, privateKeyGen):
    
    def __init__(self, bitLength=20):
        super(RSA, self).__init__(bitLength)
        self.p, self.q = self.generatePrimeNumbers()
        self.modulusN = self.modulus()
        self.phi = self.eulerTotient()
        self.pubKey = 65537 
        self.privateKeyD = self.privateKeyGenerator() 

        
        
    def modulus(self):
        """n is the product of two large primes n = p * q"""
        
        return self.p * self.q

    def eulerTotient(self):
        """Euler's totient function (also called the Phi function) Phi, 
            known as φ(n), is then used to store a calculated value of Euler’s totient function for n. 
            This is done by doing p minus 1 and q minus 1, and multiplying the results.
        """
        return (self.p-1) * (self.q-1) 


    def encrypt(self,plainText):
        """Returns an encrypted message using c = m**e mod n
           Take iterate over each char in the plain Text, converts it to a number, 
           raise that char to the public key mod n. To return a string rather than a list
           concatenate the newly create string everytime it encounters a comma.   
        """
        msg= [pow(ord(char),self.pubKey, self.modulusN) for char in plainText]
        return ",".join([str(char) for char in msg ])
    
    def decrypt(self,cipherText):
        """
            Follows the Same approach above but in reverse.
            Returns an decrypted message using m = c**d mod n"""
        msg = [int(char) for char in cipherText.split(',')]
        decrypted = [pow(char, self.privateKeyD,self.modulusN) for char in msg]
        plainText = "".join([(chr(char)) for char in decrypted])
        return plainText
        

# rsa_ = RSA(20)
# # 
# # print('message\n', message)
# # print(rsa_.decrypt(message))
# print("modulus: ", rsa_.modulus())
# print(rsa_.eulerTotient())
# print(rsa_.p, rsa_.q)
# print(rsa_.privateKeyD)
# # print(type(rsa_.modulusN))

