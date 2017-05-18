import os                   # Standard Library OS functions
import _helper              # Helper Module to carry out auxiliary functions
from stegano import lsb     # Performs Steganographic Hiding


# Take user's Command Line Argument
arg = _helper.Parser()


# Execute Control Flow for Stashing Message
if arg.stash:

    # Obtain Image Path
    imagePath = input('Enter the complete path of Image to serve as carrier (Must be a PNG): ')
    while not os.path.isfile(imagePath):
        imagePath = input('The path you specified is not a file, try again: ')
    print()
     
    # Obtain Message Path
    filePath = input('Enter complete path of .txt file containing message: ')
    while not os.path.isfile(filePath):
        filePath = input('The path you specified is not a file, try again: ')
    print()
     
    # Obtain Password and Hash it
    password = input('Perfect, now enter your password (Note that only this password can extract message from now on): ')
    hashedpwd = _helper.Hash(password)
    print()
    
    
    # Retrieve Message and Encrypt it
    message = _helper.retrieveMessage(filePath)
    encryptedMessage = _helper.encryptor(password, message)
    
    
    # Store Hashed Password and Encrypted Message into Carrier
    fullInfo = hashedpwd + " " + encryptedMessage
    hidden = lsb.hide(imagePath, fullInfo)
    hidden.save(imagePath)
    
    
    print('Hiding Completed!!!')
    print('The Carrier has been overwritten with the Message. To view the message re-run this program with -u and supply password.')
    exit(0)



# Execute Control Flow for Unstashing Message
if arg.unstash:
    
    # Obtain Image Path
    imagePath = input('Enter the complete path of the Carrier (Must be a PNG): ')
    while not os.path.isfile(imagePath):
        imagePath = input('The path you specified is not a file, try again: ')
    print()
    
    # Obtain the Password
    password = input('Enter the password to unhide message: ')
    hashAttempt = _helper.Hash(password)
    print()
    
    # Extract Hidden Information from Carrier
    revealed = lsb.reveal(imagePath)
    tmp = revealed.split(' ', 1)
    hashed = tmp[0]
    encrypted = tmp[1]
    
    
    # Verify that password is correct
    if (hashed == hashAttempt):
        
        decrypted = _helper.decryptor(password, encrypted)
        print('Success!! Here is the Hidden Message:')
        print()
        print(decrypted)
        
    else:
        
        print('Password is Incorrect... Good Bye')
    
    exit(0)
    