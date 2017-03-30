#I may have misunderstood what you mean by delimit by |

data = open('SampleData.txt')
f = open('ParsedData.txt','w')
lines = data.readlines()
newlines = []
for i, line in enumerate(lines):
    if "keybank" in line:
        newlines.append(lines[i].replace("|",""))
for line in newlines:
    f.write(line)
f.close