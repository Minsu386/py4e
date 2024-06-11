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

