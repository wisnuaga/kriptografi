class Monoalpha:
    _start_char = 65
    _length_of_char = 26
    _end_char = 90

    @staticmethod
    def encrypt(plaintext, key):
        plaintext = plaintext.upper()
        result = ''
        for i in plaintext:
            if(Monoalpha.remove_unused_char(i)):
                value = ((ord(i) - Monoalpha._start_char) + key) % Monoalpha._length_of_char
                result += chr(value + Monoalpha._start_char)
            else:
                result += i
        return result

    @staticmethod
    def decrypt(ciphertext, key):
        ciphertext = ciphertext.upper()
        result = ''
        for i in ciphertext:
            if (Monoalpha.remove_unused_char(i)):
                value = ((ord(i) - Monoalpha._start_char) - key) % Monoalpha._length_of_char
                result += chr(value + Monoalpha._start_char)
            else:
                result += i
        return result

    @staticmethod
    def remove_unused_char(char):
        return ((ord(char) >= Monoalpha._start_char) and (ord(char) <= Monoalpha._end_char))


