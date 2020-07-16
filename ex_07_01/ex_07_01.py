fname = input("Enter file name: ")
try:
	fh = open(fname)
	for line in fh :
		print(line.rstrip().upper())
except:
	print("Error in opening file")