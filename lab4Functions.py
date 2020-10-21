"""
MAT 2170: Lab 4

This module has the functions needed for lab 4

Written by: Andrew Mertz; modified by Peter Andrews and William Slough

Submitted by: Christobel Nweke
"""

import string


def letterToIndex(letter):
    """
    Given a letter, returns its distance from "a"; or -1 if the given string
    is not a letter. For example:
    letterToIndex("a") = letterToIndex("A")  =  0
    letterToIndex("b") = letterToIndex("B")  =  1
    letterToIndex("c") = letterToIndex("C")  =  2
    letterToIndex("#") = letterToIndex("AB") = -1

    Args:
        letter: the string to inspect, presumed to be a letter

    Returns:
        The distance of the letter to "a" or -1 if the string is not a letter
    """
    # Ensure the given string consists of exactly one character
    if len(letter) != 1:
        return -1

    # Convert the given character to its lower-case counterpart
    letter = letter.lower()

    # Determine the index of the given letter within "abc...z"
    return string.ascii_lowercase.find(letter)


def indexToLetter(index):
    """
    Given the value d, returns the letter which is d steps away from "a" or
    " " (space) if there is no such letter. For example:
    indexToLetter(0)  = "a"
    indexToLetter(1)  = "b"
    indexToLetter(2)  = "c"
    indexToLetter(-1) = " " (space)
    indexToLetter(26) = " " (space)

    Args:
        index: an integer

    Returns:
        The lower case letter with the given index or " " if index is out of
        bounds
    """
    # If the index is out of bounds return a space
    if index < 0 or index > 25:
        return " "

    # return the lower case letter with the given index
    return string.ascii_lowercase[index]


def scramble2Encrypt(plaintext):
    """
    Encrypts the given text using a two-rail fencepost (transposition) cipher.

    Args:
        plaintext: the string to be encrypted.

    Returns:
        the result of the encryption, i.e. the ciphertext
    """
    # Strings to hold the characters at even and odd positions of the plaintext
    evenChars = ""
    oddChars = ""

    # The position of the character currently being processed
    charCount = 0

    for ch in plaintext:
        # Even position?
        if charCount % 2 == 0:
            # Append the current character to the even-indexed characters
            evenChars = evenChars + ch
        # Odd position
        else:
            # Append the current character to the odd-indexed characters
            oddChars = oddChars + ch
        # Boost the character count
        charCount = charCount + 1

    # Return the ciphertext
    return oddChars + evenChars



def scramble2Decrypt(ciphertext):
    """
    Decrypts the given ciphertext assuming it has been encrypted using a
    two-rail fencepost (transposition) cipher.

    Args:
        ciphertext: the string to be decrypted.

    Returns:
        the result of the decryption, i.e. the plaintext
    """
    # Break the ciphertext into the even and odd parts
    halfLength = len(ciphertext) // 2
    evenChars = ciphertext[halfLength:]
    oddChars = ciphertext[:halfLength]

    # Merge the two halves into the plaintext
    plaintext = ""
    for index in range(halfLength):
        plaintext = plaintext + evenChars[index]
        plaintext = plaintext + oddChars[index]

    # Append any remaining even-indexed character to the plaintext
    if len(evenChars) > halfLength:
        plaintext = plaintext + evenChars[-1]

    return plaintext

def substitutionDecrypt(ciphertext, alphabet):
    """
        Decrypts the given plaintext with the given key using a substitution cipher

        Args:
            plaintext: the string to be encrypted, characters other than letters
                and spaces will be dropped
            key: a permutation of the lower case letters and space character to be
                used as a key

        Return:
            the result of the encryption, i.e. the ciphertext
        """
    # key that we will be finding the index values of
    key = "azsxdcfvgbhnjmklqwertyuiop "

    # plaintext variable with an empty string list stored inside it
    plaintext = ""
    # loop that goes through each word in the ciphertext. at the first run it goes like this
    # key.find(1). it then stores the value found at that position inside index.
    for letter in ciphertext:
        # Find where this letter is in the alphabet
        index = key.find(letter)

        # If it was found map it to the corresponding location in the key
        if index >= 0 and index < len(alphabet):
            plaintext = plaintext + alphabet[index]

    return plaintext

