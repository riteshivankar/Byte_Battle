#  Delete middle element of a stack
# Given a stack with push(), pop(), and empty() operations, The task is to delete the
# middle element of it without using any additional data structure.
def delete_middle(stack, n, current=0):
    if current == n // 2:
        stack.pop()
        return
    temp = stack.pop()
    delete_middle(stack, n, current + 1)
    stack.append(temp)

def delete_middle_element(stack):
    n = len(stack)
    delete_middle(stack, n)

# Example usage:
stack1 = [1, 2, 3, 4, 5]
delete_middle_element(stack1)
print("Stack after deleting middle element:", stack1)

stack2 = [1, 2, 3, 4, 5, 6]
delete_middle_element(stack2)
print("Stack after deleting middle element:", stack2)

