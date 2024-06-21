# Tuples
What is a Tuple?
- a tuple is a sequence of values similar to a list. The values stored in a tuple can be any type,
and they are indexed by integers. **Important** difference is that tuples are *immutable* 

- To create a single element, you have to include the final comma: Without the comma, the type will be 'str'
```python
t1 = ('a',)
type(t1)
# type 'tuple'
```

- You can't modify the elements of a tuple, but you can replace one tuple with another:
```python
t = ('A',) + t[1:]
print(t)
# ('A', 'b', 'c')
```

