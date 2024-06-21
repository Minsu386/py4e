# Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come
# from each email address, and print the dictionary.

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File not found or can not be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    else:
        senders = line.split()
        sender = senders[1]
        counts[sender] = counts.get(sender, 0) + 1

print(counts)
