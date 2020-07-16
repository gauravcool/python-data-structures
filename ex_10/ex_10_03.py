fname = input("Enter the file name: ")
if len(fname) < 1 : fname = 'clown.txt'
handle = open(fname)

di = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        di[word] = di.get(word, 0) + 1

#print(di)

#x = sorted(di.items())
#print(x)

tmp = list()
#count = 0
for k,v in sorted(di.items(), reverse=True):
    newtuple = (v,k)
    tmp.append(newtuple)
#print(tmp[:5])

for v,k in tmp[:5]:
    print(k,v)