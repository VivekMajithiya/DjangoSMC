from Crypto.Cipher import AES

class Gatepass():
    nonce=b''
    tag=b''
    ciphertext=b''
    data=b''
    key=b''

    def get_key(self):
        file_in = open("media/utility/keyfile.bin", "rb")
        self.key = file_in.read()
        return self.key


    def get_mail_data(self,key=b''):
        file_in = open("media/utility/encrypted.bin", "rb")
        self.nonce, self.tag, self.ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
        file_in.close()
        # let's assume that the key is somehow available again
        cipher = AES.new(self.key, AES.MODE_EAX, self.nonce)
        self.data = cipher.decrypt_and_verify(self.ciphertext, self.tag)
        return self.data
