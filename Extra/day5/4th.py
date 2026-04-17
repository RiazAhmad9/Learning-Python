# Removing duplicates from list
items = ["car", "bike", "boat", "plane", "rocket", "car", "car", "bike"]

def main():
    my_list = []
    # loop to check list for duplicate
    for item in items:
        if item not in my_list:
            my_list.append(item)
    # loop for printing line by line
    for i in my_list:
        print(i)
    
if __name__ == "__main__":
    main()