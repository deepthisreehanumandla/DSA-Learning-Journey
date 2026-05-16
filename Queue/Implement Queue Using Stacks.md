# 1. Implement Queue Using Stacks

## Concept

Queue follows FIFO:

- First In
- First Out

Using 2 stacks:

- `stack1` → for push
- `stack2` → for pop

---

## Code

```python
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # Push element
    def push(self, x):
        self.stack1.append(x)

    # Remove element
    def pop(self):

        if not self.stack2:

            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    # Front element
    def peek(self):

        if not self.stack2:

            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    # Check empty
    def empty(self):
        return not self.stack1 and not self.stack2
