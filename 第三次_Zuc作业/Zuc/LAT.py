# 手动将SBox0和SBox1输入
SBox0 = [['3E', '72', '5B', '47', 'CA', 'E0', '00', '33', '04', 'D1', '54', '98', '09', 'B9', '6D', 'CB'],
         ['7B', '1B', 'F9', '32', 'AF', '9D', '6A', 'A5', 'B8', '2D', 'FC', '1D', '08', '53', '03', '90'],
         ['4D', '4E', '84', '99', 'E4', 'CE', 'D9', '91', 'DD', 'B6', '85', '48', '8B', '29', '6E', 'AC'],
         ['CD', 'C1', 'F8', '1E', '73', '43', '69', 'C6', 'B5', 'BD', 'FD', '39', '63', '20', 'D4', '38'],
         ['76', '7D', 'B2', 'A7', 'CF', 'ED', '57', 'C5', 'F3', '2C', 'BB', '14', '21', '06', '55', '9B'],
         ['E3', 'EF', '5E', '31', '4F', '7F', '5A', 'A4', '0D', '82', '51', '49', '5F', 'BA', '58', '1C'],
         ['4A', '16', 'D5', '17', 'A8', '92', '24', '1F', '8C', 'FF', 'D8', 'AE', '2E', '01', 'D3', 'AD'],
         ['3B', '4B', 'DA', '46', 'EB', 'C9', 'DE', '9A', '8F', '87', 'D7', '3A', '80', '6F', '2F', 'C8'],
         ['B1', 'B4', '37', 'F7', '0A', '22', '13', '28', '7C', 'CC', '3C', '89', 'C7', 'C3', '96', '56'],
         ['07', 'BF', '7E', 'F0', '0B', '2B', '97', '52', '35', '41', '79', '61', 'A6', '4C', '10', 'FE'],
         ['BC', '26', '95', '88', '8A', 'B0', 'A3', 'FB', 'C0', '18', '94', 'F2', 'E1', 'E5', 'E9', '5D'],
         ['D0', 'DC', '11', '66', '64', '5C', 'EC', '59', '42', '75', '12', 'F5', '74', '9C', 'AA', '23'],
         ['0E', '86', 'AB', 'BE', '2A', '02', 'E7', '67', 'E6', '44', 'A2', '6C', 'C2', '93', '9F', 'F1'],
         ['F6', 'FA', '36', 'D2', '50', '68', '9E', '62', '71', '15', '3D', 'D6', '40', 'C4', 'E2', '0F'],
         ['8E', '83', '77', '6B', '25', '05', '3F', '0C', '30', 'EA', '70', 'B7', 'A1', 'E8', 'A9', '65'],
         ['8D', '27', '1A', 'DB', '81', 'B3', 'A0', 'F4', '45', '7A', '19', 'DF', 'EE', '78', '34', '60']
         ]

SBox1 = [['55', 'C2', '63', '71', '3B', 'C8', '47', '86', '9F', '3C', 'DA', '5B', '29', 'AA', 'FD', '77'],
         ['8C', 'C5', '94', '0C', 'A6', '1A', '13', '00', 'E3', 'A8', '16', '72', '40', 'F9', 'F8', '42'],
         ['44', '26', '68', '96', '81', 'D9', '45', '3E', '10', '76', 'C6', 'A7', '8B', '39', '43', 'E1'],
         ['3A', 'B5', '56', '2A', 'C0', '6D', 'B3', '05', '22', '66', 'BF', 'DC', '0B', 'FA', '62', '48'],
         ['DD', '20', '11', '06', '36', 'C9', 'C1', 'CF', 'F6', '27', '52', 'BB', '69', 'F5', 'D4', '87'],
         ['7F', '84', '4C', 'D2', '9C', '57', 'A4', 'BC', '4F', '9A', 'DF', 'FE', 'D6', '8D', '7A', 'EB'],
         ['2B', '53', 'D8', '5C', 'A1', '14', '17', 'FB', '23', 'D5', '7D', '30', '67', '73', '08', '09'],
         ['EE', 'B7', '70', '3F', '61', 'B2', '19', '8E', '4E', 'E5', '4B', '93', '8F', '5D', 'DB', 'A9'],
         ['AD', 'F1', 'AE', '2E', 'CB', '0D', 'FC', 'F4', '2D', '46', '6E', '1D', '97', 'E8', 'D1', 'E9'],
         ['4D', '37', 'A5', '75', '5E', '83', '9E', 'AB', '82', '9D', 'B9', '1C', 'E0', 'CD', '49', '89'],
         ['01', 'B6', 'BD', '58', '24', 'A2', '5F', '38', '78', '99', '15', '90', '50', 'B8', '95', 'E4'],
         ['D0', '91', 'C7', 'CE', 'ED', '0F', 'B4', '6F', 'A0', 'CC', 'F0', '02', '4A', '79', 'C3', 'DE'],
         ['A3', 'EF', 'EA', '51', 'E6', '6B', '18', 'EC', '1B', '2C', '80', 'F7', '74', 'E7', 'FF', '21'],
         ['5A', '6A', '54', '1E', '41', '31', '92', '35', 'C4', '33', '07', '0A', 'BA', '7E', '0E', '34'],
         ['88', 'B1', '98', '7C', 'F3', '3D', '60', '6C', '7B', 'CA', 'D3', '1F', '32', '65', '04', '28'],
         ['64', 'BE', '85', '9B', '2F', '59', '8A', 'D7', 'B0', '25', 'AC', 'AF', '12', '03', 'E2', 'F2']
         ]


