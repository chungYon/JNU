
stack = []
links = []
id = 0

def fibo(n):
    global id
    
    id += 1
    stack.append(id)

    if(len(stack) > 1):
        print("{}->{}".format(stack[-2], stack[-1]))
        links.append({"source" : stack[-2], "target" : stack[-1], "type" : "call", "value" : n})

    if(n < 1):
        if(len(stack) > 1):
            print("{}->{}".format(stack[-1], stack[-2]))
            links.append({"source" : stack[-1], "target" : stack[-2], "type" : "return"})
            print("return value : {}".format(0))
            links[-1]["value"] = 0
            stack.pop()
        return 0
    if(n == 1):
        if(len(stack) > 1):
            print("{}->{}".format(stack[-1], stack[-2]))
            links.append({"source" : stack[-1], "target" : stack[-2], "type" : "return"})
            print("return value : {}".format(0))
            links[-1]["value"] = 1
            stack.pop()
        return 1


    else:
        result1 = fibo(n - 1)
        result2 = fibo(n - 2)
        
        if(len(stack) > 1):
            print("{}->{}".format(stack[-1], stack[-2]))
            links.append({"source" : stack[-1], "target" : stack[-2], "type" : "return"})
            links[-1]["value"] = result1 + result2
            stack.pop()
        return result1 + result2


print(fibo(5))
for i in links:
    print(i)