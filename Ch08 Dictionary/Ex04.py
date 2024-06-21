# Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come
# from each email address, and print the dictionary.


# ------------------ #
# Open File
fname = input("Enter File: ")
# Leave blank and press enter to use test file
if len(fname) < 1:
    fname = "../code3/mbox-short.txt"
fhand = open(fname)

# Who sent the most emails?
# Create a dictionary
emails = dict()

# Look for 'From' and take the 2nd word as the sender
for line in fhand:
    if line.startswith('From '):
        # Parse using split()
        words = line.split()
        # Create sender value w/ second word
        sender = words[1]
        # Add sender to emails-dictionary as key and increase the associated value count
        emails[sender] = emails.get(sender, 0 ) +1

# Use max loop on dictionary
bigcount = None
bigword = None
for word, count in emails.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)