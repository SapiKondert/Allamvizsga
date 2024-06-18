def bbs(x,n):
    new = (x['val']*x['val'])%n
    x['val'] = new
    return new

x = {'val':6192063409}

p = 30000000091
q = 40000000003

n = p*q
for i in range(1000):
    bbs(x,n)

with open('../RandomData/PythonBBS.txt', 'w') as file:
    for i in range(2000000):
        file.writelines(str(bbs(x,n)%2))



