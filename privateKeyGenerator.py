

import math
from random import randrange, randint
import numpy as np

class privateKeyGen:
    """ Generates a private key """

    # uncomment this constructor and comment the one below to to test this class
    # def __init__(self, pubKey, phi):
    #     self.pubKey = pubKey
    #     self.phi = phi
    
    def __init__(self):
        pass

    def tableGenerator(self):
        """Generates a 2x2 matrix"""
        return np.array([[self.phi,self.pubKey], [self.phi,1]], dtype=np.int64).T


    def privateKeyGenerator(self):
        """This function follows the method explained in this video: 
        https://www.youtube.com/watch?v=Z8M2BTscoD4&ab_channel=AnthonyVance
        Creates a matrix and while the bottom left value is not 1 do the follwing
        computations.
        If the bottom left value is 1, the bottom right value has the private key (d)
        This code works as long as the bit-length of the primes numbers are less than
        or equal to e
        
        """
        table = self.tableGenerator()
        try:
            while table[1][0] != 1:
#                 if np.all(table):
#                     pass
                division = table[0][0] // table[1][0]
                multLeft = table[1][0] * division
                multRight = table[1][1] * division
                newRow = np.array([multLeft, multRight])
                subTract = table[0] - newRow
                table = np.vstack((table, subTract))
                table = np.delete(table, 0, axis=0)  
                # if either bottomRight or bottomLeft value become negative,
                # compute the value mod phi until they are positive integers 
                while table[1][0] < 0:
                    table[1][0] = table[1][0] % self.phi
                while table[1][1] < 0:
                    table[1][1] = table[1][1] %  self.phi
        except RuntimeError:
            pass
         
        
        d = table[1][1]
        if self.privateKey(d):
            return int(d)   

    def privateKey(self,d):
        """Returns true if the condition is met"""
        return (self.pubKey * d) % self.phi == 1

# p,q = 59, 61
# e=31
# # n =
# phi = 3480

# a = privateKeyGen(e,phi)

# print(a.privateKeyGenerator())

