"""This is the main file"""



from rsa import RSA
from Charlie import CharlieTheHacker
import time


intro = """
************************************************************
*   Computer Security Coursework by Maxsuel Trajano        *                                     
************************************************************

"""


welcome = """
************************************************************
*                                                          *
*                    RSA Encryption                        *
*                                                          *
************************************************************
************************************************************
*      Alice          Charlie          Bob                 *
************************************************************
************************************************************
*   Alice wants to send a message to Bob.                  *
*   She decides to use RSA cryptosystem.                   *  
*   She knows she needs to share her public keys(e,n)      *
*   She decides to create the public key (n) by herself    *
*  to do that she needs two large primes (p,q)             *
************************************************************

"""


rsa_ = RSA(20)
print(intro)
# for presentation purposes. This can be safely removed.
time.sleep(1.5)
print(welcome)
print('P and Q are  randomly generated prime numbers')
print('P: ',rsa_.p, ' Q: ', rsa_.q)
print('\nModulus = P * Q')
print('Modulus (n): ', rsa_.modulusN)

sharingKeys = """
************************************************************
*  Alice wants to compute RSA exponent (e) but she         *
*  finds out that the industry standard for (e) is 65537   *
*  Alice makes her public keys (e,n)available              *
************************************************************
"""

print(sharingKeys)

pubKey = rsa_.pubKey
modN = rsa_.modulus()
print(f'Public keys: e({pubKey}) and n({modN})',)


AliceMessageB = """
************************************************************
*  Alice questions herself: What was the message again?     *                                             
************************************************************

"""
print(AliceMessageB)

while True:
	msg = input('What is the message: ')
	if msg == "" or msg == " ":
		print('\nI dont think that is what I wanted to say\n')
				
	else:
		encryptedMessage = rsa_.encrypt(msg)
		break
		





AliceMessageA = """
************************************************************
*     Alice sends the encrypted message to Bob             *                                             
************************************************************

"""
print(AliceMessageA)


print('Encrypted Message: \n', encryptedMessage)
# for presentation purposes. This can be safely removed.
time.sleep(1.5)
Bob = """
************************************************************
*  After some time, Bob receives the message, uses his     *
*  private key (d) to decrypt the message, and reads it.   *
************************************************************

"""
print(Bob)
print("Bob's private key: ", rsa_.privateKeyD)
print("Bob decrypts the message: ",rsa_.decrypt(encryptedMessage))


# for presentation purposes. This can be safely removed.
time.sleep(0.5)

CharlieDecrypts = """
************************************************************
*                                                          *
*  Unbeknown to Alice, Charlie had been 'listening' and    *
*  he had intercepted Alice's cipher text, and the         *
*  public keys (e,n)                                       *
*                                                          *
*  Charlie is very keen to find out what the message is.   *
*  He sees that the public key (n) is small and he knows   *
*  he can use prime factorization to find the factors      *
*  of (n) and with that, he can easily decrypt the message *                                           
************************************************************

"""

print(CharlieDecrypts)
chTheHacker = CharlieTheHacker(encryptedMessage, pubKey, modN)



print(f"Charlie gets hold of the cipher text: {encryptedMessage} \
\n\nand The public key: {pubKey} and the modulus: {modN} ")


print('\nCharlie then proceeds to get the: ')
print("Prime factorization of the public key (n): ", chTheHacker.primeFactorization(modN))
print("Phi(n) : ", chTheHacker.eulerTotientCharlie())
print("Private key (d): ", chTheHacker.charliePrivateKey())
print("Charlie successfully decrypts the Message: ", chTheHacker.charlieDecrypt(), "\n")



end = """
************************************************************
*                    THE END                               *                                           
************************************************************

"""
