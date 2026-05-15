# pip3 install pycryptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


key = get_random_bytes(16)
flag=b"AIO{REDACTED}"
# Encryption
xored_key = bytes([a ^ b for a, b in zip(key, b"arealkeyarealkey")])

cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(flag.ljust(16, b"\x00"))
print("Ciphertext:", ciphertext.hex())
print("XORed Key:", xored_key.hex())

# output:
# Ciphertext: 4fed827de1fdb68469ffe1e802a3618cd6ebf7b4aff47b4ef593cbe587d1468d
# XORed Key: 963413d296ee5dbbb3dee77f198635cb
