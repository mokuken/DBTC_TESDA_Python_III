# declare the person's name and age using dictionary
person = {"name" : "Joy", "age" : 18}

# add new key(gender) with a value(Female)
person["gender"] = "female"

# update the key(age) to a new value(19)
person["age"] = 19

# remove the gender key and it value to the dictionary
person.pop("gender")

# print the dictionary key and value
print(person)