def substitutionEncrypt(plaintext, key):
    """
    Encrypt the given plaintext with the given key using a substitution cipher

    Args:
        plaintext: the string to be encrypted, characters other than letters
            and spaces will be dropped
        key: a permutation of the lower case letters and space character to be
            used as a key

    Return:
        the result of the encryption, i.e. the ciphertext
    """
    # The valid alphabet for the substitution cipher consists of the lower case
    # letters and the space.
    alphabet = string.ascii_lowercase + " "

    # Convert the plaintext to all lowercase letters
    plaintext = plaintext.lower()

    # for each letter in the plaintext convert it to the corresponding letter
    # in the key. If there is no such letter then skip it.
    ciphertext = ""
    for letter in plaintext:
        # Find where this letter is in the alphabet
        index = alphabet.find(letter)

        # If it was found map it to the corresponding location in the key
        if index >= 0 and index < len(key):
            ciphertext = ciphertext + key[index]

    return ciphertext


def removeDupes(s):
    """
    Removes all of the duplicate characters in the given string.

    Args:
        s: the string to be processed

    Returns:
        The given string with all duplicate characters removed
    """
    result = ""
    for character in s:
        if character not in result:
            result = result + character
    return result


def removeMatches(s, r):
    """
    Removes all of the characters in r from s.

    Args:
        s: the string characters are to be removed from
        r: the string of characters to be removed

    Returns:
        the string s with all of the characters from r removed
    """
    result = ""
    for character in s:
        if character not in r:
            result = result + character
    return result


def generateKeyFromPassword(passphrase):
    """
    Build a key for the substitution cipher from a passphrase.

    Args:
        passphrase: a string of letters to be used to generate the password.

    Returns:
        a key suitable for the substitution cipher, i.e. a
        permutation of the lower case letters with a trailing space character
    """
    alphabet = string.ascii_lowercase

     # Convert to lower case, as necessary
    passphrase = passphrase.lower()

    # Remove all of the duplicates from the passphrase
    passphrase = removeDupes(passphrase)


    # Make sure that the passphrase is not empty
    if len(passphrase) > 0:
        # Find the index of the last letter of the reduced passphrase in the
        # alphabet
        index = alphabet.find(passphrase[-1])
    else:
        # Otherwise return a key that will leave the plaintext unchanged
        return alphabet + " "

    # Split the alphabet into the parts that are before this index and after
    # this index
    before = alphabet[:index]
    after = alphabet[index + 1:]

    # Remove the letters found in the passphrase from the strings before and
    # after
    before = removeMatches(before, passphrase)
    after = removeMatches(after, passphrase)

    # Join the parts together to form the key
    return passphrase + after + before + " "


def vigenereLetter(plaintextLetter, keyLetter):
    """
    Computes a letter of ciphertext using the Vigenere cipher given a letter of
    the key and a letter of the plaintext.

    Args:
        plaintextLetter: a string of length one
        keyLetter: a string containing exactly one letter

    Returns:
        a letter of ciphertext
    """
    # Compute the index of each given letter
    keyIndex = letterToIndex(keyLetter)
    plaintextIndex = letterToIndex(plaintextLetter)

    # Compute the index of the ciphertext letter
    ciphertextIndex = (plaintextIndex + keyIndex) % 26

    # Return the ciphertext letter
    return indexToLetter(ciphertextIndex)


def keepMatches(s, k):
    """
    Keep only the letters in s that are also in k.

    Args:
        s: the string characters are to be removed from
        k: the string of characters to be kept

    Returns:
        the string s with only the characters that are also in k remaining
    """
    result = ""
    for character in s:
        if character in k:
            result = result + character
    return result


