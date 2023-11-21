
stack = []
links = []
id = 0

def fibo(n):
    global id
    
    id += 1
    stack.append(id)

    if(len(stack) > 1):
        links.append({"source" : stack[-2], "target" : stack[-1], "type" : "call", "value" : n})
    else:
        links.append({"source" : "", "target" : stack[-1], "type" : "call", "value" : n})

    if(n < 1):
        stack.pop()
        return 0

    if(n == 1):
        stack.pop()
        return 1


    else:
        result1 = fibo(n - 1)
        result2 = fibo(n - 2)

        for i, link in enumerate(links):
                if link["target"] == stack[-1]:
                    links[i]["return_text"] = "{} + {} = {}".format(result1, result2, result1 + result2)

        stack.pop()
        return result1 + result2