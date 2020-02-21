#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n). Because the code is linear. As the # of n goes up so to does the operations in proportion.

b) O(n^2) As the number of inputs increase, we perform two operations `for` and `while`

c) O(c^n) Recursive code of block where runtime will increase much faster than size of input.

## Exercise II

For this problem, we need to use `binary search` to find the highest floor that doesn't break the eggs.

Step 1 is to throw an egg from the middle floor by dividng n floors by 2.
Step 2 if egg breaks, we find the middle of floor of the bottom half of the building and throw it off there.
Step 2 if egg does NOT break, we find middle of the floor of the upper half of the building and throw it off there.
