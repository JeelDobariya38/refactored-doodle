"""
# 🌱 Question 4 — Pretend calculator (but no math yet)

Write a program that:
- asks the user for two numbers (as input)
- stores them in variables
- prints them exactly as entered, in one line

```md
You entered 5 and 10.
```

(Don’t calculate anything — just store and print)



## Understanding

take two number as user inputs, then just, store & print them.



## Edge Cases

No, edge case for such a simple thing...

We will pretend, user will input a number and not a alpha-numeric value.
and w'll go with it (print it)...



## Brute Force Approach

Time:  O(1) ->  ≈5 ms
Space: O(1) ->  ≈N bits (N = total No. of character user inputs)

```python
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
print(f"You entered {num1} and {num2}.")
```



## Optimized Solution

There was no need for converting the input in int we can directly use string.
Because then the number is just a alpha numeric string.

This optimizaton saves us -2ms.. because there is no `int()`.

Time:  O(1) ->  ≈3 ms
Space: O(1) ->  ≈N bits (N = total No. of character user inputs)

```python
num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
print(f"You entered {num1} and {num2}.")
```

"""

num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
print(f"You entered {num1} and {num2}.")
