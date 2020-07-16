name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst = list()

hrdict = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    words = line.split()
    fulldate = words[5]
    hour = fulldate.split(':')[0]
    lst.append(hour)
for hr in lst:
	hrdict[hr] = hrdict.get(hr, 0) + 1
for key,val in sorted(hrdict.items()):
    print(key, val)