import socket

data = open('SampleData.txt')
f = open('Results2.txt','w')
lines = data.readlines()
newlines = []
for i, line in enumerate(lines):
    temp = lines[i].split('<|>')
    try:
        socket.inet_aton(temp[3])
        f.write(temp[3] + "\n")
    except socket.error:
        print("Illegal IP Address: " + temp[3])
f.close