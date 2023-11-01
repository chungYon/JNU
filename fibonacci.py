
stack = []

def fibo(n, id):
    
    stack.insert(0, id)
    print(stack)
    
    if(n < 1):
        return [0, stack.pop()]
    if(n == 1):
        return [1, stack.pop()]
    
    result1 = fibo(n - 1, id + 1)
    result2 = fibo(n - 2, result1[1] + 1)
    
    print(stack)
    
    return [result1[0] + result2[0], stack.pop()]


print(fibo(3, 1))