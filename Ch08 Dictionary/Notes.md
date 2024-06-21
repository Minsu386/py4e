The function dict creates a new dictionary with no items. Because dict is the name of a built-in function, you should avoid using it as a variable name.
```python
eng2sp = dict()
print(eng2sp)
# {}
```
{} = empty dictionary

To add items to the dictionary, use []
```python
eng2sp['one'] = 'uno'
```

The out put format is also the way we input. For Example:
```python
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
# {'one': 'uno', 'two': 'dos', 'three': 'tres'}
```

We can access the value from the key
```python
print(eng2sp['two'])
# 'dos'
```

In operator works for the *key* 
```python
'one' in eng2sp
# true
'uno' in eng2sp
# false
```
To find the *value* 
```python
vals = list(eng2sp.values())
'uno' in vals
# True
```

## Dictionary as a set of counters
----------------
Creating a dictionary with characters as keys and counters as the corresponding values.
Will add item to the dictionary if new. Afterwards will increment the value of an existing
item.

```python
word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
    d[c] = d[c] + 1
print(d)

# {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}

# Alternative with `get`
word = 'discussions'
d = dict()
for c in word:
    d[c] = d.get(c,0) + 1
print(d)

```

## Dictionary and Files


