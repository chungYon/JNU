

def fibo(n, parent_id, child_id):
    
    print("{}->{}".format(parent_id, child_id))
    
    if(n < 1):
        return [0, child_id]
    if(n == 1):
        return [1, child_id]
    
    result1 = fibo(n - 1, child_id, child_id + 1)
    print("{}->{}".format(result1[1], child_id))
    result2 = fibo(n - 2, child_id, result1[1] + 1)
    print("{}->{}".format(result2[1], child_id))
    return [result1[0] + result2[0], result2[1]]

print(fibo(5, 0, 1))