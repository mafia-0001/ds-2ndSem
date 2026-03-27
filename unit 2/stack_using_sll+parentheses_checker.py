def check(s):
    stack = []
    for i in s:
        # if opening bracket
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        else:
            # if stack empty
            if len(stack) == 0:
                return False
            x = stack.pop()
            # checking
            if i == ')' and x != '(':
                return False
            if i == '}' and x != '{':
                return False
            if i == ']' and x != '[':
                return False
    # final check
    if len(stack) == 0:
        return True
    else:
        return False
    
# main
str1 = "(){}[]"
print("string is:", str1)
res = check(str1)
if res == True:
    print("Balanced")
else:
    print("Not Balanced")