def createEmptyList(size):
    return [0] * size


# 创建一张空的256*256的DDT
# 因为输入是8比特x，输出是8比特y，因此一共2^8=256位
def createEmptyLAT():
    LAT = []
    for i in range(0, 256):
        tem = createEmptyList(256)
        LAT.append(tem)
    return LAT


LAT0 = createEmptyLAT()
LAT1 = createEmptyLAT()


# 将8位二进制数num每一位0，1情况提取出来用于之后异或
def getInt2in8bitsInt(num):
    ls = []
    for i in range(0, 8):
        ls.append(num % 2)
        num = num >> 1
    return ls


# 根据计算LAT的方法（详见实验报告）。填充LAT表,由于每个输入x可以由S盒拿到对应输出，因此按这个进行256次运算。
# LAT的行为x的参与异或位情况，列为y参与异或位情况
def appendS0LAT():
    for inputS in range(0, 256):  # 对每一个输入S0盒的x进行计算
        input_1 = inputS >> 4
        input_2 = inputS % 16
        outputS = int(SBox0[input_1][input_2], 16)
        # X中8位的256种不同的异或情况
        # 2的8次方，8位，每位分别有参与异或和不参与两种情况
        for input_x in range(0, 256):
            xor_x = 0
            ls_x = getInt2in8bitsInt(input_x)
            for i in range(0, 8):
                if ls_x[i] == 1:
                    tem = (inputS >> i) & 1
                    xor_x = xor_x ^ tem
            # 同理，Y中8位的也有256种不同的异或情况
            for input_y in range(0, 256):
                xor_y = 0
                ls_y = getInt2in8bitsInt(input_y)
                for i in range(0, 8):
                    if ls_y[i] == 1:
                        tem = (outputS >> i) & 1
                        xor_y = xor_y ^ tem
                if xor_x == xor_y:
                    LAT0[input_x][input_y] = LAT0[input_x][input_y] + 1
    # 为了有正有负看出回归性，要减256/2=128
    for i in range(0,256):
        for j in range(0,256):
            LAT0[i][j]=LAT0[i][j]-128

def appendS1LAT():
    for inputS in range(0, 256):  # 对每一个输入S1盒的x进行计算
        input_1 = inputS >> 4
        input_2 = inputS % 16
        outputS = int(SBox1[input_1][input_2], 16)
        for input_x in range(0, 256):  # 同上部分代码，X中8位有256种不同的异或情况
            xor_x = 0
            ls_x = getInt2in8bitsInt(input_x)
            for i in range(0, 8):
                if ls_x[i] == 1:
                    tem = (inputS >> i) & 1
                    xor_x = xor_x ^ tem
            for input_y in range(0, 256):  # 同理，Y中8位也有256种不同的异或情况
                xor_y = 0
                ls_y = getInt2in8bitsInt(input_y)
                for i in range(0, 8):
                    if ls_y[i] == 1:
                        tem = (outputS >> i) & 1
                        xor_y = xor_y ^ tem
                if xor_x == xor_y:
                    LAT1[input_x][input_y] = LAT1[input_x][input_y] + 1
    # 为了有正有负看出回归性，要减256/2=128
    for i in range(0,256):
        for j in range(0,256):
            LAT1[i][j]=LAT1[i][j]-128


# 将两张LAT表输出
def printLAT():
    print("LAT for SBox0  is: \n")
    for i in range(0, 256):
        print(LAT0[i])
    print("\n")
    print("LAT for SBox1  is: \n")
    for i in range(0, 256):
        print(LAT1[i])


if __name__ == '__main__':
    appendS0LAT()
    appendS1LAT()
    printLAT()
