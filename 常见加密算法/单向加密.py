"""
单向加密，如md5,sha256等
优点：加密后不可逆
缺点：加密者也不知道加密前的值
"""
from hashlib import md5, sha256
md5_obj = md5()
md5_obj.update("这是测试demo".encode())
encryptContent = md5_obj.hexdigest()
print(encryptContent)


sha256_obj = sha256()
sha256_obj.update("这是测试demo".encode())
encryptContent = sha256_obj.hexdigest()
print(encryptContent)