# 1. How to Declare and Use Variables

# Integer variable
age = 25

# Float variable
height = 5.9

# String variable
name = "Tobi"

# Boolean variable
is_student = True


# 2. Print each variable along with its data type using the type() function


# output prints <class 'int'>
age = 25
print(type(age))

# output prints <class 'float'>
height = 5.9
print(type(height))

# output prints <class 'string'>
name = "oluwatobi"
print(type(name))

# output prints <class 'bool'>
is_student = True
print(type(is_student))


# 3. Use if, elif, and else for decision making.



#output prints your're an adult, hence you can vote

age = 18
if age < 13:
    print("you are a child, hence can't vote.")
elif age > 20:
    print("you are a teenager, hence you can vote. ")
else:
    print("you're an adult, hence can vote.")

#output prints you are a teenager, hence you can vote.

age = 18
if age < 13:
    print("you are a child, hence can't vote.")
elif age < 20:
    print("you are a teenager, hence you can vote. ")
else:
    print("you're an adult, hence can vote.")


# 4. Write a for loop that prints numbers from 1 to 10

# output prints 1,2,3,4,5,6,7,8,9,10

for number in range (1, 11):
    print(number)
    

# Write a while loop that prints even numbers between 1 and 20    

# output prints 2,4,6,8,10,12,24,26,28,20

number = 2
while number <= 20:
    print(number)
    number += 2


# 5. Create a list of 5 fruits.

# output prints list of 5 fruits in upper case

fruits = ["apple", "banana", "mango", "orange", "grape"]
for fruit in fruits:
    print(fruit.upper())
    if fruit == "banana":
      
    
    
# If the fruit is "banana", skip it using continue.


#output prints list of fruits in uppercase and ommit banana   

fruits = ["apple", "banana", "mango", "orange", "grape"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit.upper())
    

   

   

     
    