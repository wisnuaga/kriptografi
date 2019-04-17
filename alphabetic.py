class Monoalpha:
    _start_char = 65
    _length_of_char = 26
    _end_char = 90

    @staticmethod
    def encrypt(plaintext, key):
        plaintext = plaintext.upper()
        result = ''
        for index in plaintext:
            if(Monoalpha.remove_unused_char(index)):
                value = ((ord(index) - Monoalpha._start_char) + key) % Monoalpha._length_of_char
                result += chr(value + Monoalpha._start_char)
            else:
                result += index
        return result

    @staticmethod
    def decrypt(ciphertext, key):
        ciphertext = ciphertext.upper()
        result = ''
        for index in ciphertext:
            if (Monoalpha.remove_unused_char(index)):
                value = ((ord(index) - Monoalpha._start_char) - key) % Monoalpha._length_of_char
                result += chr(value + Monoalpha._start_char)
            else:
                result += index
        return result

    @staticmethod
    def remove_unused_char(char):
        return ((ord(char) >= Monoalpha._start_char) and (ord(char) <= Monoalpha._end_char))


class Polyalpha(Monoalpha):

    @staticmethod
    def encrypt(plaintext, key):
        plaintext = plaintext.upper()
        key = key.upper()
        result = ''
        key_length = len(key)

        for index in range(len(plaintext)):
            if(Polyalpha.remove_unused_char(plaintext[index])):
                key_cipher = (key[index % key_length])
                plaintext_ntrl = (ord(plaintext[index]) - Polyalpha._start_char)
                key_ntrl = (ord(key_cipher) - Polyalpha._start_char)

                value = (plaintext_ntrl + key_ntrl) % Polyalpha._length_of_char
                result += chr(value + Polyalpha._start_char)

            else:
                result += plaintext[index]

        return result

    @staticmethod
    def decrypt(ciphertext, key):
        ciphertext = ciphertext.upper()
        key = key.upper()
        result = ''
        key_length = len(key)

        for index in range(len(ciphertext)):
            if(Polyalpha.remove_unused_char(ciphertext[index])):
                key_cipher = (key[index % key_length])
                ciphertext_ntrl = (ord(ciphertext[index]) - Polyalpha._start_char)
                key_ntrl = (ord(key_cipher) - Polyalpha._start_char)

                value = (ciphertext_ntrl - key_ntrl) % Polyalpha._length_of_char
                result += chr(value + Polyalpha._start_char)

            else:
                result += ciphertext[index]

        return result


