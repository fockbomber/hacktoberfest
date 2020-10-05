#DES CIPHER STARTS

from Crypto.Cipher import DES

from Crypto.Util.Padding import pad, unpad

#key
key = b"12345678"
pt = b"1"

crypto_object = DES.new(key,DES.MODE_ECB)

ct = crypto_object.encrypt(pad(pt,DES.block_size))

print("Encrypted text is : ",ct)
print("Key Size: ",len(key)," bytes","aka ",len(key*8)," bits")

#decrypting text

pt = unpad(crypto_object.decrypt(ct),DES.block_size)
print("The plain text is : ",pt)


#DES CIPHER ENDS HERE 


