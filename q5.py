"""
# 🌱 Question 5 — A tiny self-introduction

Write a program that:
- asks for:
  - name
  - age
- stores both in variables
- prints a small introduction sentence

```md
Hello Jeel, 
But I don't believe, you are just 16.
```



## Understanding

take name & age as user inputs, then just, store & print them.



## Edge Cases

No, edge case for such a simple thing...
We will pretend, user will input is correct & vaild input and w'll go with it (print it)...



## Brute Force Approach

Time:  O(1) ->  ≈5 ms
Space: O(1) ->  ≈N bits (N = total No. of character user inputs)

```python
name = input("name: ")
age = int(input("age: "))

print(f"Hello {name},")
print(f"But I don't believe, you are just {age}.")
```



## Optimized Solution

There was no need for converting age into int we can directly use string.
This saves us -1ms.. because there is no `int()`...

Also, there was no need for two print statements...
This saves another -1ms.. because I guess, there is just one syscall...

Time:  O(1) ->  ≈3 ms
Space: O(1) ->  ≈N bits (N = total No. of character user inputs)

```python
name = input("name: ")
age = input("age: ")
print(f"Hello {name},\nBut I don't believe, you are just {age}.")
```

"""

name = input("name: ")
age = input("age: ")
print(f"Hello {name},\nBut I don't believe, you are just {age}.")
