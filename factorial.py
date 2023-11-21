stack = []
links = []
def factorial(n):
    stack.append(n)
    
    if(len(stack) > 1):
        links.append({"source" : stack[-2], "target" : stack[-1], "type" : "call", "value" : n})
    else:
        links.append({"source" : "", "target" : stack[-1], "type" : "call", "value" : n})
    
    if(n == 0 or n == 1):
        stack.pop()
        return 1
    
    else:
        result = factorial(n - 1)
        for i, link in enumerate(links):
                if link["target"] == stack[-1]:
                    links[i]["return_text"] = "{} * {} = {}".format(n, result, result * n)

        stack.pop()
        return result * n