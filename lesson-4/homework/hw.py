# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

scores_dict = {'Math': 90, 'DSA': 80, 'Algo': 95, 'Python': 75}

sorted_asc = dict(sorted(scores_dict.items(), key=lambda item: item[1])) # sorting values in ascending order

sorted_desc = dict(sorted(scores_dict.items(), key=lambda item: item[1], reverse=True)) # sorting values in descending order


print("Sorted by value asc:", sorted_asc)
print("Sorted by value desc:", sorted_desc)



# 2. Write a Python script to add a key to a dictionary.

sample_dict = {0: 10, 1: 20}

sample_dict.update({2: 30})


print("Updated_dict:", sample_dict)



# 3. Write a Python script to concatenate the following dictionaries to create a new one.

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# method 1
new_dict = {}

new_dict.update(dic1)
new_dict.update(dic2)
new_dict.update(dic3)

print("Concatenated dictionary:", new_dict)

# method 2
newd = {**dic1, **dic2, **dic3}
print("Concatenated dictionary:", newd)

# method 3
newdi = dic1 | dic2 | dic3
print("Concatenated dictionary:", newdi)



# 4. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

# Sample Dictionary (n = 5):

square_dict = {x: x*x for x in range(1, 6)}

print(square_dict)



# 5. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

my_dict = {x: x*x for x in range(1, 16)}

print(my_dict)



# 6. Write a Python program to create a set.

new_set = set(range(1, 10))

print(new_set)



# 7. Write a Python program to iterate over sets.


a = set("apple")

for i in a:
    print(i)




# 8. Write a Python program to add member(s) to a set.

my_set = {1, 2, 3, 4}

my_set.add(5)  # add a member

my_set.update([6, 7])  # add members

print(my_set)





# 9. Write a Python program to remove item(s) from a given set.

set777 = {12, 13, 14, 15, 16}

set777.discard(15) # removes one item and no error

set777.clear()  # removes all items



print(set777)



# 10. Write a Python program to remove an item from a set if it is present in the set.

set6 = {'one', 'two', 'three', 'four', 'five'}

item = "five"

if item in set6:
    set6.remove(item)
    print(f"{item} removed from the set.")
else:
    print("Item is not in the set")

