# LeetCode 1823 — Find the Winner of the Circular Game

## Concept

Players stand in a circle.

Every `k-th` player is removed.

Find the last remaining player.

---

# Solution 1 — Using List

```python
class Solution:
    def findTheWinner(self, n, k):

        players = [i for i in range(1, n + 1)]

        index = 0

        while len(players) > 1:

            index = (index + k - 1) % len(players)

            players.pop(index)

        return players[0]
```

---

## Why Modulo?

```python
(index + k - 1) % len(players)
```

Modulo keeps index inside list range.

Example:

```text
3 % 3 = 0
```

Circular movement:

```text
last index → first index
```

---

# Dry Run

## Initial

```text
players = [1,2,3,4,5]
k = 2
index = 0
```

---

## Round 1

```text
index = (0 + 2 - 1) % 5
      = 1
```

Remove:

```text
2
```

Remaining:

```text
[1,3,4,5]
```

---

## Round 2

```text
index = (1 + 2 - 1) % 4
      = 2
```

Remove:

```text
4
```

Remaining:

```text
[1,3,5]
```

---

## Round 3

```text
index = (2 + 2 - 1) % 3
      = 0
```

Remove:

```text
1
```

Remaining:

```text
[3,5]
```

---

## Round 4

```text
index = (0 + 2 - 1) % 2
      = 1
```

Remove:

```text
5
```

Remaining:

```text
[3]
```

Winner:

```text
3
```

---

# Solution 2 — Using Queue

```python
from collections import deque

class Solution:
    def findTheWinner(self, n, k):

        q = deque(range(1, n + 1))

        while len(q) > 1:

            for _ in range(k - 1):
                q.append(q.popleft())

            q.popleft()

        return q[0]
```

---

## Why `k - 1`?

Move first `k-1` players to back.

Then front becomes the `k-th` player.

Remove it.

---

## Example

```text
[1,2,3,4,5]
k = 2
```

Move 1 player:

```text
[2,3,4,5,1]
```

Remove front:

```text
remove 2
```

Remaining:

```text
[3,4,5,1]
```

---

## Why `while len(q) > 1`?

Continue until only one player remains.

Example:

```text
[3,5]
len = 2
2 > 1 → True
```

Continue.

Finally:

```text
[3]
len = 1
1 > 1 → False
```

Stop.

Winner:

```text
3
```
