from pwn import *
import sys

attempts = 1
password_file = 'rockyou.txt'
inserted_hash = sys.argv[1]



# How to use
usage_msg = "How to crack a hash:"'\n'+ sys.argv[0] +" -insert hash-"'\n'
if len(sys.argv) < 2:
    print(usage_msg)

# Checking the length of the sha256 hash is 64 digits
elif len(sys.argv[1]) < 64 or len(sys.argv[1]) != 64:
    print("Please insert a valid sha256 hash")
    exit()

# Using log.process from pwn module to create logs
with log.progress("Cracking hash [{}]\n".format(inserted_hash)) as progress:

    # Opening it as latin-1 as rockyou.txt contains legacy ASCII characters
    with open(password_file, "r", encoding = 'latin-1') as password_list:
        for password in password_list:
            password = password.strip('\n').encode('latin-1')

            #sha256sumhex is used to ensure password_hash is returned properly instead of a byte array
            password_hash = sha256sumhex(password)

            # Updating progress
            progress.status("Attempt [{}].\n {} \n ------------------- \n {}".format(attempts, password.decode("latin-1"), password_hash))
            if password_hash == inserted_hash:
                progress.success("Successful! on the attempt {}\n The hash {} matches the password '{}'".format(attempts, inserted_hash, password.decode("latin-1")))
                exit()
            attempts += 1
        progress.failure("Unable to crack {}".format(inserted_hash))
        exit()        






