stack = []
for elem in input():
    if elem in '+-*':
        b = stack.pop()
        a = stack.pop()
        if elem == '+':
            stack.append(a + b)
        elif elem == '-':
            stack.append(a - b)
        else:
            stack.append(a * b)
    else:
        stack.append(int(elem))
print(stack[0])
