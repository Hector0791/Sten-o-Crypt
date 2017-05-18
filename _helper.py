'''
This Python module contains auxiliary functions necessary for StenoCrypts execution
'''
import argparse                   # Parser for Command-Line Options 
import hashlib                    # Used for MD5 hashing 
import base64                     # Used for Encryption

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Processes Command Line Arguments ======================================================
def Parser():

    pars = argparse.ArgumentParser('StenoCrypt')
    
    exclude = pars.add_mutually_exclusive_group()
    exclude.add_argument('-s', '--stash',   action='store_true',  default=False, help="Initiates hiding process")
    exclude.add_argument('-u', '--unstash', action='store_true',  default=False, help="Initiates extraction process")
    
    theArgs = pars.parse_args()           

    return theArgs
# End of Parser ==========================================================================



# Creates an MD5 hash for input string =================================================
def Hash(password):
    
    m = hashlib.md5()
    m.update(password.encode())
    
    return m.hexdigest().upper()
# End of Hash ===========================================================================



# Retrieves the Message within the given text file ======================================
def retrieveMessage(filePath):
    
    tmp = open(filePath, 'r')
    fileContent = tmp.read()
    tmp.close()
    
    return fileContent
# End of retrieveMessage ================================================================



# Given a Password and Message, it returns and encrypted string =========================
def encryptor(password, message):
    
    salt = b"Group1"
    
    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length = 32,
        salt = salt,
        iterations = 100000,
        backend = default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    f = Fernet(key)
    
    encrypted = f.encrypt(message.encode())
    
    return encrypted.decode()
# End encryptor =========================================================================



# Given a Password and Encrypted Message, returns a decrypted string ====================
def decryptor(password, encrypted):
    
    salt = b"Group1"
    
    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length = 32,
        salt = salt,
        iterations = 100000,
        backend = default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    f = Fernet(key)
    
    decrypted = f.decrypt(encrypted.encode())
    
    return decrypted.decode()
# End of decryptor ======================================================================
