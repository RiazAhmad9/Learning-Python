"""
nutrition.py
-----------------
Looks up and prints the calorie count of a fruit from a predefined dictionary.

- .strip().lower(): normalises input — handles whitespace and case
- if n in fruits: only prints if fruit is found, silently ignores unknown inputs
- fruits[n]: direct dictionary lookup by key
"""
fruit = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 280,
}


item = input("Item: ").strip().lower()
if item in fruit:
    print(f"Calories: {fruit[item]}")