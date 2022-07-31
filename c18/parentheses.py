data = input()
stack = []
for elem in data:
    if elem == '(':
        stack.append(elem)
    else:
        if stack:
            stack.pop()
        else:
            print('NO')
            break
else:
    if stack:
        print('NO')
    else:
        print('YES')

