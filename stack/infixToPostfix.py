from collections import deque


# a+b*(c^d-e)^(f+g*h)-i

def infixToPostfix(infix):
    postfix = ''
    operatorPriority = { '+': 1, '-': 1, '*': 2, '/': 3, '^': 4 }
    stack = deque()
    
    for char in infix:
        if char.isalnum(): postfix += char
        elif char == '(': stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while stack and (stack[-1] in operatorPriority) and (operatorPriority[stack[-1]] >= operatorPriority[char]):
                postfix += stack.pop()
            stack.append(char)
            
    while stack: postfix += stack.pop()
    
    print(postfix)