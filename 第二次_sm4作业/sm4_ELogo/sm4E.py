import base64
from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT


# bytes转换成图片
def Byte2Img(location, res):  # res必须是bytes类型
    img = base64.b64decode(res)
    file = open(location, 'wb')
    file.write(img)
    file.close()


if __name__ == '__main__':
    # 初始化CryptSM4
    crypt_sm4 = CryptSM4()

    # 设定密钥, 长度为128bit，即16个字符
    key = b'1234567812345678'

    # 将logo图片转化为bytes流
    with open('pku_logo.jpeg', 'rb') as f:
        res = base64.b64encode(f.read())
    print("图片转换成的bytes流为：")
    print(res)

    # encrypt_ecb和decrypt_ecb
    # sm4加密算法ECB模式的加密和解密

    # 加密res
    crypt_sm4.set_key(key, SM4_ENCRYPT)  # 设定密钥
    encrypt_value = crypt_sm4.crypt_ecb(res)  # 加密res，返回bytes类型
    # 生成ECB模式加密后的图片
    Byte2Img('encrypt_ECB_Img.jpeg', encrypt_value)
    print("ECB模式加密图片后的bytes为：")
    print(encrypt_value)

    # 解密res
    crypt_sm4.set_key(key, SM4_DECRYPT)  # 给解密提供密钥
    decrypt_value = crypt_sm4.crypt_ecb(encrypt_value)  # 解密，返回bytes类型
    # 生成ECB模式解密后的图片
    Byte2Img('decrypt_ECB_Img.jpeg', decrypt_value)
    print("ECB模式解密图片后的bytes为：")
    print(decrypt_value)

    assert res == decrypt_value

    # encrypt_cbc和decrypt_cbc
    # sm4加密算法CBC模式的加密和解密
    # 设定初始向量
    iv = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'  # bytes类型

    # 加密res
    crypt_sm4.set_key(key, SM4_ENCRYPT)
    encrypt_value = crypt_sm4.crypt_cbc(iv, res)  # bytes类型
    # 生成CBC模式加密后的图片
    Byte2Img('encrypt_CBC_Img.jpeg', encrypt_value)
    print("CBC模式加密图片后的bytes为：")
    print(encrypt_value)

    # 解密res
    crypt_sm4.set_key(key, SM4_DECRYPT)
    decrypt_value = crypt_sm4.crypt_cbc(iv, encrypt_value)  # bytes类型
    # 生成CBC模式解密后的图片
    Byte2Img('decrypt_CBC_Img.jpeg', decrypt_value)
    print("CBC模式解密图片后的bytes为：")
    print(decrypt_value)

    assert res == decrypt_value
