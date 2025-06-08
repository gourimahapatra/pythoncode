def fib(n):
    a,b= 0,1
    if n == 0 : 
        print(0)
        return
    if n == 1 : 
        print(1)
        return
    while b < n:
        #print(a)
        #a,b = b,a + b
        res = a + b
        a = b
        b = res
        #print(a,b)
        print(res)
 

fib(4)
0,1
0+1, 1+1, 2+1, 3+2

strl= "Gouri"
if 'i' in strl:
    print("Found")
