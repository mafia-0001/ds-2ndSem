def is_balanced(s):
    stack = []
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        else:
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or \
               (top == '{' and ch != '}') or \
               (top == '[' and ch != ']'):
                return False
    return len(stack) == 0

print(is_balanced("()[]"))