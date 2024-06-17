# PascalCase: Capital the letter of class
# camelCase: Only first letter will be lower case and other in capital case
# snake_case: all letters in lower and separated by underscore(_)


# pass: the 'pass' statement is a null operation; it doesn't perform any action when executed.
# It's often used as a placeholder where syntactically a statement is required but no action is needed.

# # Creating a class:
# class User:
#     pass


# Creating a attribute
# user_1 = User()

# Adding attribute to a class
# user_1.id = '001'
# user_1.username = 'Dinkar'
#
# # Print attribute username
# print(user_1.username)

# Constructors
# initialise: to set (variables, counters, switches, etc.) to their starting values at the
# beginning of a program or subprogram

class User:
    # attribute
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # Method
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Dinkar")               # O/p for line 14-22 will be same
user_2 = User("002", "Patil")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# Method:
