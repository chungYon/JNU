stack = []
links = []
def factorial(n):
    stack.append(n)
    
    if(len(stack) > 1):
        print("{}->{}".format(stack[-2], stack[-1]))
        links.append({"source" : stack[-2], "target" : stack[-1], "type" : "call", "value" : n})
    
    if(n == 0 or n == 1):
        if(len(stack) > 1):
            print("{}->{}".format(stack[-1], stack[-2]))
            links.append({"source" : stack[-1], "target" : stack[-2], "type" : "return"})
            print("return value : {}".format(0))
            links[-1]["value"] = 1
            stack.pop()
        return 1
    
    else:
        result = n * factorial(n - 1)
        if(len(stack) > 1):
            print("{}->{}".format(stack[-1], stack[-2]))
            links.append({"source" : stack[-1], "target" : stack[-2], "type" : "return"})
            print("return value : {}".format(0))
            links[-1]["value"] = result
            stack.pop()
        return result

factorial(5)
for i in links:
    print(i)