"""
# 🌱 Question 14 — The Mood Detector

- Ask the user:
    How are you feeling today?
- If the answer is happy, print:
    I’m glad to hear that!
- Else:
    I hope your day gets better.



## Understanding

Ask about user's mood, print message accordingly.



## Edge Cases

user might enter different word then happy. that more less sau user s in good mood.
like a user might say he feeling playful or hungry,
in such case the response "I hope your day gets better." doesn't make sense.
but let ignore that for time being.

other then that a user might also type the letter in different case like
happy -> Happy



## Brute Force Approach

Time:  O(1) ->  ≈4 ms
Space: O(1) ->  ≈N bits (N = total No. of character user inputs)

```python
mood = input("How are you feeling today? ")

if mood.lower() == "happy":
    print("I’m glad to hear that!")
else:
    print("I hope your day gets better.")
```



## Optimized Solution

No optimizion possible

Time:  O(1) ->  ≈4 ms
Space: O(1) ->  ≈N bits (N = total No. of character user inputs)

```python
mood = input("How are you feeling today? ")

if mood.lower() == "happy":
    print("I’m glad to hear that!")
else:
    print("I hope your day gets better.")
```

"""

mood = input("How are you feeling today? ")

if mood.lower() == "happy":
    print("I’m glad to hear that!")
else:
    print("I hope your day gets better.")
