from alphabetic import Monoalpha, Polyalpha

msg = "JIDAD 1234"
key_mono = 3
key_poly = "beg"

# # mono-alphabetic
# en_msg = Monoalpha.encrypt(msg, key_mono)
# dn_msg = Monoalpha.decrypt(en_msg, key_mono)

# poly-alphabetic
en_msg = Polyalpha.encrypt(msg, key_poly)
dn_msg = Polyalpha.decrypt(en_msg, key_poly)

print (msg)
print (en_msg)
print (dn_msg)
