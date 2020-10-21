"submitted by: Christobel Nweke"

import lab4Functions

#uses provided keys to encrpyt and decrpyt plain text
key = "azsxdcfvgbhnjmklqwertyuiop"
ex1 = (lab4Functions.substitutionEncrypt("hello", key))
ex2 = (lab4Functions.substitutionEncrypt("hi there", key))
print(ex1)
print(ex2)
cipher = ex1
cipher1 = ex2
key1 = "abcdefghijklmnopqrstuvwxyz"
print(lab4Functions.substitutionDecrypt(cipher,key1))
print(lab4Functions.substitutionDecrypt(cipher1,key1))

test = "zd etwd rk xwgmh oktw kyanrgmd"
print(lab4Functions.substitutionDecrypt(test, key1))

#asks for message to encrypt then prints the ciphertext and plaintext
encrypt = input("Type message to encrypt: ")
print(lab4Functions.substitutionEncrypt(encrypt,key))
print(lab4Functions.substitutionDecrypt(lab4Functions.substitutionEncrypt(encrypt,key),key1))


"This part of the code has variables plain and passP. Plain is just the plaintext that we want to encrypt and decrypt." \
"once the user has entered the plaintext they are then prompted to enter the password as well" \
"once they have entered the password the variable newKey generates a key from the given password the user provided" \
"in the definition we created a new variable for the decryption portion called testSubstitutionDecrypt. This version" \
"just prompts the user to once again enter the password they used in order to obtain the original plaintext copy."

plain = input("input plaintext: ")
passP = input("input password: ")
newKey = (lab4Functions.generateKeyFromPassword(passP))
print(lab4Functions.substitutionEncrypt(plain,newKey))
print(lab4Functions.testSubstitutionDecrypt(lab4Functions.substitutionEncrypt(plain,newKey), key1))





