fhand = open('mbox-short.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

#lst = list()
#for key,val in counts.items():
    #newtup = (val,key)
    #lst.append(newtup)

print(sorted([(v,k) for k,v in counts.items()], reverse=True))

#print("old", lst)
#lst = sorted(lst, reverse=True)
#print("new", lst)

for val,key in lst[:10]:
    print(key,val)