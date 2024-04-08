print('Before')
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print('After')

# What is the Largest Num
print('Find largest Number')
large_num = -1
print('Before', large_num)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > large_num:
        large_num = the_num
    print(large_num, the_num)

print('After', large_num)

# Finding the avg in a loop
print('finding the avg in a loop')
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count += 1
    sum += value
    print(count, sum, value)
print('After', count, sum, sum / count)
