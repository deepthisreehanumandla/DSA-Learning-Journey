# 📌 Problem: Best Time to Buy and Sell Stock

* LeetCode #: 121
* Approach: Greedy (Single Pass)

--- 

## 🧠 Intuition

We want to **buy at the lowest price** and **sell at the highest price after that**.

👉 Track minimum price so far  
👉 Calculate profit at each step

---

## ⚙️ Approach

1. Initialize:
   - `minPrice = ∞`
   - `maxProfit = 0`
2. Traverse prices:
   - Update `minPrice = min(minPrice, price)`
   - Calculate profit = `price - minPrice`
   - Update `maxProfit`
3. Return maxProfit

---

## 💻 Code (Python)

```python
class Solution:
    def maxProfit(self, prices):
        minPrice = float('inf')
        maxProfit = 0

        for price in prices:
            minPrice = min(minPrice, price)
            profit = price - minPrice
            maxProfit = max(maxProfit, profit)

        return maxProfit
