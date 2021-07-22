entrada = int(input())

def fib_rec(n):
    
    if n == 0:
        return "b"
    
    elif n == 1:
        return "a"
    
    elif n > 1:
        return (fib_rec(n-1) + fib_rec(n-2))
    

print(fib_rec(entrada))