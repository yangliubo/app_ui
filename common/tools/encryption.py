import hashlib

# print(b'123')
# print()
# a = hashlib.md5(b'123')
# x = a.hexdigest()
# print(x)
class Encrypt:
    @classmethod
    def md5_encrypt(cls,a:str):
        byte_str = a.encode('utf-8')
        str_encryption = hashlib.md5(byte_str).hexdigest()
        return str_encryption
    
    
print(Encrypt.md5_encrypt('123'))