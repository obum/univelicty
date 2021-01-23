import datetime # Already preinstalled in python
import pprint # Downloded the package and now imported
from prettytable import PrettyTable # Downloded the package and now imported


print(datetime.datetime.now())

time_now = datetime.datetime.now()

# print("hour :", time_now.day )
# print("min :", time_now.minute)
# print("second :", time_now.second)
# print("microsec :", time_now.microsecond)

# print(time_now.strftime("%A"))

# print(time_now.strftime("%b %d, %Y %I:%M%p"))

sample_date = "2020-20-12"

print(datetime.datetime.strptime(sample_date, "%Y-%d-%m").strftime("%b %d, %Y %I:%M%p"))


#----------------------------------------------------------------------------------------------------------------

# name = input("Enter your name > ")

# age = input("Enter your age > ")

# life_philosophy = input("what is your life_philosophy > ")


# bio_dict = dict()

# while True:
    
#     name = input("Enter your name > ")

#     age = input("Enter your age > ")

#     life_philosophy = input("what is your life_philosophy > ")
    
#     time_created = datetime.datetime.now().strftime("%b %d, %Y %I:%M%p")
    
#     action = input("Please do you want to add another ? (y/n): ")
    
#     bio_dict[name] = {
#         "age": age,
#         "life_philosphy" : life_philosophy,
#         "time_created": time_created,
#     }
    
#     if action == "n":
#         break
    
# pprint.pprint(f"Name : {name}, age : {age}")

# pprint.pprint(f"life_philosophy : {life_philosophy}")

# pprint.pprint(bio_dict)

# table = PrettyTable(['key', 'value'])
# for key, val in bio_dict.items():
#     table.add_row([key, val])
# print(table)












