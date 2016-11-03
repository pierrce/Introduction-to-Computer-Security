# CS 642: Computer Security - Homework Three

This homework assignment covers topics in cryptography. You must work with a partner. There are two parts labeled A and B and one extra credit part described at the end of this document.

It is due **April 18, 2016** by 11:59 PM local time. 

## Part A: Password Cracking

A colleague has built a password hashing mechanism. It applies SHA-256 to a string of the form `username,password,salt` where `salt` is a randomly chosen value. For example, the stored value for username `user` and password `12345` and salt `999999` is 
`c50603be4fedef7a260ef9181a605c27d44fe0f37b3a8c7e8dbe63b9515b8e96`.

For example, the Python code to generate this is:
```
import hashlib;
print hashlib.sha256("user,12345,999999").hexdigest();
```

The same process was used to generate the challenge hash 
`83c02558e533b6051e6d40e84bd03d19193b7090fa016b9b247f86d129d5f608` 
for user `ace` and salt `8593018378`.

* Recover the password used to generate the challenge hash above. *Hint:* The password consists only of numbers.
* Give a pseudocode description of your algorithm and the worst case running time for it.
* Discuss the merits of your colleague’s proposal. Suggest how your attack might be made intractable.
* Put your solutions in the file `solutions.txt`.


## Part B: Encryption

Another colleague decided to build a symmetric encryption scheme. These are implemented in `badencrypt.py` and `baddecrypt.py` and are designed to encrypt a sample message to demonstrate the encryption scheme. To use these demo programs, run:
```
CT=$(python badencrypt.py testkeyfile)
echo $CT
python baddecrypt.py testkeyfile $CT
```

Your job is to assess the security of this encryption scheme. Your solution will be a Python program `attack.py` that takes as input a ciphertext and modifies the ciphertext so that the decrypted message has a different (and more lucrative to the recipient) `AMOUNT` field and still passes the verification in `baddecrypt.py`. `attack.py` must do this without access to the keyfile or knowledge of the key. You can assume the ciphertext contains the sample message hardcoded in `badencrypt.py`.

We will test your solution with original versions of `badencrypt.py` and `baddecrypt.py` and with different encryption keys than the test key provided. To ensure that `attack.py` produces the correct formatted output, you can run from the command line:
```
CT=$(python badencrypt.py testkeyfile)
MODCT=$(python attack.py $CT)
python baddecrypt.py testkeyfile $MODCT
```

In `solutions.txt`, describe what is wrong with your colleague's scheme and how it should be fixed so that it will be more secure.

Your attack script will not have direct access to the key file and should not attempt to gain access to the process memory of baddecrypt or any other files to steal the key directly.

## Deliverables
Put the files `attack.py` and `solutions.txt` into a tarball with the following command (where UWID1/2 are your group members' UWID #s):
```
tar -cf UWID1_UWID2_hw3.tar attack.py solutions.txt
```

Upload `UWID1_UWID2_hw3.tar` to the hw-3 folder on the Desire2Learn website for this course:
https://uwmad.courses.wisconsin.edu/d2l/home/3199130

Use Assignments > Dropbox to find the hw-3 submission folder.
exc3dazk
## Grading
Parts A and B are worth up to 5 points for a total of 10 points for this assignment. The extra credit below is worth up to 2 additional points.

## Collaboration Policy
You are encouraged to use the internet, the Piazza discussion board for this class, and classmates for information about tools and setup. Please help your fellow classmates with setup and understanding Python, but don't discuss solution specifics with anyone beyond your project partner.


## Extra credit: More password cracking

The input `ace,password,2953983556` processed with SHA256 iterated 256 times produces the hash 
`1f449b8b05967da7b3c069012174d587e788a8ecd20a5d6a62746c9ed9a2d6d1`. For the username `ldecarli` with salt `0556927495` the challenge hash is 
`f6bf5d2b5a7c85e2bcf4d183fc7ba9db335cf6f177913328c43cf85123f1b18c`.

Find the password used to produce the challenge hash. Submit the code you used to solve the hash and add to `solutions.txt` the correct password a description of how you found the correct password.

