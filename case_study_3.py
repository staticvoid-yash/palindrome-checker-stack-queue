# Palindrome Checker using Stack + queue 

# Node class for Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ---------- STACK using Linked List (LIFO) ----------
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def is_empty(self):
        return self.top is None


# ---------- QUEUE using Linked List (FIFO) ----------
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:          # empty queue
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:         # queue became empty
            self.rear = None
        return data

    def is_empty(self):
        return self.front is None


# ---------- PALINDROME CHECKER ----------
def is_palindrome(text):
    stack = Stack()
    queue = Queue()

    # Step 1: Put all characters in both
    for ch in text:
        stack.push(ch)
        queue.enqueue(ch)

    # Step 2: compare one by one 
    while not stack.is_empty() and not queue.is_empty():
        if stack.pop() != queue.dequeue():
            return False
    return True


# ---------- MAIN ----------
if __name__ == "__main__":
    print("=== Palindrome Checker using Stack + Queue ===\n")

    test_words = ["madam", "racecar", "hello", "12321", "A man"]

    for word in test_words:
        result = is_palindrome(word.lower())
        status = " Palindrome" if result else " Not Palindrome"
        print(f"{word:12} → {status}")

    # User input option
    print("\n--- Try your own ---")
    user_input = input("Enter a string: ")
    if is_palindrome(user_input.lower()):
        print(f"'{user_input}' is a Palindrome ")
    else:
        print(f"'{user_input}' is NOT a Palindrome ")