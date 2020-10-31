
# Test Function
def do_something(node):
    pass


# Inorder Traversal Stack

def inorder_stack(root):
    stack = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left 
        elif stack:
            current = stack.pop()
            do_something(current)
            current = current.right
        else:
            break
    