f = open('cybertronians.csv', 'r')
lines = f.readlines()
for line in lines:
	line = line.rstrip('\n')
	print line
f.close()
