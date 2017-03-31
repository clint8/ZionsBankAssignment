import socket

def verifyAddr(str):
    try:
        socket.inet_aton(str)
        return True
    except socket.error:
        print("Illegal IP Address: " + str)
        return False

data = open('SampleData.txt')
f = open('Results3.txt','w')
lines = data.readlines()
newlines = []
for i, line in enumerate(lines):
    temp = lines[i].split('<|>')
    addr1 = temp[3].strip()
    addr2 = temp[8].strip()
    if verifyAddr(addr1) and verifyAddr(addr2):
        temp[8] = addr2
        for i, val in enumerate(temp):
            if i != (len(temp) - 1):
                f.write(val + "<>")
        f.write('\n')
f.close


