"""
Template for part 1
Using substitution ciphers to encrypt and decrypt plain text
"""


# Part 1 - Use a dictionary that represents a substition cipher to 
# encrypt a phrase

# Example of a cipher dictionary 26 lower case letters plus the blank
CIPHER_DICT = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': ' ', 'w': 't'}

def encrypt(phrase, cipher_dict):
    """
    Take a string phrase (lower case plus blank) 
    and encypt it using the dictionary cipher_dict
    """
    encrypted_string=""
    for alpha in phrase:
        if alpha in cipher_dict:
            encrypted_string+=cipher_dict[alpha]
    return encrypted_string


# Tests
print("Output for part 1")
print(encrypt("pig", CIPHER_DICT))
print(encrypt("hello world", CIPHER_DICT))
print()

# Output for part 1
#vif
#hunnybtygnd



