# Write a program to convert an Infix expression to Postfix form.
# Infix expression: The expression of the form “a operator b” (a + b) i.e., when an
# operator is in-between every pair of operands.
# Postfix expression: The expression of the form “a b operator” (ab+) i.e., When
# every pair of operands is followed by an operator
def infix_to_postfix(infix):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    postfix = ''
    stack = []

    for char in infix:
        if char.isalnum():
            postfix += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()  # Remove '(' from stack
        else:
            while stack and precedence.get(stack[-1], 0) >= precedence.get(char, 0):
                postfix += stack.pop()
            stack.append(char)

    while stack:
        postfix += stack.pop()

    return postfix

# Example usage:
infix_expression = "(a+b)*c-d/e"
postfix_expression = infix_to_postfix(infix_expression)
print("Infix Expression:", infix_expression)
print("Postfix Expression:", postfix_expression)
