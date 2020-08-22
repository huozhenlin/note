
# """
# aes加密算法
# 优点：安全，加密速度快
# 确定：key保存在客户端，逆向分析可以拿到
# """
# ==============-py3.6-=============
# import base64
# from Crypto.Cipher import AES
#
# '''
# 采用AES对称加密算法
# '''
# # str不是16的倍数那就补足为16的倍数
# def add_to_16(value):
#     while len(value) % 16 != 0:
#         value += '\0'
#     return str.encode(value)  # 返回bytes
# #加密方法
# def encrypt_oracle():
#     # 秘钥
#     key = '123456'
#     # 待加密文本
#     text = 'abc123def456'
#     # 初始化加密器
#
#     aes = AES.new(add_to_16(key), AES.MODE_CBC, iv=add_to_16(key))
#     #先进行aes加密
#     encrypt_aes = aes.encrypt(add_to_16(text))
#     #用base64转成字符串形式
#     encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
#     print(encrypted_text)
#
# #解密方法
# def decrypt_oralce():
#     # 秘钥
#     key = 'huazhu@&idataapi'
#     # 密文
#     text = '925b974681a678659c9418ffad3f61e2408659f937e0a06aa9cc65d56d7b4cf36d11fcafed8762362d44e0de71a490a4a1500ded3ab25738995eed65ecfaf5a00d7d84634868a6de7ddfc1adaa098db1146ec36ed9227607b28362c68fb92131e596c8ddbb0d236c0dc6d4d4aee20b0c50ecbcdafe5c767fd35eaf920d56018b878a16c49b5b2672a399adaf7778ebce2204e12d8e6ea80f48f5641f0d4163622305ba118d6d32a40db863061eb39e4323dd9468a405d28ae39a566ae3e42522c87c57e2c2ee64243dfd046d63b46c956f47225661af724a3a9a7fbc9fd8e699'
#     # 初始化加密器
#     aes = AES.new(add_to_16(key), AES.MODE_CBC, iv=add_to_16(key))
#     #优先逆向解密base64成bytes
#     base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
#     #执行解密密并转码返回str
#     decrypted_text = str(aes.decrypt(base64_decrypted),encoding='utf-8').replace('\0','')
#     print(decrypted_text)
#
# if __name__ == '__main__':
#     encrypt_oracle()
#     decrypt_oralce()


# ==============py3.5================
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
aesKey = 'huazhu@&idataapi'
# 加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
def encrypt_oracle(text):
    cryptor = AES.new(aesKey, AES.MODE_CBC, aesKey)
    text = text.encode("utf-8")
    # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
    length = 16
    count = len(text)
    add = length - (count % length)
    text = text + (b'\0' * add)
    ciphertext = cryptor.encrypt(text)
    # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
    # 所以这里统一把加密后的字符串转化为16进制字符串
    return b2a_hex(ciphertext).decode("ASCII")


# 解密后，去掉补足的空格用strip() 去掉
def decrypt_oralce(text):
    cryptor = AES.new(aesKey, AES.MODE_CBC, aesKey)
    plain_text = cryptor.decrypt(a2b_hex(text))
    return plain_text.rstrip(b'\0').decode("utf-8")

result = decrypt_oralce('925b974681a678659c9418ffad3f61e2408659f937e0a06aa9cc65d56d7b4cf36d11fcafed8762362d44e0de71a490a4a1500ded3ab25738995eed65ecfaf5a00d7d84634868a6de7ddfc1adaa098db1549015b3fe26ca1cacc423e6816f483fe53dfbd3bad2cb2967cb05f8311b73e5e36355cb7abf881868c791aab6e67ac617d72968a7cbcc0b4272e28555bec0126bb3e4f91addcb254d66a8d06bfc2a3fb07ab9988c4f7d0330a288a6999c397ed31ccbecf7931398d5cdd36bd79e2407f8a134eea20db928ca61aa8f05ca507e674e5d8b1c269d357395969dcb26bc85')
print(result)

# from cryptography.hazmat.primitives import padding
# from cryptography.hazmat.primitives.ciphers import algorithms
# from Crypto.Cipher import AES
# from binascii import b2a_hex, a2b_hex
# import json
#
# '''
# AES/CBC/PKCS7Padding 加密解密
# 环境需求:
# pip3 install pycryptodome
# '''
#
# class PrpCrypt(object):
#
#     def __init__(self, key='0000000000000000'):
#         self.key = key.encode('utf-8')
#         self.mode = AES.MODE_CBC
#         self.iv = b'0102030405060708'
#         # block_size 128位
#
#     # 加密函数，如果text不足16位就用空格补足为16位，
#     # 如果大于16但是不是16的倍数，那就补足为16的倍数。
#     def encrypt(self, text):
#         cryptor = AES.new(self.key, self.mode, self.iv)
#         text = text.encode('utf-8')
#
#         # 这里密钥key 长度必须为16（AES-128）,24（AES-192）,或者32 （AES-256）Bytes 长度
#         # 目前AES-128 足够目前使用
#
#         text=self.pkcs7_padding(text)
#
#         self.ciphertext = cryptor.encrypt(text)
#
#         # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
#         # 所以这里统一把加密后的字符串转化为16进制字符串
#         return b2a_hex(self.ciphertext).decode().upper()
#
#     @staticmethod
#     def pkcs7_padding(data):
#         if not isinstance(data, bytes):
#             data = data.encode()
#
#         padder = padding.PKCS7(algorithms.AES.block_size).padder()
#
#         padded_data = padder.update(data) + padder.finalize()
#
#         return padded_data
#
#     @staticmethod
#     def pkcs7_unpadding(padded_data):
#         unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
#         data = unpadder.update(padded_data)
#
#         try:
#             uppadded_data = data + unpadder.finalize()
#         except ValueError:
#             raise Exception('无效的加密信息!')
#         else:
#             return uppadded_data
#
#     # 解密后，去掉补足的空格用strip() 去掉
#     def decrypt(self, text):
#         #  偏移量'iv'
#         cryptor = AES.new(self.key, self.mode, self.iv)
#         plain_text = cryptor.decrypt(a2b_hex(text))
#         # return plain_text.rstrip('\0')
#         return bytes.decode(plain_text).rstrip("\x01").\
#             rstrip("\x02").rstrip("\x03").rstrip("\x04").rstrip("\x05").\
#             rstrip("\x06").rstrip("\x07").rstrip("\x08").rstrip("\x09").\
#             rstrip("\x0a").rstrip("\x0b").rstrip("\x0c").rstrip("\x0d").\
#             rstrip("\x0e").rstrip("\x0f").rstrip("\x10")
#
#     def dict_json(self, d):
#         '''python字典转json字符串, 去掉一些空格'''
#         j = json.dumps(d).replace('": ', '":').replace(', "', ',"').replace(", {", ",{")
#         return j
#
# # 加解密
# if __name__ == '__main__':
#     import json
#     pc = PrpCrypt('12345678\0\0\0\0\0\0\0\0')  # 初始化密钥
#     a = "1"
#     print("加密前：%s" % a)
#     b = pc.encrypt(a)
#     print("解密后：%s" % b)
#     print("大写变小写：%s" % b.lower())