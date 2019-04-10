from monoalpha import Monoalpha

class Polyalpha(Monoalpha):

    @staticmethod
    def encrypt(plaintext, key):
        plaintext = plaintext.upper()
        key = key.upper()
        result = ''
        key_length = len(key)

        for i in range(len(plaintext)):
            if(Polyalpha.remove_unused_char(plaintext[i])):
                key_cipher = (key[i % key_length])
                plaintext_ntrl = (ord(plaintext[i]) - Polyalpha._start_char)
                key_ntrl = (ord(key_cipher) - Polyalpha._start_char)

                value = (plaintext_ntrl + key_ntrl) % Polyalpha._length_of_char
                result += chr(value + Polyalpha._start_char)

            else:
                result += plaintext[i]

        return result

    @staticmethod
    def decrypt(ciphertext, key):
        ciphertext = ciphertext.upper()
        key = key.upper()
        result = ''
        key_length = len(key)

        for i in range(len(ciphertext)):
            if(Polyalpha.remove_unused_char(ciphertext[i])):
                key_cipher = (key[i % key_length])
                ciphertext_ntrl = (ord(ciphertext[i]) - Polyalpha._start_char)
                key_ntrl = (ord(key_cipher) - Polyalpha._start_char)

                value = (ciphertext_ntrl - key_ntrl) % Polyalpha._length_of_char
                result += chr(value + Polyalpha._start_char)

            else:
                result += ciphertext[i]

        return result
