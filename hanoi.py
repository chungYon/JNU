links = []
stack = []
id = 0

def hanoi(N, start, sub, end):
    global id
    id += 1
    stack.append(id)

    if (len(stack) > 1):
        links.append({"source" : stack[-2], "target" : stack[-1], "move": N, "from" : start, "via" : sub, "to" : end, "type" : "call"})
    else:
        links.append({"source" : "", "target" : stack[-1], "move": N, "from" : start, "via" : sub, "to" : end, "type" : "call"})

    if (N == 1):
        stack.pop()
        return None

    hanoi(N-1, start, end, sub)
    hanoi(N-1, sub, start, end)
    
    stack.pop()