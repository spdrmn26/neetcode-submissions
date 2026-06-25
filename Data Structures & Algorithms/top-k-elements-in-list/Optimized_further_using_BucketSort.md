Here is the ultimate, $O(N)$ Big Tech solution. When you pull this out in a Google or Meta interview after discussing the $O(N \log N)$ sorting method, it signals that you truly understand memory allocation and algorithm optimization.

Here is the complete deep-dive on the **Bucket Sort** method, perfectly formatted for your GitHub `README.md`.

```markdown
# 🧠 Deep Dive: Top K Frequent Elements (The O(N) Bucket Sort Optimization)

While solving the Top K Frequent Elements problem in $O(N \log N)$ time using standard sorting is good, Big Tech interviewers (Google, Meta, Microsoft) will push you for an $O(N)$ time complexity solution. 

To achieve strictly $O(N)$ time, we must abandon standard sorting algorithms entirely. Instead, we use a technique called **Bucket Sort**.

---

## ⚙️ 1. The Core Mechanic: Index as Frequency

In a normal array, the index just represents the position of an item (0st, 1st, 2nd...). 
In Bucket Sort, we hack the array structure: **We use the *index* of the array to represent the *frequency* of an element.**

### The Logic Breakdown:
Imagine our input array is `nums = [1, 1, 1, 2, 2, 3]`.

1. **Count Frequencies:** Just like before, we use a Hash Map to count occurrences.
   `counts = {1: 3, 2: 2, 3: 1}`

2. **The Upper Bound (The Trick):** What is the maximum possible frequency any number could have? If an array has $N$ elements, the absolute maximum frequency is $N$ (e.g., if the array is `[1, 1, 1, 1]`, the number `1` appears 4 times). 
   Therefore, we can create an empty array of arrays (buckets) of size $N + 1$.

3. **Mapping to Buckets:** We iterate through our Hash Map and drop each number into the bucket that matches its frequency.
   * Number `3` appears `1` time $\rightarrow$ Drop it into `bucket[1]`
   * Number `2` appears `2` times $\rightarrow$ Drop it into `bucket[2]`
   * Number `1` appears `3` times $\rightarrow$ Drop it into `bucket[3]`

### Visualizing the Buckets in Memory:
| Index (Frequency) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Values (Numbers)** | `[]` | `[3]` | `[2]` | `[1]` | `[]` | `[]` | `[]` |

---

## 🚀 2. Extracting the Top K

Because the indices themselves represent the frequencies, the array is **already sorted by frequency without us ever running a sorting algorithm!**

To get the Top K most frequent elements, all we have to do is loop through this bucket array **backwards** (starting from the highest possible frequency at the end of the array) and gather the numbers until we have exactly $K$ elements.

---

## 💻 3. The Final O(N) Python Implementation

Here is the production-grade, optimal solution. 

```python
import collections
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count the frequencies in O(N) time
        count = collections.defaultdict(int)
        for num in nums:
            count[num] += 1
            
        # 2. Create the buckets. We need N + 1 buckets to account for 0 frequency up to N frequency.
        # This creates a list of empty lists.
        freq_buckets = [[] for _ in range(len(nums) + 1)]
        
        # 3. Map numbers to their corresponding frequency bucket in O(N) time
        # dict.items() gives us (number, frequency)
        for num, frequency in count.items():
            freq_buckets[frequency].append(num)
            
        # 4. Gather the top K elements by iterating backwards in O(N) time
        res = []
        for i in range(len(freq_buckets) - 1, 0, -1): # Start at end, stop at 1, step backwards
            for num in freq_buckets[i]:
                res.append(num)
                # The moment we have K elements, we are completely done
                if len(res) == k:
                    return res
                    
        return res

```

### **Complexity Analysis:**

* **Time Complexity:** $O(N)$. We iterate through the array to count elements $O(N)$, iterate through the dictionary to place them in buckets $O(N)$, and iterate backwards through the buckets $O(N)$. Total time is strictly linear!
* **Space Complexity:** $O(N)$. We allocate memory for the Hash Map and the `freq_buckets` array, both of which scale linearly with the size of the input array.

```

***

### 🧠 The "Job-Country Switch 2027!" Interview Check
When you write `freq_buckets = [[] for _ in range(len(nums) + 1)]`, an interviewer might ask: *"Why did you use list comprehension here instead of just writing `[[]] * (len(nums) + 1)`?"* Do you know the subtle Python memory trap that makes `[[]] * N` dangerous when creating nested lists?

```
