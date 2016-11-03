
import sys
import os
import Crypto.Cipher.AES
import hashlib

message = \
"""AMOUNT: $  101.00
Originating Acct Holder: ACE
Orgininating Acct #82675-582370954

I authorized the above amount to be transferred to the account #78561-1848
held by a UW-Student at the National Bank of the Cayman Islands.
"""

def baddecrypt(inthing, keyfile ):
    f = open( keyfile, 'r' )
    key = f.readline()
    key = key[:32].decode("hex")
    f.close()

    # Grab ciphertext from first argument
    print sys.argv.count()
    ciphertextWithTag = inthing.decode("hex")

    if len(ciphertextWithTag) < 16+16+32:
      print "Ciphertext is too short!"
      sys.exit(0)

    iv = ciphertextWithTag[:16]
    ciphertext = ciphertextWithTag[:len(ciphertextWithTag)-32]
    tag = ciphertextWithTag[len(ciphertextWithTag)-32:]
    cipher = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CBC, IV=iv )
    plaintext = cipher.decrypt( ciphertext[16:] )

    # Check the tag
    if tag.encode("hex") != hashlib.sha256(plaintext).hexdigest():
       print "Invalid tag!"
    else:
       print "Verified message:"
       print plaintext

    f = open(sys.argv[1], 'r')
    key = f.readline()
    key = key[:32].decode("hex")
    f.close()

    message = \
    """AMOUNT: $  101.00
    Originating Acct Holder: ACE
    Orgininating Acct #82675-582370954

    I authorized the above amount to be transferred to the account #78561-1848
    held by a UW-Student at the National Bank of the Cayman Islands.
    """

    iv = os.urandom(16)
    cipher = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CBC, IV=iv)
    ciphertext = cipher.encrypt(message).encode("hex")
    tag = hashlib.sha256(message).hexdigest()
    # print iv.encode("hex")
    # print ciphertext
    # print tag
    print iv.encode("hex") + ciphertext + tag


def badencrypt(file):
    f = open(file, 'r')
    key = f.readline()
    key = key[:32].decode("hex")
    f.close()


    iv = os.urandom(16)
    cipher = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CBC, IV=iv)
    print "message = %s" %message
    ciphertext = cipher.encrypt(message).encode("hex")
    tag = hashlib.sha256(message).hexdigest()
    # print iv.encode("hex")
    # print ciphertext
    # print tag
    print iv.encode("hex") + ciphertext + tag
    return iv.encode("hex") + ciphertext + tag



