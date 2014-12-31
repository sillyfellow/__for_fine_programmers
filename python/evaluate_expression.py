#!/usr/bin/python

def tokenise(expr, ops):
    for x in ops.keys() + list('()'):
        expr = expr.replace(x, ' ' + x + ' ')
    return [token for token in expr.split(' ') if token != '']

def infix_to_postfix(infix, ops):
    stack = []
    postfix = []
    tokens = tokenise(infix, ops)
    for token in tokens:
        if token in ops:
            while stack and ops.get(stack[-1], len(ops)) < ops[token]:
                postfix.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            postfix.append(token)
    while stack:
        postfix.append(stack.pop())
    return postfix

def evaluate(operand1, operand2, operator):
    if operator == '+': return int(operand1) + int(operand2)
    if operator == '-': return int(operand1) - int(operand2)
    if operator == '*': return int(operand1) * int(operand2)
    if operator == '/': return int(operand1) / int(operand2)
    raise Exception("No such operator")

def evaluate_postfix(postfix, ops):
    stack = []
    for token in postfix:
        if token in ops:
            stack.append(evaluate(stack.pop(), stack.pop(), token))
        else:
            stack.append(token)
    return stack.pop()

def evaluate_infix(expression):
    operators = { '*': 0, '/': 0, '+': 1, '-': 1, }
    return evaluate_postfix(infix_to_postfix(expression, operators), operators)

if __name__ == "__main__":
    print evaluate_infix(raw_input("Expr : "))
    print 'bye.'
