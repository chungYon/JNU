links =[]
id = 0
stack = []
def JNU5(N, count=0):
    global id
    id += 1
    stack.append(id)

    if (len(stack) > 1):
        if (N != 1):
            links.append({"source" : stack[-2], "target" : stack[-1], "N" : N, "type" : "call"})
        else:
            links.append({"source" : stack[-2], "target" : stack[-1], "N" : N, "count" : count, "type" : "call"})
    else:
        if (N != 1):
            links.append({"source" : "", "target" : stack[-1], "N" : N, "type" : "call"})
        else:
            links.append({"source" : "", "target" : stack[-1], "N" : N, "count" : 0, "type" : "call"})

    if (N == 1):
        stack.pop()
        return None
    if (N == 2 or N == 3):
        JNU5(1, count+1)
        stack.pop()
        return None

    if (N%2==0 and N%3==0):
        JNU5(N//3, count+1)
        JNU5(N//2, count+1)
        JNU5(N-1, count+1)
        stack.pop()
    elif (N%2==0):
        JNU5(N//2, count+1)
        JNU5(N-1, count+1)
        stack.pop()
    elif (N%3==0):
        JNU5(N//3, count+1)
        JNU5(N-1, count+1)
        stack.pop()
    else:
        JNU5(N-1, count+1)
        stack.pop()