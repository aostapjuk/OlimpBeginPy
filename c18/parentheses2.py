def isPair(left, right): # () or [] or {} -> True
    return left + right in ['()', '[]', '{}']
stack = []
for elem in input():
    if elem in '([{':
        stack.append(elem)
    else:
        if len(stack) == 0 or not isPair(stack.pop(), elem):
            print('NO')
            break
else:
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')