def vigenereEncrypt(plaintext, key):
    """
    Encrypt the given plaintext with the given key using a Vigenere cipher

    Args:
        plaintext: the string to be encrypted, only letters will be encrypted.
        key: a string of lower case letters

    Returns:
        the result of the encryption, i.e. the ciphertext
    """
    # Ensure letters in the plaintext and key are lowercase
    plaintext = plaintext.lower()
    key = key.lower()

    # Ensure the key contains only lower case letters
    key = keepMatches(key, string.ascii_lowercase)

    # If there is no key left return the plaintext unencrypted
    keyLength = len(key)
    if keyLength == 0:
        return plaintext

    # Encrypt each letter of plaintext. Note that we need the index of the
    # plaintext letter to compute the ciphertext letter.
    ciphertext = ""
    for index in range(len(plaintext)):
        # Get one character of plaintext
        plaintextCharacter = plaintext[index]

        # If the plaintext character is not a lower case letter, then it does
        # not need to be encrypted i.e. it can just be passed on to the
        # ciphertext.
        if plaintextCharacter not in string.ascii_lowercase:
            ciphertext = ciphertext + plaintextCharacter
        # Otherwise it needs to be encrypted
        else:
            keyLetter = key[index % keyLength]
            ciphertext = ciphertext + \
                         vigenereLetter(plaintextCharacter, keyLetter)

    return ciphertext



def scramble3Encrypt(plaintext):
    """
    Encrypts the given text using a Three-rail fencepost (transposition) cipher.

    Args:
        plaintext: the string to be encrypted.

    Returns:
        the result of the encryption, i.e. the ciphertext
    """

    # Strings to hold the characters at remainders of zeroes, ones and twos
    zeroes = ""
    ones = ""
    twos = ""

    # Range function that loops depending on how long the plaintext is
    # this function takes the initial char remainders and loops back to store the new values
    for i in range(len(plaintext)):

        if i % 3 == 0:
            zeroes = zeroes + plaintext[i]

        elif i % 3 == 1:
            ones = ones + plaintext[i]

        elif i % 3 == 2:
            twos = twos + plaintext[i]

        # Boost the character count
        cipherText = twos + ones + zeroes

    # Return the ciphertext
    return cipherText

def scramble3Decrypt(ciphertext):
    """
    Decrypts the given ciphertext assuming it has been encrypted using a
    three-rail fencepost (transposition) cipher.

    Args:
        ciphertext: the string to be decrypted.

    Returns:
        the result of the decryption, i.e. the plaintext
    """
    length = len(ciphertext)
    split = len(ciphertext) // 3
    dSplit = split + split
    twos = ciphertext[dSplit:]
    ones = ciphertext[split:dSplit:]
    zeroes = ciphertext[:split]


    plaintText = ""


    for i in range(split):
        if length % 3 == 0:
            plaintText = plaintText + twos[i]
            plaintText = plaintText + ones[i]
            plaintText = plaintText + zeroes[i]
        else:
            plaintText = plaintText + twos[i]
            plaintText = plaintText + ones[i]
            plaintText = plaintText + zeroes[i]


    if len(zeroes) < len(twos):
        plaintText = plaintText + twos[-1]


    return plaintText


def testSubstitutionDecrypt(ciphertext, alphabet):
    """
        prompts the user to enter a password which it then uses to give them the original plaintext

        Args:
            plaintext: the string to be encrypted, characters other than letters
                and spaces will be dropped
            key: a permutation of the lower case letters and space character to be
                used as a key

        Return:
            the result of the encryption, i.e. the ciphertext
        """
    # newkey that we will be finding the index values of but this time we're prompting the user for it
    passP = input("input password to obtain plaintext: ")
    newKey = (generateKeyFromPassword(passP))

    # plaintext variable with an empty string list stored inside it
    plaintext = ""
    # loop that goes through each word in the ciphertext. at the first run it goes like this
    # key.find(1). it then stores the value found at that position inside index.
    for letter in ciphertext:
        # Find where this letter is in the alphabet
        index = newKey.find(letter)

        # If it was found map it to the corresponding location in the key
        if index >= 0 and index < len(alphabet):
            plaintext = plaintext + alphabet[index]

    return plaintext
