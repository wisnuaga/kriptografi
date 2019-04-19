class Caesar:
    _start_char = 65
    _length_of_char = 26
    _end_char = 90

    def __init__(self, message, key):
        self.message = message.upper()
        self.key = key

    #hapus karakter selain (A s/d Z)
    def __remover(self, char):
        return (ord(char) >= self._start_char) and (ord(char) <= self._end_char)

    def encrypt(self):
        e_msg = ""
        for char in self.message:
            if(self.__remover(char)):
                value = ( (ord(char) - self._start_char) + self.key ) % self._length_of_char
                e_msg += chr(value + self._start_char)
            else:
                e_msg += char
        return e_msg

    def decrypt(self):
        e_msg = self.encrypt()
        d_msg = ""
        for char in e_msg:
            if (self.__remover(char)):
                value = ((ord(char) - self._start_char) - self.key) % self._length_of_char
                d_msg += chr(value + self._start_char)
            else:
                d_msg += char
        return d_msg


msg = "kOteKA 1234"
key = 3

monoalphabetic = Caesar(msg, key)
print (monoalphabetic.encrypt())
print (monoalphabetic.decrypt())