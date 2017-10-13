x = float(1)
y = float(1)
z = float(1)

for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
                a = (x * y) / z
                b = x * (y / z)
                if (b-.0001)<a<(b+.0001):
                    print("Equivalent at x = ", x, ", y = ", y, "z = ", z)
                else:
                    print("Statements are not equivalent!")
                    print("x = ", x, ", y = ", y, ", z = ", z)
                    print("a = ", a, ", and b = ", b)
                    
print("Statements are equivalent.")