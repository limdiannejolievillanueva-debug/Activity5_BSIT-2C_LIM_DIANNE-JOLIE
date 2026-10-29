Sample Runs & Error Handling Documentation

​1. ArrayStack Overflow & Underflow
​Overflow: Attempting to push() past the predefined capacity raises an explicit OverflowError: Stack overflow: Cannot push to a full stack.
​Underflow: Attempting to pop() or peek() an empty stack raises an explicit IndexError: Stack underflow: Cannot pop from an empty stack.
​
2. Circular ArrayQueue Wrap-Around & Overflow
​Wrap-Around: Enqueuing items, dequeuing some, and enqueuing more successfully wraps the rear index back to index 0 using modulo arithmetic (front + size) % capacity.
​Overflow: Reaching capacity limits throws OverflowError: Queue overflow: Cannot enqueue to a full queue.
​
3. Application Outputs
​Balanced Parentheses: Correctly evaluates strings like ({[]}) as True and ({[}) as False.
​Print Queue: Successfully handles jobs in FIFO order (Job1, then Job2, then Job3).
