
stack = []
id = 0


def fibo(n):
    global id
    
    id += 1
    stack.append(id)

    #print(stack)

    if(len(stack) > 1):
        print("{}->{}".format(stack[-2], stack[-1]))

    if(n <= 1):
        if(len(stack) > 1):
            print("{}->{}".format(stack.pop(), stack[-1]))

        if(n < 1):
            return 0
        if(n == 1):
            return 1

            
    else:
        result1 = fibo(n - 1)
        result2 = fibo(n - 2)

        #print(stack)
        
        if(len(stack) > 1):
            print("{}->{}".format(stack.pop(), stack[-1]))

        return result1 + result2


print(fibo(20))