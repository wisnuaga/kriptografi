class Vigenere:
    _start_char = 65
    _length_of_char = 26
    _end_char = 90

    def __init__(self, message, key):
        self.message = message.upper()
        self.key = key.upper()
        self.msg_len = len(message)
        self.key_len = len(key)

    #hapus karakter selain (A s/d Z)
    def __remover(self, char):
        return (ord(char) >= self._start_char) and (ord(char) <= self._end_char)

    def encrypt(self):
        e_msg = ""
        for i in range(self.msg_len):
            if (self.__remover(self.message[i])):
                key_cipher = (self.key[i % self.key_len])
                msg_ntrl = (ord(self.message[i]) - self._start_char)
                key_ntrl = (ord(key_cipher) - self._start_char)
                value = (msg_ntrl + key_ntrl) % self._length_of_char
                e_msg += chr(value + self._start_char)
            else:
                e_msg += self.message[i]
        return e_msg

    def decrypt(self):
        e_msg = self.encrypt()
        d_msg = ""
        for i in range(len(e_msg)):
            if (self.__remover(e_msg[i])):
                key_cipher = (self.key[i % self.key_len])
                msg_ntrl = (ord(e_msg[i]) - self._start_char)
                key_ntrl = (ord(key_cipher) - self._start_char)
                value = (msg_ntrl - key_ntrl) % self._length_of_char
                d_msg += chr(value + self._start_char)
            else:
                d_msg += e_msg[i]
        return d_msg



msg = "kOteKA 1234"
key = "beG"
poly = Vigenere(msg, key)

print ("Pesan : " + poly.message)
print ("Kunci : " + poly.key)
print ("======================================")
print ("Encrypt : " + poly.encrypt())
print ("Decrypt : " + poly.decrypt())