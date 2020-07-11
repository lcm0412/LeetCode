---
title: why sorting is faster than O(n) Hashmap solution
author: msadler
---

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
