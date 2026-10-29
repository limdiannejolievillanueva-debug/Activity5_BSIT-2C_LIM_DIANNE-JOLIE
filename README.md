# Stacks and Queues

*Name:* Lim, Dianne Jolie V.  
*Course, Year, and Section:* BSIT - 2C  

## About
This program demonstrates how stacks and queues work using arrays and linked lists. It also includes a balanced parentheses checker and a print queue simulation.

## Files
- array_stack.py — Stack made with a fixed-size list
- linked_stack.py — Stack made with linked nodes
- array_queue.py — Circular queue made with a fixed-size list
- linked_queue.py — Queue with front and rear nodes
- main.py — Menu for testing the four data structures
- balanced_parentheses.py — Checks matching parentheses, brackets, and braces
- print_queue.py — Enqueue and print jobs in first-in, first-out order
- analysis.md — Answers the analysis question
- sample_runs.md — Example outputs for testing

## Requirements
Python 3 is required. No extra packages are needed.

## Run the programs
Open a terminal in this folder and run:
python main.py

To run the parentheses checker:
python balanced_parentheses.py

To run the print queue:
python print_queue.py

## Things to test
- Push more than three items into the Array Stack to see overflow.
- Pop from an empty stack to see underflow.
- Enqueue more than three items into the Circular Array Queue to see overflow.
- Dequeue from an empty queue to see underflow.
- For queue wrap-around, enqueue A, B, C; dequeue A and B; then enqueue D and E. The order should be C, D, E.
- Try ({[]}) and ({[}) in the parentheses checker.
- Add several print jobs and check that the first job added prints first.
