# A parameter is a variable which we use in the fn definition. It is a handle that allows the code in the fn to access
# the arguments for a particular fn invocation

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')


greet('en')
greet('es')
greet('fr')


# Return fn
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'


print(greet('en'), 'Brooks')
    # Hello Brooks
print(greet('es'), 'Alex')
    # Hola Alex
print(greet('fr'), 'Aline')
    # Bonjour Aline

# Parameters and Arguments
def addtwo(a, b):
    added = a + b
    return added
# the a, and b are parameters

x = addtwo(3, 5)
print(x)
# the 3, and 5 are arguments