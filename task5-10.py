list_= [1, 3, 4, 56, -32, -23 , -33,-54, -201, -100,-44]
new_list = []

for lis in list_:
    if lis > 0:
        new_list.append(1)
    elif lis < 0:
        new_list.append(-1)
    else:
        new_list.append(0)


print(new_list)