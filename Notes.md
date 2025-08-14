# Here I have stored some of my learnings while making this project :)

## Python Packages and **init**.py

- `__init__.py` files mark a folder as a Python package, allowing you to import modules from it.
- They can be empty or contain initialization code for the package.
- Organizing code into multiple files and folders (with `__init__.py`) is better for larger projects, making code easier to manage and reuse.
- Functionality can be the same as writing all code in one file, but splitting code improves readability and maintainability.

---

**Error:** `AttributeError: 'tuple' object has no attribute 'append'`

**Cause:** `.append()` works only on lists. Tuples are immutable and do not have this method.

**Common Mistake:** Accidentally creating a tuple instead of a list:

```python
papers = ()       # tuple
papers = [],      # tuple (due to trailing comma)
```

**Fix:** Use square brackets without a trailing comma:

```python
papers = []
authors = []
seen_author_ids = set()
```

**Key Point:**

* **List:** mutable, uses `[]`
* **Tuple:** immutable, uses `()`

---




