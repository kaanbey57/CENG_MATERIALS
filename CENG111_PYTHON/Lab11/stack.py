def createStack():
    return []

def push(item, stack):
    stack.append(item)

def pop(stack):
    return stack.pop()

def top(stack):
    return stack[-1]

def isEmpty(stack):
    return stack==[]