# EncryptTools (ENGLISH CHARACTER ONLY!!!)
# This version of the format supports numbers and capital letters and is case-sensitive

import random
from collections import namedtuple
from binascii import hexlify, unhexlify
from base64 import b64encode, b64decode
EncryptedNamedTuple = namedtuple('Encrypted', 'text, key')
char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
excp = ["'", '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+', '"', '<', '>', '/', '[', ']', '{', '}', '.', ',', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '?']

def encrypt(message):
    """
    Encrypts a message with a random key. Returns a Encrypted object.
    """
    err = True
    while err is True:
        try:
            count = 0
            enckey = _pdigitrand(len(message))
            split = list(message)
            enckey2 = list(str(enckey))
            enc = []
            for i in split:
                if not i in char and i not in excp:
                    raise ValueError("Characters must be in English only.")
                if i in excp:
                    enc.append(i)
                else:
                    l = char.index(i)
                    q = l + int(enckey2[count])
                    enc.append(char[q])
                count = count + 1
        except IndexError:
            err = True
        else:
            err = False
        if err == False:
            return Encrypted(''.join(enc), enckey)
        
def decrypt(encrypted):
    """
    Decrypts a Encrypted object returned by encrypt()
    """
    if not isinstance(encrypted, Encrypted):
        raise TypeError("'encrypted' must be an Encrypted object")
    enckey = encrypted.key
    count = 0
    split = list(encrypted.message)
    enckey2 = list(str(enckey))
    enc = []
    for i in split:
        if i in excp:
            enc.append(i)
        else:
            l = char.index(i)
            q = l - int(enckey2[count])
            enc.append(char[q])
        count = count + 1
    return ''.join(enc)

def decryptwithkey(message, key):
    """
    Decrypts with raw message and key.
    """
    enckey = key
    count = 0
    split = list(message)
    enckey2 = list(str(enckey))
    enc = []
    for i in split:
        if i in excp:
            enc.append(i)
        else:
            l = char.index(i)
            q = l - int(enckey2[count])
            enc.append(char[q])
        count = count + 1
    return ''.join(enc)

def encryptastuple(message):
    """
    Encrypts a message with a random key. Returns a namedtuple.
    """
    tmp = encrypt(message)
    return EncryptedNamedTuple(tmp.message, tmp.key)

def _pdigitrand(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)

def encrypt_to_bin(text, encoding='utf-8', errors='surrogatepass', formatted=False):
    """Encodes a message to binary.
    Attributes:
        text: The text to encode.
        encoding: The encoding to use in the encoding process.
        error: The error mode to use in the encoding process.
        formatted: Whether to format the encoded string or not."""
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    encoded = bits.zfill(8 * ((len(bits) + 7) // 8))
    if formatted == True:
        return ' '.join(encoded[i:i+8] for i in range(0,len(encoded),8))
    else:
        return encoded

def decrypt_from_bin(bits, encoding='utf-8', errors='surrogatepass'):
    """Decodes a message from binary.
    Attributes:
        text: The text to decode.
        encoding: The encoding to use in the decoding process."""
    bits = bits.replace(' ', '')
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def encrypt_to_hex(text, encoding='utf-8', formatted=False):
    """Encodes a message to hexadecimal.
    Attributes:
        text: The text to encode.
        encoding: The encoding to use in the encoding process.
        error: The error mode to use in the encoding process.
        formatted: Whether to format the encoded string or not."""
    encoded = hexlify(text.encode(encoding)).decode(encoding)
    if formatted == True:
        return ' '.join(encoded[i:i+2] for i in range(0,len(encoded),2))
    else:
        return encoded

def decrypt_from_hex(hx, encoding='utf-8'):
    """Decodes a message from hexadecimal.
    Attributes:
        text: The text to decode.
        encoding: The encoding to use in the decoding process."""
    hx = hx.replace(' ', '')
    return unhexlify(hx.encode(encoding)).decode(encoding)

def encrypt_to_base64(text, encoding='utf-8'):
    """Encodes a message to Base64.
    Attributes:
        text: The text to encode.
        encoding: The encoding to use in the encoding process.
        error: The error mode to use in the encoding process.
        formatted: Whether to format the encoded string or not."""
    return b64encode(text.encode(encoding)).decode(encoding)

def decrypt_from_base64(text, encoding='utf-8'):
    """Decodes a message from Base64.
    Attributes:
        text: The text to decode.
        encoding: The encoding to use in the decoding process."""
    return b64decode(text.encode(encoding)).decode(encoding)

class Encrypted(object):
    """Encrypted Object
    Attributes:
        message: The encrypted message.
        key: The decryption key."""
    def __init__(self, encrypted, key):
        self.message = encrypted
        self.key = key
    def __str__(self):
        return self.message
    

