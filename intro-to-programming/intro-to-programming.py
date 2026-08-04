print("Hours in a year:")
# There are 365 days in a year, 24 hours in a day
print(365 * 24)

# They can also be added at the end of the string
print("Hours in a year:")
print(365 * 24)  # There are 365 days in a year, 24 hours in a day

# input() function allows user input

name = input("What is your name?")
print("Hello, " + name)

name = input("what is your name?")  # This is some practice
print(name)
print(name)

# using multiple variables
first_name = input("What is your first name?")
last_name = input("What is your last name?")

print("Hello, " + first_name + " " + last_name + "!")
print(first_name + " " + last_name + " is quite a nice name.")

# More than one input

full_name = input("Enter Full Legal Name")
email = input("Enter Reliable Email Address")
nickname = input("What nickname do you go by?")

print("Let's make sure we got that right")
print("Your name:" + full_name)
print("Your email address:" + email)
print("Your nickname:" + nickname)

confirmation = input("Is this correct? YES / NO" " ")
print("Okay, thank you for fufilling our request. "
      "We will contact you within a 48 hour time-frame.")

# Practice
The_1st_part = input(" ")
The_2nd_part = input(" ")
The_3rd_part = input(" ")

print(The_1st_part + "-" + The_2nd_part + "-" + The_3rd_part + "!")

story_name = input("story name?")
story_year = input("story year?")
print(story_name + " is a valiant knight, born in the year " + story_year +
      ". One morning " + story_name + " woke up to an awful racket: a dragon was approaching the village. Only " +
      story_name + " could save the village's residents.")

# Day #2 variables
given_name = "Paul"
family_name = "Python"
name = given_name + " " + family_name
print(name)

word = input("Please type in a word: ")
print(word)
word = input("And another word: ")
print(word)
word = "third"
print(word)


word = input("Please type in a word: ")
print(word)

word = word + "!!!"
print(word)

number1 = 100
number2 = "100"

print(number1 + number1)
print(number2 + number2)

result = 10 * 25
print("The result is " + str(result))

result = 10 * 25
print("The result is", result)

# f-strings
result = 10 * 25
print(f"The result is {result}")

# All 3 Examples
name_fstring = input("name")
age_fstring = input("age")
city_fstring = input("city")
print(
    f"Hi {name_fstring}, you are "
    f"{age_fstring} years old. "
    f"You live in {city_fstring}."
)

name_str = input("name")
age_str = input("age")
city_str = input("city")
print(
    "Hi" + " " + str(name_str) + ", " + "you are " 
    + str(age_str) + ". " + "You live in" +
    str(city_str) + "."
)

name = input("name")
age = input("age")
city = input("city")
print("Hi", name, ", you are", age, "years old. You live in",
        city, ".")


# Arithmetic 

uno = 97
dos = 99
tres = 100
mean = (uno + dos + tres) / 3 
print(f"Mean: {mean}")


quiz1 = 90
quiz2 = 100 
quiz3 = 84
quiz4 = 105
mean = (quiz1 + quiz2 + quiz3 + quiz4) / 4 
print(f"Mean: {mean}")

height = 172.5
weight = 68.55

bmi = weight / (height / 100) ** 2
print(f"The BMI is {bmi}")

x = 3
y = 2

print(f"/ operator {x/y}")
print(f"// operator {x//y}")

# input strings

input_str = input("Which year were you born? ")
year = int(input_str)
print(f"Your age at the end of the year 2028: {2028 - year}")

# Alternative 
year = int(input("Which year were you born? "))
print(f"Your age at the end of the year 2028: {2028 - year}")

height = float(input("What is your height? "))
weight = float(input("What is your weight? "))

height = height / 100 
bmi = weight / height ** 2 

print(f"The BMI is {bmi}")

# Practice

user_input = int(input("Please enter a number "))
final_value = user_input * 5 
print(f"{user_input} * 5 is {final_value}")

user_name = input("What is your name? ")
user_birth_year = int(input("What year were you born? "))
age_by_2028 = 2028 - user_birth_year
print(f"Hi {user_name}, you will be {age_by_2028} years old at the end of the year 2028")


# Using Variables 

sum = 0 

number  = int(input("First Number: "))
sum += number 

number  = int(input("Second Number: "))
sum += number 

number  = int(input("Third Number: "))
sum += number 

print(f"The sum of all the numbers: {sum}")

sum = 0 
sum += int(input("First Number:"))
sum += int(input("Second Number: "))
sum += int(input("Third Number: "))

print(f"The sum of the numbers: {sum}")

# Practice

days = int(input("How many days? "))
seconds_value = days * 86400
seconds = print(f"There are {seconds_value} seconds in {days} days!")

number_1 = int(input("Please enter a number: "))
number_2 = int(input("Another one: "))
sum = number_1 + number_2 
product = number_1 * number_2 
print(f"The sum of the numbers is: {sum}")
print(f"The product of the numbers is: {product}")

value1 = int(input("Enter an integer: "))
value2 = int(input("Enter an integer: "))
value3 = int(input("Enter an integer: "))
value4 = int(input("Enter an integer: "))
number_value = int(input("Enter number of values inputed: "))

sum = value1 + value2 + value3 + value4
mean = sum / number_value
print(f"The sum of the number is {sum} and the mean is {mean}")


times_weekly = int(input("How many times a week do you eat at the student cafeteria? "))
prices = float(input("The price of a typical student lunch? "))
money_spent = float(input("How much money do you spend on groceries in a week? "))

print("Average food expenditure: ")
total_spent = prices * times_weekly + money_spent
weekly = total_spent
daily = total_spent / 7
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")


students_count = int(input("How many students in the course? "))
desired_group_size = int(input("Group Size? "))
number_groups_formed = students_count // desired_group_size
print(f"Number of possible groups: {number_groups_formed}")





