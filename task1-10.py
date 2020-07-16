a = input()
b = (len(a) // 2) + (len(a) % 2)
z = a[b: ] + a[ :b]

print(z)