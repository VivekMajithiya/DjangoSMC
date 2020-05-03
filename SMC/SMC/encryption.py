from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

mailcontent="Alert from Pythonworld:Action required on app alert:pythonworldiscool@gmail.com:vmpk2001@gmail.com:Sallumajju@123"

key = get_random_bytes(16)
print(key)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(mailcontent.encode())

file_out = open("encrypted.bin", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
file_out.close()

file_outkey = open("keyfile.bin","wb")
file_outkey.write(key)
file_outkey.close()
