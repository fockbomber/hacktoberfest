#AES CIPHER STARTS

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes

key = get_random_bytes(32)
plaint_text = b"Hello Friend !"

AES_OBJECT = AES.new(key,AES.MODE_ECB)

#encryption part
cipher_text = AES_OBJECT.encrypt(pad(plaint_text,AES.block_size))

print("Key Size: ",len(key)," bytes","aka ",len(key*8)," bits")

print("Encrypted text is : ", cipher_text)

#decryption part 
plain_text = unpad(AES_OBJECT.decrypt(cipher_text),AES.block_size)

print("Plain text is : ",plain_text)

#AES CIPHER ENDS HERE 
