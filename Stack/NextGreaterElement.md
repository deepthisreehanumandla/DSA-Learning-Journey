# 📌 Problem: Next Greater Element (All Variants)

* LeetCode #: 496 (and related variants)
* Approach: Stack (Monotonic Stack)

---

## 🧠 Intuition

The goal is to find the **next greater element to the right**.

Instead of checking every element (O(n²)), we use a **monotonic decreasing stack**:
- It keeps only useful elements
- Helps find next greater in **one pass**

---

# 🔹 Variant 1: Next Greater Element I (nums1 ⊂ nums2)

## ⚙️ Approach

1. Traverse `nums2`
2. Use stack to find next greater for each element
3. Store results in hashmap
4. Build answer for `nums1`
 
---

## 💻 Code (Python)

```python
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)

        for num in stack:
            next_greater[num] = -1

        return [next_greater[num] for num in nums1]
