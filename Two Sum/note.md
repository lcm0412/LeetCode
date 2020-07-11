## Optimal Solution - One-pass Hash Table
It turns out we can do it in one-pass. While we iterate and inserting elements into the table, we also look back to check if current element's complement already exists in the table. If it exists, we have found a solution and return immediately.

## Complexity Analysis
- Time complexity : $O(n)$. We traverse the list containing $n$ elements only once. Each look up in the table costs only $O(1)$ time.
- Space complexity : $O(n)$. The extra space required depends on the number of items stored in the hash table, which stores at most $n$ elements.

---

## Why sorting is faster than O(n) Hashmap solution
### author: msadler
### March 6, 2019 2:17 PM

I think it is highly dependent on test case input size and how sorted the input already is..

This code could finish with a "faster" O(N) than the hashMap implementation.
The reason for this is because:

```
Adding all elements to a HashMap
// iterating over all the ints in nums  [Always O(N)]
// adding all the elements from nums to a new data structure [Always O(N)]
// then comparing.. could be O(1)

Sorting elements then comparing values
// sorting  [could be O(N) comparisons, O(1) swaps]
// ^ this case happens when nums.length < 17 and nums was already sorted.. for explanation check source code of arrays.sort()
// (NOTE: here we skip the step of adding elements to another data structure)
// then comparing.. could be O(1)
```

We assume adding/setting an element in a data structure will take a split second longer in time then just looking at an index. So the sorting implementation could take split seconds less than the hashMap implementation depending on nums.

Hence, if nums.length < 17 and nums is fairly sorted, then we can expect that example to finish faster with this implementation..

However, if there are mostly huge, anti-sorted cases then hashMap will likely be faster.

Now we can assume that a majority of the test-cases are small input arrays because hashMap is slower.
