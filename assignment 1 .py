# Experiment 1: Stack Implementation + Operations
Design a Stack ADT and build confidence in LIFO behavior and constant-time operations.
What you will implement (in lab)
Implement StackADT with push, pop, peek, isEmpty, size. Use it once meaningfully (e.g.,
store steps of recursion trace, undo operations, or expression symbols).
Input / Output expectation
Input: sequence of operations. Output: returned values (pop/peek) + final stack state
+ safe underflow handling.
Lab checkpoints (faculty verifies)
• All operations behave correctly (LIFO)
• Underflow handled safely (no crash)
• Stack used in a small real task (not only basic testing)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(item, "pushed")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack Underflow"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is Empty"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Stack:", self.items)


# Use of Stack
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()

print("Popped:", s.pop())
print("Top element:", s.peek())


# Experiment 2: Complexity Drill (Operation Counting)

# Count number of operations in a loop
Aim
Develop intuition for time/space complexity using simple loop structures and case analysis.
What you will implement (in lab)
Create 4 snippets: single loop, nested loop, triangular loop, and halving loop. Count operations roughly and map to Big-O. Add best/avg/worst reasoning for linear search and
binary search.
    Input: n. Output: for each snippet print estimated operation count + complexity label
+ 2-line justification.
Lab checkpoints (faculty verifies)
• Correct mapping for O(1), O(n), O(n2), O(logn)
• Clear best/avg/worst definitions with example.

def operation_count(n):
    count = 0
    for i in range(n):
        count += 1
    return count

n = int(input("Enter n: "))
print("Total Operations:", operation_count(n))
print("Time Complexity: O(n)")

# Experiment 3: Recursive Factorial + Call Stack Trace
Experiment 3: Recursive Factorial + Call Stack Trace
Aim
Learn recursion basics: base case, recursive case, and stack growth.
What you will implement (in lab)
Implement factorial(n) recursively for n≥0 and reject invalid input. Draw call stack for
factorial(4) showing return values.
Input / Output expectation
Input: n. Output: factorial(n) + manual call stack trace (in notebook) + time/space
complexity statement.
Lab checkpoints (faculty verifies)
• Base case correct, recursion correct
• Complexity stated correctly: time O(n), space O(n)

def factorial(n):
    print("Calling factorial(", n, ")")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter number: "))
result = factorial(num)
print("Factorial =", result)

#  Experiment 4: Fibonacci (Naive vs Memoized) + Call Counter

# Naive Fibonacci

Understand inefficiency of naive recursion and benefit of memoization.
What you will implement (in lab)
Implement fib naive(n) and fib memo(n) with call counters. Compare call counts for
n=10,20,30 to show performance difference clearly.
Input / Output expectation
Input: n values. Output: fib(n) + calls naive + calls memo + short explanation (3–4
lines).
Lab checkpoints (faculty verifies)
• Memoized version drastically reduces calls
• Student can explain repeated subproblems



count1 = 0
def fib_naive(n):
    global count1
    count1 += 1
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)


# experiment 4 Memoized Fibonacci
count2 = 0
memo = {}
def fib_memo(n):
    global count2
    count2 += 1
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]


n = int(input("Enter n: "))
print("Naive Fibonacci:", fib_naive(n))
print("Naive Call Count:", count1)

print("Memoized Fibonacci:", fib_memo(n))
print("Memoized Call Count:", count2)

#  Experiment 5: Tower of Hanoi (N=3 Trace + Complexity)
Aim
Use recursion to generate step-by-step solution and observe exponential growth.
What you will implement (in lab)
Implement Hanoi(n, src, aux, dst) and print exact move sequence for n=3. Show move
count for n=4 and infer complexity.
Input / Output expectation
Input: n. Output: move sequence for n=3 + move count for n=4 + complexity statement.
Lab checkpoints (faculty verifies)
• Correct move order for n=3
• Complexity stated: O(2n)

def tower_of_hanoi(n, source, helper, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return
    tower_of_hanoi(n-1, source, destination, helper)
    print("Move disk", n, "from", source, "to", destination)
    tower_of_hanoi(n-1, helper, source, destination)

n = 3
tower_of_hanoi(n, 'A', 'B', 'C')

print("Time Complexity: O(2^n)")

# experiment 6 : Binary Search + Recurrence + Complexity

Aim
Implement binary search recursively and explain why it is O(log n).
What you will implement (in lab)
Implement binarySearch(arr, key, low, high) returning index or -1. Explain recurrence
intuition: T(n)=T(n/2)+O(1).
Input / Output expectation
Input: sorted list + key. Output: index or -1, including empty list and missing key cases.
Lab checkpoints (faculty verifies)
• Correct mid logic and termination
• Handles empty list and not-found properly


def binary_search(arr, low, high, key):
    if low <= high:
        mid = (low + high) // 2
        print("Checking index:", mid)

        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, low, mid - 1, key)
        else:
            return binary_search(arr, mid + 1, high, key)
    else:
        return -1


arr = [2, 5, 8, 12, 16, 23, 38, 56, 72]
key = int(input("Enter element to search: "))

result = binary_search(arr, 0, len(arr)-1, key)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")

print("Recurrence: T(n) = T(n/2) + 1")

print("Time Complexity: O(log n)")
