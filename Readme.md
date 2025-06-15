# Order Displacement Distance

This repository contains the Python implementation of the **Order Displacement Distance** algorithm, a metric designed to quantify the positional displacement of common elements between two ordered lists. It also includes utility functions to apply this metric to data loaded from CSV files, making it suitable for analyzing and comparing rankings or ordered sequences.

---

## What is Order Displacement Distance?

The Order Displacement Distance is a normalized metric that provides a value between 0 and 1:

* **0** indicates **no displacement** among common elements in the two lists.

* **1** signifies the **maximum possible displacement** for those common elements.

Unlike traditional sequence alignment algorithms that consider insertions, deletions, and substitutions, this algorithm focuses specifically on how much the relative positions of *shared items* have shifted between two lists. It is particularly useful for comparing the ordering preferences or sequences where the presence of an item is important, but its exact position relative to non-common items is less critical than its displacement relative to other common items.

---

## Algorithm Details

The core algorithm, `order_displacement_dist`, works as follows:

1.  **Identify Common Elements:** It first identifies all elements present in both input lists.

2.  **Calculate Current Displacement:** For each common element, it calculates the absolute difference between its index in the first list and its index in the second list. These individual differences are summed to get the total `current_displacement_sum`.

3.  **Calculate Maximum Possible Displacement:** To normalize the `current_displacement_sum`, the algorithm determines the `max_possible_displacement_sum`. This is achieved by sorting the original indices of the common elements from both lists and then pairing them in a way that maximizes their absolute positional differences (e.g., the smallest index from list A's common elements is paired with the largest index from list B's common elements).

4.  **Normalize:** The final `order_displacement_distance` is `current_displacement_sum` divided by `max_possible_displacement_sum`.

The algorithm also provides an output of the most displaced common items, ordered by their individual displacement values.

---
## Usage
`order_displacement_dist(a, b)`
```python

# This function calculates the normalized displacement distance between two Python lists.

from order_displacement_distance import order_displacement_dist

a = ['a', 'b', 'c', 'd']
b = ['a', 'd', 'c', 'b']

distance = order_displacement_dist(a, b)
print(f"Normalized Displacement Distance: {distance}")
#Expected output for the given example would show a displacement for 'b', 'c', and 'd' and print the overall normalized distance.
```