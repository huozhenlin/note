from hashlib import md5, sha256
md5_obj = md5()
md5_obj.update("这是测试demo".encode())
encryptContent = md5_obj.hexdigest()
print(encryptContent)


sha256_obj = sha256()
sha256_obj.update("这是测试demo".encode())
encryptContent = sha256_obj.hexdigest()
print(encryptContent)