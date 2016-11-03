# CS 642 University of Wisconsin
#
# usage: attack.py ciphertext
# Outputs a modified ciphertext and tag

import sys
import hashlib

def strxor(a, b):     
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


# Grab ciphertext from first argument
ciphertextWithTag = (sys.argv[1]).decode("hex")

if len(ciphertextWithTag) < 16+16+32:
  print "Ciphertext is too short!"
  sys.exit(0)

iv = ciphertextWithTag[:16]
ciphertext = ciphertextWithTag[:len(ciphertextWithTag)-32]
tag = ciphertextWithTag[len(ciphertextWithTag)-32:]

message = \
"""AMOUNT: $  101.00
Originating Acct Holder: ACE
Orgininating Acct #82675-582370954

I authorized the above amount to be transferred to the account #78561-1848
held by a UW-Student at the National Bank of the Cayman Islands.
"""

attackMessage = \
"""AMOUNT: $ 9999.00
Originating Acct Holder: ACE
Orgininating Acct #82675-582370954

I authorized the above amount to be transferred to the account #78561-1848
held by a UW-Student at the National Bank of the Cayman Islands.
"""
attack = "AMOUNT: $ 9999."

# TODO: Modify the input so the transfer amount is more lucrative to
# the recipient
# each block is 16 bytes in AES, each character is 4 bytes: 4 chars/block
#print ciphertextWithTag
#print len(ciphertextWithTag)

m1 = message[:16]
c2 = ciphertext[16:32]
#print "message = " + message[10:13]
#print "cryprt = " + attackMessage[10:13]

xor = strxor(attackMessage[:16], message[:16])
#xor = strxor(attackMessage[:16], c2)
#xor = strxor(xor, iv)
#print "xor = " + xor

ciphertext = "".join([xor,ciphertext[16:]])
#print len(ciphertext + tag)
#ciphertext.strip()

tag = hashlib.sha256(attackMessage).hexdigest()

# TODO: Print the new encrypted message
# print ciphertext.encode("hex") + tag.encode("hex")

print ciphertext.encode("hex") + tag