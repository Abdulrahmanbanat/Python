# NumPy Basics Summary

This file includes summarized notes and concepts from working with **NumPy**, **Pandas**, and **Matplotlib** in Python. It also contains basic tasks and exercises for learning and practice.

---

## Contents

- Pandas Basics  
- NumPy Arrays  
- Creating Arrays  
- Built-in Methods  
- Array Shape, Size, and Reshaping  
- Indexing & Selection  
- Broadcasting  
- NumPy Operations  
- Universal Functions  
- Practice Tasks  

---

## Pandas Basics

- Create a DataFrame using dictionaries with lists (e.g. names, ages, salaries).  
- Use `.head()`, `.info()`, `.describe()` and `.columns` to explore your data.  
- Read CSV files using `read_csv()`.  
- Select columns or filter rows based on conditions.  

---

## NumPy Arrays

- NumPy is a powerful linear algebra library in Python used for handling arrays, matrices, and numerical operations.  
- NumPy arrays are faster and more efficient than Python lists.  
- Common array types:  
  - 1D Arrays (Vectors)  
  - 2D Arrays (Matrices)  

---

## Creating Arrays

- Convert Python lists or nested lists to NumPy arrays.  
- Use built-in methods to create arrays:  
  - `arange`  
  - `zeros`, `ones`  
  - `linspace`, `eye`, `identity`  
  - Random generators: `rand`, `randn`, `randint`  

---

## Shape, Size, and Reshape

- `.shape` gives dimensions of the array.  
- `.size` gives total number of elements.  
- Use `.reshape()` to change the structure of the array.

---

## Indexing & Selection

- Index individual elements using brackets.  
- Slice arrays to get ranges.  
- Use boolean conditions to filter values.  
- 2D arrays can be indexed using `[row, col]`.  

---

## Broadcasting

- NumPy allows broadcasting operations like assigning a value to a range of indices.  
- Changes to slices affect the original array unless `.copy()` is used.  

---

## NumPy Operations

- Perform arithmetic between arrays or with scalars.  
- Example operations: `+`, `-`, `*`, `/`, `**`  
- Division by zero returns `nan` or `inf` (not an error).  

---

## Universal Functions

- NumPy provides built-in functions that work on entire arrays:
  - `sqrt()`, `exp()`, `log()`, `cos()`, `max()`, `min()`, etc.

---

## Practice Tasks

1. Create arrays of zeros, ones, or fives.  
2. Generate arrays with even numbers or linearly spaced values.  
3. Create identity matrices or random arrays.  
4. Use indexing to select values from matrices.  
5. Calculate sum, mean, standard deviation of arrays.  

---

## Key Takeaways

- NumPy and Pandas are foundational libraries for data analysis and numerical computing in Python.  
- NumPy arrays are efficient and support powerful operations.  
- Learning how to manipulate and understand arrays is critical for data science and machine learning.

---
