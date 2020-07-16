#fname = input("Enter file name: ")
fname = "X-DSPAM-Confidence:    0.8475"
fh = open(fname)
count = 0
fltTxt = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    print(line)
    count = count + 1
    text = line.find(':')
    fltTxt = fltTxt + float(line[text+1:].lstrip())
avg = fltTxt/count
print("Average spam confidence:", avg)