# Experiment 1: Stack Implementation + Operations
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

def operation_count(n):
    count = 0
    for i in range(n):
        count += 1
    return count

n = int(input("Enter n: "))
print("Total Operations:", operation_count(n))
print("Time Complexity: O(n)")

# Experiment 3: Recursive Factorial + Call Stack Trace

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