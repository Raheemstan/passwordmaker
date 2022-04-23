#!/usr/bin/env python3
"""
Designed By:    ph03n!X
Date:           20 April, 2022
Version:        1.0
"""

import random
import csv
from cryptography.fernet import Fernet


def read(name, op):
    with open(name, op) as file:
        plain = file.read()
    return plain


def write(name, op, filed):
    with open(name, op) as file:
        plain = file.write(filed)
    return plain


def encrypt():
    try:
        print("Decrypting password file!")
        decrypt()
    except:
        print("Password file is plain text!")
    finally:
        # start of key creation
        # writing key
        keycode = Fernet.generate_key()
        write('filekey.key', 'wb', keycode)
        # end

        # file encryption
        key = read('filekey.key', 'rb')
        fernet = Fernet(key)
        original = read('passwrd.csv', 'rb')
        encryption = fernet.encrypt(original)
        write('passwrd.csv', 'wb', encryption)


def decrypt():
    # reading files
    key = read('filekey.key', 'rb')
    pfile = read('passwrd.csv', 'rb')
    # using generated key
    fernet = Fernet(key)
    decrypt = fernet.decrypt(pfile)
    write('passwrd.csv', 'wb', decrypt)


def newpass():
    try:
        print("Decrypting password file!")
        decrypt()
    except:
        print("Password file is plain text!")
    finally:
        # File containing passwords.
        pass_file = open("passwrd.csv", "a", encoding="UTF8", newline="")

        # password characters
        alphanum = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()<>"
        # number of characters for password
        n = 16

        app = input("Enter name of site: ")
        uname = input("Enter Username: ")

        # writing to file
        writer = csv.writer(pass_file)
        password = "".join(random.sample(alphanum, n))
        data = [app, uname, password]
        writer.writerow(data)
        pass_file.close()
        print("Your new password is: " + password)
    encrypt()


def help():
    print("Usage: \n"
          "1        for new encryption key \n"
          "2        for decrypt password \n"
          "0        for new password \n"
          "help     to print this menu")


print("***************************                  ********                        ********\n"
       "*********************************            ***********                  ***********\n"
       "***********            ***********           **************            **************\n"
       "***********              ***********         *****************      *****************\n"
       "***********              ***********         **********   ***************   *********\n"
       "***********             ***********          **********      *********      *********\n"
       "***********           ***********            **********         ***         *********\n"
       "*****************************                **********          *          *********\n"
       "***************************                  **********                     *********\n"
       "********             ********                **********                     *********\n"
       "********             *********               **********                     *********\n"
       "********             **********              **********                     *********\n"
       "********             ***********             **********                     *********\n"
       "                                             Designed By: \n"
       "                                                ph03n!X   \n"
       )
help()
while True:
    var = input("Enter command: ")

    if var == '1':
        encrypt()
        print("Encryption successful !!!")
        break
    elif var == '2':
        decrypt()
        print("Decryption successful !!!")
        break
    elif var == '0':
        newpass()
        print("Password Generation successful !!!")
        break
    elif var == 'help':
        help()
    else:
        print("Invalid input")
        help()
