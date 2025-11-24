#1. Age Calculator

from datetime import date

# Ask for user input
Name = input("enter the name:")
Year_of_birth = int(input("enter the year of birth:"))

# Calculate age
current_year = date.today().year
age = current_year - Year_of_birth

# Display result
print(f'Hello, {Name}! You are {age} years old.')



#2. Extract Car Names

txt = 'LMaasleitbtui'

# Har 2-belgini olish, 1-indeksdan boshlab
car_name1 = txt[1::2]

# Har 2-belgini olish, 0-indeksdan boshlab
car_name2 = txt[0::2]

print("car1:", car_name1)
print("car2:", car_name2)


#3. Extract Car Names

txt = 'MsaatmiazD'

# Har 2-belgini olish, 0-indeksdan boshlab
car_name1 = txt[0::2]

# Har 2-belgini olish, 1-indeksdan boshlab
car_name2 = txt[1::2][::-1]     #[::-1] — stringni teskari aylantiradi.

print("car1:", car_name1)
print("car2:", car_name2)

#4. Extract Residence Area

txt = "I'am John. I am from London"

# from so'zini topamiz
keyword = "from "
start = txt.find(keyword)

# Agar "from" topilsa, undan keyingi so'zni (joy nomini) olamiz
if start != -1:
    residence = txt[start + len(keyword):]
    print("Residence area:", residence)
else:
    print("Residence area is not found")


# 5. Reverse String

text = input("Enter a string: ")

reversed_text = text[::-1]  # reverse the string

print("Reversed text:", reversed_text)


# 6. Count Vowels

text = input("Enter a string: ")

vowels ="aeiouAEIOU" # all possible vowels (both cases)
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of count vowels:", count)


# 7. Find Maximum Value

nums = list(map(int, input("Enter numbers separated by space: ").split()))

print("Maximum value is:", max(nums))


# 8. Check Palindrome

word = input("Enter a word: ")

word = word.lower() # Convert the word to lowercase to handle case-insensitivity

# Reverse the word
rev = word[::-1]

# Check if same
if word == rev:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")


# 9. Extract Email Domain

# Foydalanuvchidan email kiritishni so'rash
email = input("Enter your email address: ")

# Emailni tekshirish
if '@' in email and email.count('@') == 1:  # Emailda @ borligini va faqat bitta ekanligini tekshiradi.
    domain = email.split('@')[1]  # Agar @ mavjud bo‘lsa va to‘g‘ri joylashgan bo‘lsa, split('@')[1] yordamida domainni ajratadi.
    if domain:  # domain bo'sh emasligini tekshirish
        print("Domain:", domain)
    else:
        print("Error: Domain part is missing!")  # Agar @ bo'lsayu, lekin @ dan keyingi qismi bo'lmasa, xatolik xabarini beradi.
else:
    print("Error: Invalid email address. '@' is missing or used multiple times.")  #  Agar @ yo‘q yoki bir nechta bo‘lsa, foydalanuvchiga xatolik haqida ogohlantiradi.



# 10. Generate Random Password

import random
import string

# Parol uzunligini so'rash
length = int(input("Enter the desired password length (minimum 6): "))

if length < 6:
    print("Password length should be at least 6 for security.")
else:
    # Belgilar to'plami
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # Har doim 1 harf, 1 raqam, 1 maxsus belgi qo'shamiz
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special)
    ]

    # Qolgan belgilarni tasodifiy tanlash
    all_chars = letters + digits + special
    password += [random.choice(all_chars) for _ in range(length - 3)]

    # Belgilarni aralashtirish
    random.shuffle(password)

    # Ro'yxatni satrga aylantirish
    password = ''.join(password)

    print("Generated secure password:", password)


