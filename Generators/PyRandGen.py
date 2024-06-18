import random

with open('../RandomData/PythonRandom.txt','w') as f:
    for i in range(2000000):
        r = random.randint(0,1)
        f.writelines(str(r))