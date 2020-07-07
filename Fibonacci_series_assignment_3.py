fib = [0, 1]


for i in range(20):     #it will be iterated 20 times
    fib.append(fib[-1]+fib[-2])

print(fib)
print(fib[-1])
