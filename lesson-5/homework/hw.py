# 1.  Python program to determine whether a given year is a leap year

year = int(input("Enter a year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")



# 2. Given an integer, `n`, perform the following conditional actions:

#- If `n` is **odd**, print `Weird`
#- If `n` is **even** and in the inclusive range of **2 to 5**, print `Not Weird`
#- If `n` is **even** and in the inclusive range of **6 to 20**, print `Weird`
#- If `n` is **even** and **greater than 20**, print `Not Weird`


n = int(input("Enter a number:"))

if n % 2 == 1:
    print("Weird")
if n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
if n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
if n % 2 == 0 and n > 20:
    print("Not Weird")



# 3. Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop. 
    # Give two solutions.
    
    

# Solution 1 with if-else statement.
a = int(input("enter a: "))
b = int(input("enter b: "))

if a % 2 != 0:  
    a = a + 1     # If a is odd → move to the next even number

evens = list(range(a, b+1, 2))  # jumps by 2 (only evens)

print("Even numbers: ", evens) 



# Solution 2 without if-else statement.

a = a + (a % 2)

evens = list(range(a, b+1, 2))

print("Even numbers: ", evens) 
