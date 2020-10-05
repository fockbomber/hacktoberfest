
#DES3 CIPHER

from Crypto.Cipher import DES3

from Crypto.Util.Padding import pad,unpad

plain_text = b"12345678"
key = b"3498723894723498"

#encryption part
des3_object = DES3.new(key,DES3.MODE_ECB)

ct = des3_object.encrypt(pad(plain_text,DES3.block_size))

print("Encrypted text is : ",ct)
print("Key Size: ",len(key)," bytes","aka ",len(key*8)," bits")


#decryption part 

pt = unpad(des3_object.decrypt(ct),DES3.block_size)

print("Plain text: ",pt)

#DES3 CIPHER ENDS HERE 




