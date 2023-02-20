name = input('enter a file: ')
handle = open(name)


counts = dict()
for var in handle:
    if var.startswith('From '):
        fname = var.rstrip()
        fname = var.split()
        #print(fname)
        fhand = fname[1]
        #print('a',fhand)

        if fhand not in counts:
            counts[fhand] = 1
        else:
            counts[fhand] = counts[fhand] + 1
        
bigcount = None
bigword = None
#print(counts.items())
for key,value in counts.items():
    if bigcount is None or value > bigcount:
        bigword = key
        bigcount = value

print(bigword , bigcount)