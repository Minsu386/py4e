def thing():
    print('Hello')
    print('Fun')


# invoking the function
thing()
print('Zip')
# invoking the fn
thing()


# Max  Function
# A fn is some stored code that we use. A fn takes some input and produces an output.
big = max('Hello world')
print(big)
# outputs 'w' a string

# Building your own fn
# Create a new fn using the def keyword followed by optional parameters in parentheses
# Indent the body of the fn
# Once we have Defined a fn, we can call ( or invoke ) it, this is the store and reuse pattern
# *** Example ***
x = 5
print('Hello')

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day')


print('Yo')
print_lyrics()
x = x + 2
print(x)

