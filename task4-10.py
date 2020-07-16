list_=list(range(-10,11))
sp1 = []
sp2 = []

for lis in list_:
    if lis > 0:
        sp1.append(lis)
    elif lis < 0:
        sp2.append(lis)

print(sp1)
print(sp2)