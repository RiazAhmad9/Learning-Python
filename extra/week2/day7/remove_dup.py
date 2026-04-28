"""
remove_duplicates
--------------------
Removes duplicates from a list while preserving the original order.

- dict.fromkeys(items): creates a dict using list items as keys — duplicates
  are dropped since dict keys must be unique, and insertion order is preserved
- list(): converts the dict keys back into a list
- if __name__ == "__main__": ensures main() only runs when executed directly
"""

def main():
    items = ["car", "bike", "boat", "plane", "rocket", "car", "car", "bike"]
    my_list = list(dict.fromkeys(items))
    for item in my_list:
        print(item)

if __name__ == "__main__":
    main()