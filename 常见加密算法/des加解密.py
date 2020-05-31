from Crypto.Cipher import DES

# str不是8的倍数那就补足为16的倍数
def add_to_8(value):
    while len(value) % 8 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes

key = "01234"

content = "我是爬虫"
des = DES.new(key=add_to_8(key), mode=DES.MODE_ECB)
encryptContent = des.encrypt(add_to_8(content))
print(encryptContent)
decryptContent = des.decrypt(encryptContent)
print(decryptContent.decode().replace('\0',''))