from gmssl import sm3
import sm3Encrypt


# 长度扩展攻击过程
# 已知密钥的hash值，密钥长度，未知密钥明文
# sm3为大端方式，修改第二轮IV为hash(secret),可用于求hash(secret||padding||length||append)。padding和length将其填充到512位
# 构造任意str使得len(str)=len(secret),第一轮计算截断后，结果IV修改为hash(secret)的分组，再进行第二轮，即可求得用于求hash(secret||padding||length||append)

# 字符串转ASCII码
def strToASCII(string):
    li = []
    for s in string:
        li.append(ord(s))
    return li


if __name__ == '__main__':

    strA = input('请输入密钥的值:')  # 输入secret的值，后面计算中secret当做未知，仅知道其长度和hash值
    strSecond = input('请输入第二轮字符串（append）进行长度拓展攻击，任意输入即可:')  # 输入第二轮计算的字符串，即append

    length = len(strA)  # 计算secret长度
    y = sm3.sm3_hash(strToASCII(strA))  # 计算secret的hash值用于修改第二轮IV，存于y中
    # print(y)

    # 对hash(secret)进行分组，用于求二轮的IV，分组存在liNum中
    liStr = []
    liNum = []
    count = 0
    for i in range(0, len(y) + 1):
        if count % 8 == 0 and count != 0:
            liStr.append('0x' + y[i - 8:i])
        count = count + 1
    for x in liStr:
        liNum.append(int(x, 16))
    # print(count)
    # print(liStr)
    # print(liNum)

    strARandom = 'a' * length  # 填充第一轮中的secret部分，长度相等即可
    strPadding = '\x80' + '\x00' * (56 - length - 1)  # 填充第一轮剩余部分
    strLength = '\x00' * 6  # 第一轮数据长度前半部分
    # 根据第一轮secret长度分类填写长度部分
    if length * 8 < 256:
        strLength = strLength + '\x00' + bytes([length * 8]).decode('utf-8')
    else:
        strLength = strLength + bytes([(length - 32) * 8]).decode('utf-8') + '\xff'

    # 输出hash(secret||padding||length||append)用于对比验证攻击是否成功
    y2 = sm3.sm3_hash(strToASCII(strA + strPadding + strLength + strSecond))
    print('hash(secret||padding||length||append)为：')
    print(y2)

    # 将新的IV，即liNum传入sm3Encrypt进行攻击
    y1 = sm3Encrypt.sm3_hash(strToASCII(strARandom + strPadding + strLength + strSecond), liNum)
    print('使得length(random)==length(secret),并利用hash(secret)修改IV进行攻击后hash(random||padding||length||append)为：')
    print(y1)

    if y1 == y2:
        print("两个hash相等，长度拓展攻击成功!!!")
    else:
        print("长度拓展攻击失败")