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