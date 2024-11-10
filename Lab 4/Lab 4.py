def fibbonacci (n): 
    a,b = 1,1 
    yield a
    while b < n: 
        yield b
        a,b = b,b+a 

for i in fibbonacci(50):
    print(i)
