"""
# 🌱 Question 6 — The Confused Greeter

A terminal greeter is broken. It asks for a name, but it wants to speak before and after the input.

Write a program that:
- prints: `Welcome! Please tell me your name`.
- takes the user’s name as input
- prints: `Nice to meet you, <name>`

(Looks easy — but follow the order exactly.)



## Understanding

Make a the program that respects formatting...
And prints the statements in order given by question...



## Edge Cases

No edge case, for such a simple thing...



## Brute Force Approach

Time:  O(1) ->  ≈3 ms
Space: O(1) ->  ≈N bits (N = total No. of character user inputs)

```python
print("Welcome! Please tell me your name")
name = input()
print(f"Nice to meet you, {name}")
```



## Optimized Solution

Time:  O(1) ->  ≈3 ms
Space: O(1) ->  ≈N bits (N = total No. of character user inputs)

```python
# No optimizion possible
print("Welcome! Please tell me your name")
name = input()
print(f"Nice to meet you, {name}")
```

"""

print("Welcome! Please tell me your name")
name = input()
print(f"Nice to meet you, {name}")
