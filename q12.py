"""
# 🌱 Question 12 — The Age Check

- Ask the user for their age.
- If the age is 18 or more, print:
    You are an adult.
- Else, print:
    You are a minor.

(No validation. Assume the input makes sense.)



## Understanding

Ask user's age & print the status


## Edge Cases

Following assume that `(No validation. Assume the input makes sense.)` not read by you:

> User may even enter a negative number or zero as age.. but i guess we will ignore..
> We can even write if else for check that.. I guess it not needed as someone, who is -2 year is still a minor, either ways.. 
>
> (anyways, the optimized code cover this edge cases)



## Brute Force Approach

Time:  O(1) ->  ≈3 ms
Space: O(1) ->  ≈N bits (N = total No. of character user inputs)

```python
age = int(input("age: "))

if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")
```



## Optimized Solution


Time:  O(1) ->  ≈3 ms
Space: O(1) ->  ≈N bits (N = total No. of character user inputs)

```python
age = int(input("age: "))

# if age <= 0:
#     print("You have entered a invalid age but anyways...")

print(f"You are a {'adult' if age >= 18 else 'minor'}.")
```

"""

age = int(input("age: "))

# if age <= 0:
#     print("You have entered a invalid age but anyways...")

print(f"You are a {'adult' if age >= 18 else 'minor'}.")
