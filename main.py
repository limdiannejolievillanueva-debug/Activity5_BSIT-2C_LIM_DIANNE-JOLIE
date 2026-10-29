# Menu-driven test program for testing the four data structures
from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def run_menu():
    print("Select Implementation:")
    print("1. ArrayStack")
    print("2. LinkedStack")
    print("3. ArrayQueue (Circular)")
    print("4. LinkedQueue")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        cap = int(input("Enter Stack Capacity: "))
        ds = ArrayStack(cap)
        is_stack = True
    elif choice == "2":
        ds = LinkedStack()
        is_stack = True
    elif choice == "3":
        cap = int(input("Enter Queue Capacity: "))
        ds = ArrayQueue(cap)
        is_stack = False
    elif choice == "4":
        ds = LinkedQueue()
        is_stack = False
    else:
        print("Invalid choice.")
        return

    while True:
        print(f"\nCurrent State: {ds.display()}")
        if is_stack:
            print("Operations: 1. Push | 2. Pop | 3. Peek | 4. Exit")
            op = input("Choose operation: ")
            if op == "1":
                val = input("Enter value to push: ")
                try:
                    ds.push(val)
                except OverflowError as e:
                    print(f"Error: {e}")
            elif op == "2":
                try:
                    print(f"Popped: {ds.pop()}")
                except IndexError as e:
                    print(f"Error: {e}")
            elif op == "3":
                try:
                    print(f"Top element: {ds.peek()}")
                except IndexError as e:
                    print(f"Error: {e}")
            elif op == "4":
                break
        else:
            print("Operations: 1. Enqueue | 2. Dequeue | 3. Peek Front | 4. Exit")
            op = input("Choose operation: ")
            if op == "1":
                val = input("Enter value to enqueue: ")
                try:
                    ds.enqueue(val)
                except OverflowError as e:
                    print(f"Error: {e}")
            elif op == "2":
                try:
                    print(f"Dequeued: {ds.dequeue()}")
                except IndexError as e:
                    print(f"Error: {e}")
            elif op == "3":
                try:
                    print(f"Front element: {ds.peek_front()}")
                except IndexError as e:
                    print(f"Error: {e}")
            elif op == "4":
                break


if __name__ == "__main__":
    run_menu()
