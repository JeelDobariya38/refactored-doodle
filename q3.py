"""
# 🌱 Question 3 — Two things, one sentence

Write a program that:
- takes two inputs:
  - your city
  - your country
- stores them in variables
- prints them together in one sentence

```md
I live in Doraemon World, Japan.
```



## Understanding

take two user inputs, city & country. then just, store & print them.



## Edge Cases

No, edge case for such a simple thing...
We will assume, user will input a correct names and w'll go with it (print it)...



## Brute Force Approach

Time:  O(1) ->  ≈3 ms
Space: O(1) ->  ≈N+M bits (N = No. of character user inputs for city & M = character for country)

```python
city = input("Enter name of a city: ")
country = input("Enter name of a country: ")
print(f"I live in {city}, {country}.")
```



## Optimized Solution

...

Time:  O(1) ->  ≈3 ms
Space: O(1) ->  ≈N+M bits (N = No. of character user inputs for city & M = character for country)

```python
# No optimization possible!!
city = input("Enter name of a city: ")
country = input("Enter name of a country: ")
print(f"I live in {city}, {country}.")
```

"""

city = input("Enter name of a city: ")
country = input("Enter name of a country: ")
print(f"I live in {city}, {country}.")
