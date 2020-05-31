"""
rsa加密算法
优点：安全，私钥保存着服务端
确定：速度慢
"""
import rsa
publicKey, privateKey = rsa.newkeys(999)
content = '这是测试rsa加密算法的测试文本'

encryContent = rsa.encrypt(content.encode(), publicKey)
print(encryContent)
decryContent = rsa.decrypt(encryContent, privateKey)
print(decryContent.decode())