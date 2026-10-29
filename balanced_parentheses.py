# Balanced Parentheses Checker using LinkedStack
from linked_stack import LinkedStack


def is_balanced(expression: str) -> bool:
    stack = LinkedStack()
    brackets = {")": "(", "]": "[", "}": "{"}

    for char in expression:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty() or stack.pop() != brackets[char]:
                return False
    return stack.is_empty()


if __name__ == "__main__":
    test_exprs = ["({[]})", "({[})", "((())", "[{()}]"]
    print("--- Parentheses Checker Tests ---")
    for expr in test_exprs:
        print(f"Expression '{expr}' is balanced: {is_balanced(expr)}")
