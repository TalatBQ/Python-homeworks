#  1. Create a list containing five different fruits and print the third fruit.

fruits = ["apple", "peach", "banana", "melon", "blueberry"]
print("Third fruit:", fruits[2])


# 2. Create two lists of numbers and concatenate them into a single list.

list1 = list(range(1, 11))

list2 = list(range(11, 21))

concatenated_list = list1 + list2  # Concatenate by using + 

print(list1)
print(list2)
print("concatenated_list:", concatenated_list)


list1.extend(list2) # Concatenate by using .extend() and updates the list1

print("concatenated_list:", list1)



# 3. Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

numbers = [10, 20, 30, 40, 50, 60, 70]

first = numbers[0] 
middle = numbers[len(numbers)//2]  # integer division to get middle index
last = numbers[-1]

new_list = [first, middle, last]

print(numbers)
print(new_list)


# 4. Create a list of your five favorite movies and convert it into a tuple.

five_favorite_movies = ["Jason Bourne", "Bourne Legacy", "Mission Impossible", "Time", "Valley of Wolves"]

print("tuple:", tuple(five_favorite_movies))



# 5. Given a list of cities, check if "Paris" is in the list and print the result.

list_of_cities = ["London", "Tashkent", "Paris", "Chicago", "Arizona"]


# Check if "Paris" is in the list
if "Paris" in list_of_cities:
    print("Paris is in the list of cities")
else:
    print("Paris is not in the list of cities")



# 6. Create a list of numbers and duplicate it without using loops.

numbers = list(range(1, 8))

duplicated_list = numbers * 2   # Duplicate the list using multiplication

print(numbers)
print("Duplicated list", duplicated_list)



# 7. Given a list of numbers, swap the first and last elements.

numbers = [1, 2, 3, 4, 5]

numbers[0], numbers[-1] = numbers[-1], numbers[0]  # Swap first and last elements

print("After swapping first and last:", numbers)



# 8. Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

tuple_of_numbers = tuple(range(1, 11))  # Create a tuple of numbers from 1 to 10

sliced_tuple = tuple_of_numbers[3:7] # Slice from index 3 to 7 (index 3 inclusive, 7 exclusive)

print("tuple_of_numbers:", tuple_of_numbers)
print("sliced_tuple from index 3 to 7:", sliced_tuple)


# 9. Create a list of colors and count how many times "blue" appears in the list.

colors = ['red', 'blue', 'white', 'yellow', 'blue']

count_blue = colors.count('blue')  # Count how many times "blue" appears

print("Times of appearing of 'blue':", count_blue)



# 10. Given a tuple of animals, find the index of "lion".

animals = ('rabbit', 'cobra', 'monkey', 'lion', 'giraffe')

index = animals.index('lion')

print("Index of 'lion':", index)



# 11. Create two tuples of numbers and merge them into a single tuple.

num1 = tuple(range(1, 6))
num2 = tuple(range(6, 11))

merged_tuple = num1 + num2  ##  Merging by operator (+)

print("tuple_1:", num1)
print("tuple_1:", num2)
print("Merged tuple:", merged_tuple)

M = tuple((*num1, *num2))   ##  Merging by unpacking operator (*)

print("Merged tuple:", M)



# 12. Given a list and a tuple, find and print their lengths.

list = [1, 2, 3, 4, 5, 6, 7, 8]
tuple = (10, 20, 30, 40, 50)

list_length = len(list)
tuple_length = len(tuple)

print("Length of list:", list_length)
print("Length of tuple:", tuple_length)



# 13. Create a tuple of five numbers and convert it into a list.

numbers = range(50, 56)

print(list(numbers))




# 14. Given a tuple of numbers, find and print the maximum and minimum values.

numbers = (8, 12, 55, 3, 43, 29)

max_value = max(numbers)  # max value
min_value = min(numbers)  # min value

print("Maximum value:", max_value)
print("Minimum value:", min_value)



# 15. Create a tuple of words and print it in reverse order.

words = ('book', 'tea', 'pencil', 'state', 'chicago')

rev = words[::-1]

print("Reverse order of the tuple:", rev)









