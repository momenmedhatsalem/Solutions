# Programming Exercises - Solutions and Explanations

**Student:** Momen Medhat Salem  
**Date:** December 13, 2025

---

## Overview

This document provides detailed explanations for all four debugging exercises, including the bugs identified, my debugging methodology, and the implemented solutions.

---

## Exercise 1: id_to_fruit Function

### Problem Description
The function was supposed to return a fruit name at a specific index from a set of fruits. However, it returned inconsistent results across different runs.

### Bug Identified
**Root Cause:** Python sets are **unordered data structures**. The iteration order is not guaranteed to be consistent, which means accessing elements by index is unreliable.

When the function iterated through the set with:
```python
for fruit in fruits:
```
The order could change between executions, making it impossible to reliably get "orange" at index 1 or "kiwi" at index 3.

### Solution
Convert the set to a **sorted list** to ensure consistent, predictable ordering:

```python
fruits_list = sorted(list(fruits))
```

This guarantees that:
- The same input always produces the same output
- Index-based access works consistently
- The alphabetical ordering makes it testable

### Why This Works
By converting to a sorted list, we transform an unordered collection into an ordered sequence. The `sorted()` function ensures alphabetical ordering, so index 0 will always be "apple", index 1 will be "kiwi", etc.

**File:** `exercise1_fixed.py`

---

## Exercise 2: swap Function

### Problem Description
The function was intended to swap x and y coordinates in bounding box arrays, but the coordinates were corrupted after the swap operation.

### Bugs Identified

**Bug 1 (Obvious Error):** In the original line:
```python
coords[:, 0], coords[:, 1], coords[:, 2], coords[:, 3], = coords[:, 1], coords[:, 1], coords[:, 3], coords[:, 2]
```
- `coords[:, 1]` appears **twice** on the right side
- This means column 0 gets the value from column 1, but column 1 also gets column 1 (no swap!)
- Should be: `coords[:, 0]` from the right side

**Bug 2 (Subtle Error):** Even after fixing Bug 1, simultaneous assignment can cause issues when modifying the same array in-place. Without creating a copy first, intermediate values during the tuple unpacking can overwrite data needed for subsequent assignments.

### Solution
1. Create a copy of the array to avoid in-place modification issues
2. Fix the assignment to properly swap x1↔y1 and x2↔y2:

```python
coords = coords.copy()
coords[:, 0], coords[:, 1], coords[:, 2], coords[:, 3] = coords[:, 1], coords[:, 0], coords[:, 3], coords[:, 2]
```

### Why This Works
- The copy ensures the original array isn't modified
- The corrected assignment properly swaps: column 0↔1 (x1↔y1) and column 2↔3 (x2↔y2)
- Column 4 (class ID) remains unchanged

**File:** `exercise2_fixed.py`

---

## Exercise 3: plot_data Function

### Problem Description
The precision-recall curve was plotted incorrectly. When comparing the CSV data values with the displayed plot, the axes didn't match the actual data.

### Bug Identified
**Root Cause:** The plot command had **swapped axes**:

```python
plt.plot(results[:, 1], results[:, 0])  # Wrong: recall on x, precision on y
plt.xlabel('Recall')
plt.ylabel('Precision')
```

The CSV file has columns in order: [precision, recall]
- `results[:, 0]` = precision (should be x-axis)
- `results[:, 1]` = recall (should be y-axis)

But the plot was using column 1 for x and column 0 for y, while the labels claimed the opposite.

### Solution
Fix both the plot call AND the axis labels:

```python
plt.plot(results[:, 0], results[:, 1])  # Correct: precision on x, recall on y
plt.xlabel('Precision')
plt.ylabel('Recall')
```

### Why This Works
Now the data columns match their axis labels: precision (column 0) on the x-axis and recall (column 1) on the y-axis. The plot correctly represents the precision-recall relationship.

**File:** `exercise3_fixed.py`

---

## Exercise 4: train_gan Function

### Problem Description
The GAN training code worked fine with `batch_size=32` but crashed with `batch_size=64`, producing the error:
```
ValueError: Using a target size (torch.Size([128, 1])) that is different to the input size (torch.Size([96, 1]))
```

Additionally, there was a cosmetic bug in how results were displayed.

### Bugs Identified

**Bug 1 (Structural - Critical):**
The code hardcoded `batch_size` when creating tensors:
```python
real_samples_labels = torch.ones((batch_size, 1))
```

**Problem:** The MNIST dataset has 60,000 images. With `batch_size=64`:
- 60,000 ÷ 64 = 937.5 batches
- The last batch only has 32 images (60,000 % 64 = 32)
- But the code still creates tensors with size 64, causing a mismatch

**Bug 2 (Cosmetic):**
```python
if n == batch_size - 1:
```
This condition compares the batch index `n` with `batch_size - 1`. This makes no logical sense:
- `n` is the iteration number (0, 1, 2, ... up to ~937 batches)
- `batch_size` is 32 or 64
- They're completely different scales

### Solutions

**Fix 1:** Use the actual batch size dynamically:
```python
current_batch_size = real_samples.size(0)
real_samples_labels = torch.ones((current_batch_size, 1))
```
This ensures all tensors match the actual number of samples in each batch, including the last partial batch.

**Fix 2:** Use a sensible display condition:
```python
if n % 50 == 0:
```
This displays results every 50 batches, providing periodic updates throughout training.

### Why This Works
- `real_samples.size(0)` returns the actual number of samples in the current batch
- All tensors are created with matching dimensions
- Works correctly for both full batches and the final partial batch
- The periodic display gives meaningful progress updates

**File:** `exercise4_fixed.py`

---

## Recommended Files for Review

I recommend reviewing these two files as they best demonstrate my programming capabilities:

### 1. exercise4_fixed.py (Primary Recommendation)
**Complexity demonstrated:**
- Object-oriented programming with PyTorch neural networks
- Understanding of deep learning architectures (GAN with Generator and Discriminator)
- Tensor operations and GPU/CPU device management
- Debugging complex training loops with dynamic batch sizes
- Error handling and fallback mechanisms (MNIST download URLs)
- Data visualization with matplotlib
- Understanding of the interaction between multiple components in a ML pipeline

**Why this file:** It shows I can work with modern deep learning frameworks, understand neural network architectures, and debug sophisticated issues in production-quality ML code.

### 2. exercise2_fixed.py (Secondary Recommendation)
**Complexity demonstrated:**
- NumPy array operations and slicing
- Understanding of memory management (copy vs. view)
- Debugging subtle concurrency issues in simultaneous assignments
- Working with multi-dimensional data structures

**Why this file:** It demonstrates strong fundamentals in scientific computing and attention to subtle bugs that could cause serious issues in production code.

---

## Debugging Methodology

My approach to solving these exercises:

1. **Understand the expected behavior** - Read documentation and test cases carefully
2. **Reproduce the issue** - Run the code and observe the actual vs. expected output
3. **Identify the root cause** - Trace through the logic to find where behavior diverges
4. **Implement the fix** - Make minimal, targeted changes to address the root cause
5. **Verify the solution** - Test with multiple inputs including edge cases
6. **Document the fix** - Add comments explaining what was wrong and why the fix works

---

## Conclusion

These exercises required understanding of:
- Python data structures and their properties (ordered vs. unordered)
- NumPy array operations and memory management
- Data visualization and axis conventions
- Deep learning frameworks and tensor operations
- Debugging systematic vs. edge-case failures

Each bug was identified through careful analysis of the expected behavior, actual output, and systematic code review. The solutions are minimal, targeted, and well-documented.
