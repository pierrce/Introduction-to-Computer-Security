# CS 642 University of Wisconsin
#
# usage: attack.py ciphertext
# Outputs a modified ciphertext and tag

import sys

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
"""AMOUNT: $  101.00
Originating Acct Holder: ACE
Orgininating Acct #82675-582370954

I authorized the above amount to be transferred to the account #78561-1848
held by a UW-Student at the National Bank of the Cayman Islands.
"""

# TODO: Modify the input so the transfer amount is more lucrative to
# the recipient
# each block is 16 bytes in AES, each character is 4 bytes: 4 chars/block



tag = hashlib.sha256(attackMessage).hexdigest()

# TODO: Print the new encrypted message
# print ciphertext.encode("hex") + tag.encode("hex")
print ciphertext.encode("hex") + tag