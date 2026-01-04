"""
# 🌱 Question 10 — The Polite Terminal

The terminal wants to be polite, but it can only do what you tell it.

Write a program that:
- asks the user for their name
- prints:
    Thank you.
- prints:
    Have a nice day, jeel3498.

(Yes, this is simple. Treat it with the same seriousness.)



## Understanding

Take user's name, then print it with fluff given in question.



## Edge Cases

No edge case, for such a simple thing...



## Brute Force Approach

Time:  O(1) ->  ≈3 ms
Space: O(1) ->  ≈N bits (N = total No. of character user inputs)

```python
name = input("name: ")

print("Thank you.")
print(f"Have a nice day, {name}.")
```



## Optimized Solution

May be one `print()` statement just make one syscall.. But I am not sure..

Time:  O(1) ->  ≈2 ms
Space: O(1) ->  ≈N bits (N = total No. of character user inputs)

```python
print("Thank you.", f"Have a nice day, {input("name: ")}.", sep="\n")
```

"""

print("Thank you.", f"Have a nice day, {input("name: ")}.", sep="\n")
