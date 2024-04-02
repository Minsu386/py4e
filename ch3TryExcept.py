# When the 1st conversion fails - it just drops into the except: clause and the program continues
astr = 'Hello Phillip'
try:
    astr = int(astr)
except:
    istr = -1

print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

# When the 2nd conversion succeeds - it just kips the except: clause and the program contiues
print('Second', istr)

# Sample
rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0 :
    print('Nice work')
else:
    print('Not a number')