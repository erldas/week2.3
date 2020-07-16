lis = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a','a', 'a']
print(lis)

for index, li in enumerate(lis,0):
    if index % 2 == 0:
        print([index,li]) 