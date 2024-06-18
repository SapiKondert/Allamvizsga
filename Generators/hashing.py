import hashlib

def genNum(bytes):
    return hashlib.sha256(bytes).digest()

b = 'HashHashHashHash'

b = b.encode()

for i in range(10000):
    b = genNum(b)

with open('../RandomData/PythonSHA256.txt', 'w') as file:
    for i in range(2000000):
        tmp = genNum(b)
        b = tmp
        binary_representation = ''.join(format(byte, '08b') for byte in tmp)
        file.writelines(str(binary_representation[-1]))
