import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
bst = BinarySearchTree(names_1[0])

# Replace the nested for loops below with your improvements

# Original runtime: 8.644546031951904 seconds

# Create a binary search tree with names from the first doc and then search it with the "contains" method.
for name_1 in names_1:
    bst.insert(name_1)
    
for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)

# New runtime: 0.2043600082397461 seconds 
# Changed the append to name_2 and the runtime improves again to 0.19469118118286133 seconds       

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
