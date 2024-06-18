import os


with open('../RandomData/PythonOpenSSL.txt', 'w') as file:
    for i in range(2000000):    
        random_bytes = os.urandom(32)
        last_byte = random_bytes[-1]
        last_bit = last_byte & 0x01
        file.writelines(str(last_bit))
    