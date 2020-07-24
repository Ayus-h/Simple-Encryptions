from cryptography.fernet import Fernet

def create_key():
    key = Fernet.generate_key()

    with open("key.key","wb") as filename:
        filename.write(key)

def load_key():
    return open("key.key","rb").read()

def file_encryption(file):
    f = Fernet(load_key())

    file_data = open(file,"rb").read()
    encrypted = f.encrypt(file_data)

    with open(file,"wb") as filename:
        filename.write(encrypted)

def file_decryption(file):
    f = Fernet(load_key())

    file_data = open(file,"rb").read()
    decrypted = f.decrypt(file_data)

    with open(file,"wb") as filename:
        filename.write(decrypted)

#for 1st time, uncomment this:
#create_key()
file = r"C:\Users\Dell\Desktop\file encryption\encrypting files\files\Sample1000.csv"
#file_encryption(file)  #for encryption
#print("Hello, starting encryption..")
file_decryption(file) 





