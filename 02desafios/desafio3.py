def main():
    # dic = {
    #     'a': (stack.append('A') if not stack or stack[-1] == 'A' else stack.pop()),
    #     'b': (stack.append('B') if not stack or stack[-1] == 'B' else stack.pop()),
    # }

    # flag = 0
    stack = []
    buf = input()
    for i in buf:
        # dic[i]
        if i == 'a':
            if not stack or stack[-1] == 'A':
                stack.append('A')
            elif stack[-1] == 'B':
                stack.pop()
        elif i == 'b':
            if not stack or stack[-1] == 'B':
                stack.append('B')
            elif stack[-1] == 'A':
                stack.pop()
        if not stack:
            print('nil')
        else:
            print(''.join(stack))
    if not stack:
        print('Aceito')
    else:
        print('Rejeito')
    while True:
        try:
            stack = []
            buf = input()
            print()
            for i in buf:
                if i == 'a':
                    if not stack or stack[-1] == 'A':
                        stack.append('A')
                    elif stack[-1] == 'B':
                        stack.pop()
                elif i == 'b':
                    if not stack or stack[-1] == 'B':
                        stack.append('B')
                    elif stack[-1] == 'A':
                        stack.pop()
                if not stack:
                    print('nil')
                else:
                    print(''.join(stack))
            if not stack:
                print('Aceito')
            else:
                print('Rejeito')
        except EOFError:
            
            break

main()
