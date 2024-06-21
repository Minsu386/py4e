# Write a program that categorizes each mail message by which day of the week the commit was done.
# Look for lines that start w/ "From", then look for the 3rd word and keep a running count of each of the days of the
# week. Print out the content of your dictionary.

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

day_count = dict()
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    else:
        words = line.split()
        day = words[2]
        if day not in day_count:
            day_count[day] = 1
        else:
            day_count[day] += 1

print(day_count)

