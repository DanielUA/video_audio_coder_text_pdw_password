import pyAesCrypt
from pathlib import Path

password = input("Inser password: ")
data_path = Path("data.txt")
#encrypt
# pyAesCrypt.encryptFile(f"{data_path}", "data.txt.aes", password)

decrypt_path = Path("data.txt.aes")
#decrypt
pyAesCrypt.decryptFile(f"{decrypt_path}", "dataout.txt", password)
